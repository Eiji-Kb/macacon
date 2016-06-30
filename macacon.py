import tensorflow as tf
import numpy as np
import cv2
import argparse
import time

start_time = time.time()

parser = argparse.ArgumentParser() 
parser.add_argument("inputMovie", type=file) 
parser.add_argument("outputMovie") 
parser.add_argument("-m", const=1, nargs="?")
parser.add_argument("-c", default=0, type=float, nargs="?") 
args = parser.parse_args()
inputMovie = args.inputMovie
outputMovie = args.outputMovie

cap = cv2.VideoCapture(inputMovie.name)

heightInputMovie = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
widthInputMovie = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
FPS = cap.get(cv2.CAP_PROP_FPS)
allFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print ("Width  =", widthInputMovie)
print ("Height =", heightInputMovie)
print ("FPS =", FPS)
print ("Frames =", allFrames)

fourcc = "XVID"
out = cv2.VideoWriter(outputMovie, cv2.VideoWriter_fourcc(*fourcc), FPS, (widthInputMovie,heightInputMovie))

with open("colorize.tfmodel", mode='rb') as f:
	fileContent = f.read()

graph_def = tf.GraphDef()
graph_def.ParseFromString(fileContent)
grayscale = tf.placeholder("float", [1, 224, 224, 1])
tf.import_graph_def(graph_def, input_map={ "grayscale": grayscale }, name='')


with tf.Session() as sess:

	for frameNo in range(1, allFrames+1):

		print ("Frame no =", frameNo)
	
		ret, frame = cap.read()

		if ret == True:

			frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
			frame_rgb = (frame_rgb / 255.).astype(np.float32)
			frame_lab = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2Lab)
			frame_lab_l = frame_lab[:,:,0]
			frame_rgb_vgg = cv2.resize(frame_rgb, (224, 224))
			frame_rgb_vgg_gray = cv2.cvtColor(frame_rgb_vgg, cv2.COLOR_RGB2GRAY).reshape(1, 224, 224, 1)
			inferred_rgb = sess.graph.get_tensor_by_name("inferred_rgb:0")
			inferred_batch = sess.run(inferred_rgb, feed_dict={ grayscale: frame_rgb_vgg_gray })
			foward_rgb = cv2.resize(inferred_batch[0], (widthInputMovie, heightInputMovie), interpolation=cv2.INTER_CUBIC)
			frame_lab = cv2.cvtColor(foward_rgb, cv2.COLOR_RGB2Lab)
			if args.c:
				frame_lab *= args.c
			frame_lab_out = np.concatenate((frame_lab_l[:,:,np.newaxis], frame_lab[:,:,1,np.newaxis], frame_lab[:,:,2,np.newaxis]), axis=2) 
			frame_rgb_out = cv2.cvtColor(frame_lab_out, cv2.COLOR_Lab2RGB)
			frame_rgb_out = (frame_rgb_out * 255).astype(np.uint8)
			cvFrame = cv2.cvtColor(frame_rgb_out, cv2.COLOR_RGB2BGR)
			out.write(cvFrame)

			if args.m:
				cv2.imshow('frame', cvFrame)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	cap.release()
	out.release()
	cv2.destroyAllWindows()

	print ("Elapsed time:{0:.2f}".format(time.time() - start_time)) + "sec"

