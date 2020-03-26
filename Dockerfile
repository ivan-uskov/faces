FROM jjanzic/docker-python3-opencv

COPY . /app

RUN cd /app
RUN pip install -r /app/face_morpher/requirements.txt
RUN echo "export DLIB_DATA_DIR=/app/dlib" >> /root/.bashrc