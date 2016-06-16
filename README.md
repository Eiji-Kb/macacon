# macacon  
##Movie auto colorization converter(Dahl Automatic Colorization model wrapper) 
====
## Demo  


##Setup:  
1. Download the Automatic Colorization model by Ryan Dahl.  
2. http://tinyclouds.org/colorize/  

2. Save "macacon.py" and "macacon.sh" in the same folder.  

### Dependencies:
* Tensorflow   
* python (2.7 validation)  
* OpenCV3  
* numpy  


## movie
Basic usage:  

```
python macacon.py input_movie.mp4 output_movie.mp4
```

To display the monitor window
```
python macacon.py input_movie.mp4 output_movie.mp4 -m
```

Colorfulness control (This is addition functions. But not recommend. because unnatural.)
```
python macacon.py input_movie.mp4 output_movie.mp4 -c 3.2
```

## sound
Macacon does not process a sound track.   
Please process it separately.  
 e.g.  
  ・Video editing software (Recommend. I use AviUtl)  
  ・ffmpeg  
```
ffmpeg -i input_movie.mp4 -acodec copy -map 0:1 soundtrack.m4a
ffmpeg -i output_movie.mp4 -i soundtrack.m4a -vcodec copy -acodec copy output_movie_color.mp4
```

## movie+sound
Batch processing　（movie and sound）  

Dependencies:  
　ffmpeg  

Basic usage:  
```
sh ./macacon.sh  oronamin.mp4 neworonamin.mp4
```
To display the monitor window
```
sh ./macacon.sh -m -c 1.2 oronamin.mp4 neworonamin.mp4
```

Colorfulness control (This is addition functions. But not recommend. because unnatural.)
```
sh ./macacon.sh -c 2.8 oronamin.mp4 neworonamin.mp4
```


## Note:
* non-commercial  
* When you publish the colorization work,  
 You should respect the will of the movie director.  
