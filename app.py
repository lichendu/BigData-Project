#!/usr/bin/env python
#-*- coding: utf-8 -*- 

import tensorflow as tf
from PIL import Image
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
from flask import Flask, request
from redis import Redis, RedisError
import os
import db

app = Flask(__name__)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        image_path= request.files['file']
        ckpt_dir="./ckpt"
        upload_filename=image_path.filename
        result= str(loadmodel(image_path, ckpt_dir))
    return result
    


def loadmodel(img_path=None, ckpt_dir="./ckpt"):
    if img_path is None:
        return 
    # 1. define a session
    sess = tf.Session()
    # 2.1 checkpoint dir
    ckpt_dir = ckpt_dir
    # 2.2 find the lastest checkpoint path
    ckpt = tf.train.get_checkpoint_state(ckpt_dir)
    print(ckpt)
    # 3. load
    if ckpt and ckpt.model_checkpoint_path:
        # 3.1 coumpute graph
        saver = tf.train.import_meta_graph(ckpt.model_checkpoint_path + ".meta", clear_devices=True)
        # 3.2 load weights
        saver.restore(sess, ckpt.model_checkpoint_path) 

    # 4. load input and label tensor
    x_op = sess.graph.get_tensor_by_name("Placeholder:0")
    predict_op = sess.graph.get_tensor_by_name("Softmax:0")

    # 5. read inputs
    img = Image.open(img_path).convert('L')     
    flatten_img = np.reshape(img, 784)
    x = np.array([1 - flatten_img])

    # 6. predict
    y = sess.run(predict_op, feed_dict={x_op: x})
    result = np.argmax(y[0])

    return result


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)






