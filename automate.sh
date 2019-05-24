#!/bin/bash
dt=$(date '+%d/%m/%Y %H:%M:%S');
start=`date +%s`
convert -respect-parenthesis \( ac.jpg -contrast-stretch 0 \) \
\( -clone 0 -colorspace gray -negate -lat 15x15+5% -contrast-stretch 0 \) \
-compose copy_opacity -composite -fill white -opaque none\
 -alpha off -modulate 100,200,100 act.jpg 

#Note that -contrast-stretch 0 will modify the image such that the image's min and max values are stretched to 0 and QuantumRange, respectively, without any loss of data due to burn-out or clipping at either end. 
#lat is used for adaptive thresholding, here in a 15X15 window
# negate used to negitive of image
# second parenthesis is basically a mask for first 
#modulate brightness[,saturation,hue] as percewntage
tesseract act.jpg stdout | espeak -g 1 -s 140 -w output.wav 
end=`date +%s`
echo "$((end-start))::$dt" >> log.txt
