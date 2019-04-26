#!/bin/bash

./textcleaner -g -e stretch -f 25 -o 20 -t 30 -u -s 1 -T -p 20 ac.jpg act.jpg

tesseract act.jpg stdout | speak
