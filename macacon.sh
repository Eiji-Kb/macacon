#!/bin/sh

FLAG_M=FALSE
FLAG_C=FALSE
VALUE_C=
OPT=

while getopts mc: OPT
do
  case $OPT in
    m ) FLAG_M=TRUE ;;
    c ) FLAG_C=TRUE
		VALUE_C=$OPTARG ;;
    \?) echo "Usage: sh ./macacon.sh [-m] [-c value] input_movie.mp4 output_movie.mp4"
          exit 1 ;;
  esac
done

shift `expr $OPTIND - 1`

if [ "$FLAG_M" = "FALSE" ]; then
	if [ "$FLAG_C" = "FALSE" ]; then
    	python macacon.py $1 $2
	else
    	python macacon.py $1 $2 -c $VALUE_C
	fi
fi

if [ "$FLAG_M" = "TRUE" ]; then
	if [ "$FLAG_C" = "FALSE" ]; then
	    python macacon.py $1 $2 -m
	else
    	python macacon.py $1 $2 -m -c $VALUE_C
	fi
fi

mv $2 temp_mcon1_$2
ffmpeg -y -i $1 -acodec copy -map 0:1 temp_mcon1_soundtrack.m4a
ffmpeg -y -i temp_mcon1_$2 -i temp_mcon1_soundtrack.m4a -vcodec copy -acodec copy $2

if test -f $2 ;then
	rm temp_mcon1_$2
    rm temp_mcon1_soundtrack.m4a
fi

