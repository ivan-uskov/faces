rm -rf /app/work/result
mkdir /app/work/result
mkdir /app/work/result/one
mkdir /app/work/result/two
mkdir /app/work/result/three
mkdir /app/work/result/all

python /app/face_morpher/facemorpher/morpher.py \
     --src=/app/work/source/1.jpg \
     --dest=/app/work/source/2.jpg \
     --background=average \
     --out_frames=/app/work/result/one \
     --num=12

python /app/face_morpher/facemorpher/morpher.py \
     --src=/app/work/source/3.png \
     --dest=/app/work/source/4.png \
     --background=average \
     --out_frames=/app/work/result/two \
     --num=12

python /app/face_morpher/facemorpher/morpher.py \
     --src=/app/work/source/5.jpeg \
     --dest=/app/work/source/6.jpeg \
     --background=average \
     --out_frames=/app/work/result/three \
     --num=12