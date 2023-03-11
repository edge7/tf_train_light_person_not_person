import time

import cv2
import os
import numpy as np
os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python'
import tensorflow as tf


def real_time():
    model_fitted = tf.keras.models.load_model(
        'model.h5', custom_objects=None, compile=False,
        options=None
    )
    for layer in model_fitted.layers:
        if 'dropout' in layer.name:
            layer.rate = 0

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
    while cap.isOpened():
        try:
            success, image = cap.read()
            if not success or image is None or image.shape[0] == 0:
                print("Ignoring empty camera frame.")
                # If loading a video, use 'break' instead of 'continue'.
                continue
            gray_scale =  cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gray_scale_resized = cv2.resize(gray_scale, (128, 128)) / 255.0
            prediction = model_fitted.predict(np.expand_dims(gray_scale_resized, 0))[0][0]
            if prediction > 0.5:
                print("Person identified ", round(prediction, 3))
            else:
                print("No person identified", round(prediction, 3))
            time.sleep(2)
            # cv2.imshow('Frame recorded', raw)
            if cv2.waitKey(5) & 0xFF == 27:
                break
        except Exception as e:
            print(e)
            pass
    cap.release()

real_time()