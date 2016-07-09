# macacon  
##Movie auto colorization converter(Dahl Automatic Colorization model wrapper) 

## Demo  

https://www.youtube.com/watch?v=XrgQaVmeWbQ

https://www.youtube.com/watch?v=bNwa4Sk-2Yo

##Setup
1. Download the Automatic Colorization model by Ryan Dahl.  
   http://tinyclouds.org/colorize/  

2. Save "macacon.py" and "macacon.sh" in the same folder.  

### Dependencies:
* Tensorflow   
* python2.7
* OpenCV3  
* numpy  


## MOVIE
Basic usage:  

```
python macacon.py input_movie.mp4 output_movie.mp4
```

To display the monitor window
```
python macacon.py input_movie.mp4 output_movie.mp4 -m
```

Colorfulness control (Not recommend. because unnatural.)
```
python macacon.py input_movie.mp4 output_movie.mp4 -c 2.8
```

## SOUND
"macacon.py" does not process a sound track.   
Please process it separately.  
 e.g.  
  ・Video editing software 
  ・ffmpeg  
```
ffmpeg -i input_movie.mp4 -acodec copy -map 0:1 soundtrack.m4a
ffmpeg -i output_movie.mp4 -i soundtrack.m4a -vcodec copy -acodec copy output_movie_color.mp4
```

## MOVIE+SOUND Batch processing 

Dependencies:  
　ffmpeg  

Basic usage:  
```
sh ./macacon.sh input_movie.mp4 output_movie.mp4
```
To display the monitor window
```
sh ./macacon.sh -m input_movie.mp4 output_movie.mp4
```

Colorfulness control (Not recommend. because unnatural.)
```
sh ./macacon.sh -c 2.8 input_movie.mp4 output_movie.mp4
```


## Note:
* Non-commercial  
* When you publish your colorization work,You should respect the will of the movie director.  
* 日本語のブログは準備中です。
