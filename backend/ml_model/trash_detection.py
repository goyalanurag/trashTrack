import os
from datetime import datetime
import requests
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.applications import VGG16
from keras.layers import Dense, Flatten
from keras.models import Sequential, load_model
import cv2

cwd = os.path.dirname(os.path.realpath(__file__))

if os.path.isfile(f'{cwd}/data/train/.DS_Store'):
    os.remove(f'{cwd}/data/train/.DS_Store')
if os.path.isfile(f'{cwd}/data/train/low/.DS_Store'):
    os.remove(f'{cwd}/data/train/low/.DS_Store')
if os.path.isfile(f'{cwd}/data/train/medium/.DS_Store'):
    os.remove(f'{cwd}/data/train/medium/.DS_Store')
if os.path.isfile(f'{cwd}/data/train/high/.DS_Store'):
    os.remove(f'{cwd}/data/train/high/.DS_Store')
if os.path.isfile(f'{cwd}/data/test/.DS_Store'):
    os.remove(f'{cwd}/data/test/.DS_Store')
if os.path.isfile(f'{cwd}/data/test/low/.DS_Store'):
    os.remove(f'{cwd}/data/test/low/.DS_Store')
if os.path.isfile(f'{cwd}/data/test/medium/.DS_Store'):
    os.remove(f'{cwd}/data/test/medium/.DS_Store')
if os.path.isfile(f'{cwd}/data/test/high/.DS_Store'):
    os.remove(f'{cwd}/data/test/high/.DS_Store')


datagen = ImageDataGenerator(rescale=1./255,
                             zoom_range=0.2)


trained_image = datagen.flow_from_directory(f'{cwd}/data/train',
                                            target_size=(32, 32),
                                            class_mode='categorical')

test_datagen = ImageDataGenerator(rescale=1./255)

test_image = test_datagen.flow_from_directory(f'{cwd}/data/test',
                                              target_size=(32, 32),
                                              class_mode='categorical')


def train_model():
    global trained_image, test_image
    model = Sequential()
    conv_base = VGG16(weights='imagenet', include_top=False,
                      input_shape=(32, 32, 3))
    model.add(conv_base)
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(3, activation='softmax'))
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(trained_image, epochs=25,
              validation_data=test_image, validation_steps=1)
    model.save(f'{cwd}/model.h5')

if not os.path.isfile(f'{cwd}/model.h5'):
    train_model()

def predict_model(img):
    global trained_image   
    new_model = load_model(f'{cwd}/model.h5')
    img = cv2.resize(img, (32, 32), 3)
    img = np.expand_dims(img, axis=0)
    img = img / 255
    prediction = new_model.predict_classes(img)
    my_dict = dict(trained_image.class_indices)
    prediction = prediction[0]
    for key, value in my_dict.items():
        if prediction == value:
            return key

def scan_and_call():
    path = os.path.join(cwd, '../../img')
    path = os.path.abspath(path)

    with open(f'{path}/latest_timestamp', 'r') as f:
        latest = float(f.read().strip())

    new_dirs = []
    _latest = latest

    for _dir in os.listdir(path):
        name = os.path.abspath(os.path.join(path, _dir))
        try:
            assert os.path.isdir(name)
            subfiles = os.listdir(name)
            assert len(subfiles) == 2
            time = os.stat(name).st_ctime
            assert time > latest
            _latest = time
            time = datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')
            new_dirs.append((name, time))
        except AssertionError:
            pass

    with open(f'{path}/latest_timestamp', 'w') as f:
        f.write(str(_latest))

    for _dir, timestamp in new_dirs:    
        coordinates = open(f'{_dir}/location.txt', 'r').read().strip()
        coordinates = coordinates.replace(' ', '')

        image = f'{_dir}/trash_image.jpg'
        amount = predict_model(image)

        status_map = {'low': 'green', 'medium': 'yellow', 'high': 'red'}
        status = status_map[amount]

        data = {'coordinates': coordinates, 'image': image, 'timestamp': timestamp, 'amount': amount, 'status': status}
        requests.post('http://localhost:4000/api/postData', json=data)
