from pymongo import MongoClient
import time
import cv2
import os
from dotenv import load_dotenv
load_dotenv("./.env")
import numpy as np

class DataBase:
    def __init__(self):
        self.client = MongoClient(os.getenv("db_url"))
        self.db = self.client[os.getenv("db_name")]
        self.collection = self.db[os.getenv("collection_name")]


    def insert_image(self, time_stamp, img, label=""):

        is_success, im_buf_arr = cv2.imencode(".jpg", img)
        binary_data = im_buf_arr.tobytes()

        self.collection.insert_one(
            {
                "_id": self.db_count + 1,
                "time": time_stamp,
                "img": binary_data,
                "label": label,
            }
        )

        self.db_count += 1
        return True

    #def data_generator(self):
    def data_generator(self):
        cursor = self.collection.find()
        for document in cursor:
            image_bytes = document["img"]
            image_array = np.frombuffer(image_bytes, dtype=np.uint8)
            image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
            label = document["label"]
            yield image, label


    def get_len(self):
        data = self.collection.find({})
        return int(data.explain()["executionStats"]["nReturned"])

    def remove_all(self):
        self.collection.delete_many({})
        return True

