import tensorflow as tf
import tensorflow_hub as hub
import cv2
import numpy as np
import argparse as ap
import os
import time

# disable tensorflow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

model = tf.keras.models.load_model('./adam_0.0005_dropout/model_dropout.h5', compile=False, custom_objects={'KerasLayer':hub.KerasLayer})

def detect(image_path):
    labels = ['metal', 'plastic', 'glass']
    
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    
    prediction = model.predict([img, img])
    idx = np.argmax(prediction, axis=1)[0]
    
    return idx
    

if __name__ == "__main__":
    parser = ap.ArgumentParser()

    parser.add_argument("-i", "--image", help="path to the image")
    
    args = parser.parse_args()
    
    detect(args.image)
    
    start = time.time()
    detect(args.image)
    end = time.time()
    print("time: ", end-start)
    
