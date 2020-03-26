#!/bin/bash

rm -rf /app/work/result
mkdir /app/work/result
mkdir /app/work/result/one
mkdir /app/work/result/two
mkdir /app/work/result/three
mkdir /app/work/result/all

morph () {
   python /app/face_morpher/facemorpher/morpher.py \
     --src=$1 \
     --dest=$2 \
     --background=average \
     --out_frames=$3 \
     --num=12
}

morph /app/work/source/1.jpg /app/work/source/2.jpg /app/work/result/one
morph /app/work/source/3.png /app/work/source/4.png /app/work/result/two
morph /app/work/source/5.jpeg /app/work/source/6.jpeg /app/work/three

for from in /app/work/result/one/*.png; do
    for to in /app/work/result/two/*.png; do
        morph $from $to /app/work/result/all
    done
done