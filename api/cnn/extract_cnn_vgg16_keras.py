
import numpy as np
from numpy import linalg as LA

from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input

from os import listdir
from os.path import isfile, isdir, join
from keras.layers.core import Dense, Flatten
from keras.engine.training import Model
from keras import optimizers
from keras.callbacks.callbacks import EarlyStopping, ModelCheckpoint
from keras.engine.sequential import Sequential

#from sklearn.cluster import KMeans


class VGGNet:
    def __init__(self):
        self.input_shape = (224, 224, 3)
        self.weight = 'imagenet'
        self.pooling = 'avg'
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

    """ def features_list_in_cluster(self):
        vgg16_feature_list = []

        rootpath = ".\\dataset-retr\\train\\"
        subdir = ['MEN\\', 'WOMEN\\']

        # Parcours MEN puis WOMEN
        for idx, item in enumerate(subdir):
            pathname = rootpath + item
            print("[dir] ", pathname)
            subsubdir = [ssd for ssd in listdir(
                pathname) if isdir(join(pathname, ssd))]

            # Parcours Denim, etc
            for subidx, subitem in enumerate(subsubdir):
                subsubdirname = pathname + subitem + '\\'
                print("[ssdir] ", subsubdirname)
                subsubsubdir = [sssd for sssd in listdir(
                    subsubdirname) if isdir(join(subsubdirname, sssd))]

                # Parcours id_XXX, etc
                for subsubidx, subsubitem in enumerate(subsubsubdir):
                    subsubsubdirname = subsubdirname + subsubitem
                    print("[sssdir] ", subsubsubdirname)
                    filenames = [f for f in listdir(
                        subsubsubdirname) if isfile(join(subsubsubdirname, f))]

                    # Parcours chaque files
                    for i, fname in enumerate(filenames):
                        print("[file {} number {} of {} max] ".format(
                            fname, idx, subdir.__len__()))
                        img = image.load_img(
                            subsubsubdirname+"\\"+fname, target_size=(224, 224))
                        img_data = image.img_to_array(img)
                        img_data = np.expand_dims(img_data, axis=0)
                        img_data = preprocess_input(img_data)

                        vgg16_feature = self.model.predict(img_data)
                        vgg16_feature_np = np.array(vgg16_feature)
                        vgg16_feature_list.append(vgg16_feature_np.flatten())

        vgg16_feature_list_np = np.array(vgg16_feature_list)
        km = KMeans(n_clusters=23, random_state=0).fit(vgg16_feature_list_np).predict()
        
        print("KMEANS : ", km)
        return km """
