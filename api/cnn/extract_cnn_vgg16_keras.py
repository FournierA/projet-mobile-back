
import numpy as np
from keras import optimizers
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
from keras.engine.training import Model
from keras.layers.core import Dense, Flatten
from keras.preprocessing import image
from numpy import linalg as LA


class VGGNet:
    def __init__(self):
        self.input_shape = (224, 224, 3)
        self.weight = 'imagenet'
        self.pooling = 'max'
        self.model = VGG16(weights=self.weight, input_shape=(
            self.input_shape[0], self.input_shape[1], self.input_shape[2]), pooling=self.pooling, include_top=False)

        self.X = self.model.layers[-2].output
        self.X = Flatten()(self.X)
        self.X = Dense(units=4096, activation="relu")(self.X)
        self.X = Dense(units=4096, activation="relu")(self.X)
        self.X = Dense(units=3, activation="softmax")(self.X)

        for layers in (self.model.layers)[:19]:
            layers.trainable = False

        self.model.predict(np.zeros((1, 224, 224, 3)))
        self.model_final = Model(input=self.model.input, output=self.X)
        self.model_final.compile(loss="categorical_crossentropy", optimizer=optimizers.SGD(
            lr=0.0001, momentum=0.9), metrics=["accuracy"])

        self.model_final.summary()

    '''
    Use vgg16 model to extract features
    Output normalized feature vector
    '''

    def extract_feat(self, img_path):
        img = image.load_img(img_path, target_size=(
            self.input_shape[0], self.input_shape[1]))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = preprocess_input(img)
        feat = self.model.predict(img)
        norm_feat = feat[0]/LA.norm(feat[0])
        return norm_feat
