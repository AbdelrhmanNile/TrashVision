from flask import Flask, request, jsonify
from PIL import Image, ImageFile
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import io
import cv2
import os

ImageFile.LOAD_TRUNCATED_IMAGES = True
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

app = Flask(__name__)


model = tf.keras.models.load_model('/home/pirate/git/TrashVision/machinelearning/classifier/adam_0.0005_dropout_negcls/model_dropout_negcls_.h5', compile=False, custom_objects={'KerasLayer':hub.KerasLayer})

def detect(img):
    labels = ['metal', 'not-trash','plastic', 'glass']
    
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    
    prediction = model.predict([img, img])
    print(prediction)
    idx = np.argmax(prediction, axis=1)[0]
    print(labels[idx])
    
    return idx


@app.route('/classify', methods=['POST'])
def classify():

    img = Image.open(io.BytesIO(request.data))
    
    img = np.array(img)
    # save rgb image
    cv2.imwrite('test.jpg', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    #img = img / 255.0 # Normalize the image

    print("got the image")

    pred = detect(img)
    # Return the classification as JSON
    pred = int(pred)
    ##pred = int(input("enter num: "))
    return jsonify({'class': pred})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')