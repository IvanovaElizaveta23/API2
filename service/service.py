import io

import pandas as pd
from fastapi import UploadFile

import tensorflow as tf
import tensorflow_hub as hub

from tensorflow.keras.applications.efficientnet import preprocess_input

import numpy as np

from service.constants import CSV_URL, CLASSIFIER_URL, IMAGE_RES
from service.schema import Bird
import keras.utils as image


class BirdService:
    @staticmethod
    async def get_bird(file: UploadFile) -> Bird:
        df = pd.read_csv(CSV_URL)

        model = tf.keras.Sequential([hub.KerasLayer(CLASSIFIER_URL)])

        img = image.load_img(
            io.BytesIO(file.file.read()), target_size=(IMAGE_RES, IMAGE_RES)
        )

        x = image.img_to_array(img)
        x = 255 - x
        x /= 255
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        result = model.predict(x)
        predicted_class = np.argmax(result)

        class_number = str(predicted_class)
        class_name = df[df["id"].isin([predicted_class])]["name"].tolist()[0]

        return Bird(class_number=class_number, class_name=class_name)
