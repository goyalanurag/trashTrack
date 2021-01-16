import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.applications import VGG16
from keras.layers import Dense, Flatten
from keras.models import Sequential, load_model
import cv2


if os.path.isfile('DATA/train/.DS_Store'):
    os.remove('DATA/train/.DS_Store')
if os.path.isfile('DATA/test/.DS_Store'):
    os.remove('DATA/test/.DS_Store')

datagen = ImageDataGenerator(rescale=1./255,
                             zoom_range=0.2)


trained_image = datagen.flow_from_directory('DATA/train',
                                            target_size=(32, 32),
                                            class_mode='categorical')

test_datagen = ImageDataGenerator(rescale=1./255)

test_image = test_datagen.flow_from_directory('DATA/test',
                                              target_size=(32, 32),
                                              class_mode='categorical')


def Train_Model():
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
    model.save('model.h5')


# Train_Model()

# testing a random img
img = cv2.imread('DATA/test/Low/1.jpg')


def Predict_Model(img):
    global trained_image
    new_model = load_model('model.h5')
    img = cv2.resize(img, (32, 32), 3)
    img = np.expand_dims(img, axis=0)
    img = img / 255
    prediction = new_model.predict_classes(img)
    my_dict = dict(trained_image.class_indices)
    prediction = prediction[0]
    for key, value in my_dict.items():
        if prediction == value:
            return key


print(Predict_Model(img))
