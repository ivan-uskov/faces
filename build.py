#!/usr/local/bin/python
import os

X_MIN = "1.jpg"
X_MAX = "2.jpg"
Y_MIN = "3.jpg"
Y_MAX = "4.jpg"
Z_MIN = "5.jpg"
Z_MAX = "6.jpg"


def morph(src, dst, res_dir):
    os.system("python /app/face_morpher/facemorpher/morpher.py --src=" + src + " --dest=" + dst + " --background=transparent --out_frames=" + res_dir + " --num=12")


def average(src_dir, dst):
    os.system("python /app/face_morpher/facemorpher/averager.py --work=" + src_dir + " --background=transparent --out=" + dst)


def copy(src, dst):
    os.system("cp " + src + " " + dst)


def reset(p):
    os.system("rm -rf " + p)
    os.system("mkdir " + p)


os.environ["DLIB_DATA_DIR"] = "/app/dlib"

os.system("rm -rf /app/work")
os.system("mkdir /app/work")
os.system("mkdir /app/work/tmp")
os.system("mkdir /app/work/tmp/one")
os.system("mkdir /app/work/tmp/two")
os.system("mkdir /app/work/tmp/three")

work = "/app/work/tmp/avg"
result = "/app/result"
os.system("mkdir " + work)

morph("/app/source/" + X_MIN, "/app/source/" + X_MAX, "/app/work/tmp/one")
morph("/app/source/" + Y_MIN, "/app/source/" + Y_MAX, "/app/work/tmp/two")
morph("/app/source/" + Z_MIN, "/app/source/" + Z_MAX, "/app/work/tmp/three")

variants = ["frame001.png", "frame002.png", "frame003.png", "frame004.png", "frame005.png", "frame006.png", "frame007.png", "frame008.png", "frame009.png", "frame010.png"]

aC = 0
for a in variants:
    a_path = "/app/work/tmp/one/" + a
    bC = 0
    for b in variants:
        b_path = "/app/work/tmp/two/" + b
        cC = 0
        for c in variants:
            c_path = "/app/work/tmp/three/" + c
            reset(work)
            copy(a_path, work + "/1.png")
            copy(b_path, work + "/2.png")
            copy(c_path, work + "/3.png")
            average(work, result + "/" + str(aC) + "_" + str(bC) + "_" + str(cC) + ".png")
            cC += 1
        bC += 1
    aC += 1

os.system("rm -rf /app/work")
os.system("chown www-data:www-data -R /app/result")