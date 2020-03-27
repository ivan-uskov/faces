#!/usr/local/bin/python
import os


def morph(src, dst, res_dir):
    os.system("python /app/face_morpher/facemorpher/morpher.py --src=" + src + " --dest=" + dst + " --background=average --out_frames=" + res_dir + " --num=12")

def average(src_dir, dst):
    os.system("python /app/face_morpher/facemorpher/averager.py --work=" + src_dir + " --out=" + dst)

def copy(src, dst):
    os.system("cp " + src + " " + dst)


def reset(p):
    os.system("rm -rf " + p)
    os.system("mkdir " + p)


os.system("rm -rf /app/work/tmp")
os.system("mkdir /app/work/tmp")
os.system("mkdir /app/work/tmp/one")
os.system("mkdir /app/work/tmp/two")
os.system("mkdir /app/work/tmp/three")

work = "/app/work/tmp/avg"
result = "/app/work/result"
os.system("mkdir " + work)

morph("/app/work/source/1.jpg", "/app/work/source/2.jpg", "/app/work/tmp/one")
morph("/app/work/source/3.png", "/app/work/source/4.png", "/app/work/tmp/two")
morph("/app/work/source/5.jpeg", "/app/work/source/6.jpeg", "/app/work/tmp/three")

variants = ["frame001.png", "frame002.png", "frame003.png", "frame004.png", "frame005.png", "frame006.png", "frame007.png", "frame008.png", "frame009.png", "frame010.png"]

aC = 1
for a in variants:
    a_path = "/app/work/tmp/one/" + a
    bC = 1
    for b in variants:
        b_path =  "/app/work/tmp/two/" + b
        cC = 1
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