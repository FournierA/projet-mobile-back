
import numpy as np
import h5py
import csv
import os

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import keras.backend.tensorflow_backend as tb
from rest_framework.utils import json

from .extract_cnn_vgg16_keras import VGGNet


def get_result(new_img):
    # this line is important because of the attributeerror thread_local (when launched with Django !)
    tb._SYMBOLIC_SCOPE.value = True

    # read in indexed images' feature vectors and corresponding image names
    # h5f = h5py.File(args["index"], 'r')

    h5f = h5py.File('./cnn/featureCNN.h5', 'r')
    feats = h5f['dataset_feat'][:]
    imgNames = h5f['dataset_name'][:]
    h5f.close()

    print("--------------------------------------------------")
    print("               searching starts")
    print("--------------------------------------------------")

    # read and show query image
    # queryDir = args["query"]
    # queryDir = './database/001_accordion_image_0001.jpg'

    queryDir = "./media/upload/"+new_img

    # queryImg = mpimg.imread(queryDir)
    # plt.figure()
    # plt.subplot(2, 1, 1)
    # plt.imshow(queryImg)
    # plt.title("Query Image")
    # plt.axis('off')

    # init VGGNet16 model
    model = VGGNet()

    # extract query image's feature, compute simlarity score and sort
    queryVec = model.extract_feat(queryDir)
    scores = np.dot(queryVec, feats.T)
    rank_ID = np.argsort(scores)[::-1]
    rank_score = scores[rank_ID]
    print(rank_ID)
    print(rank_score)

    # number of top retrieved images to show
    maxres = 5
    imlist = [imgNames[index] for i, index in enumerate(rank_ID[0:maxres])]
    print("top %d images in order are: " % maxres, imlist)

    result = []
    for i, im in enumerate(imlist):
        tmp = {"img_path": im.decode('UTF-8'), "score": rank_score[i].item()}
        result.append(tmp)

    json_result = json.dumps(np.array(result).tolist())
    print("RESULT", json_result)

    # show top  # maxres retrieved result one by one
    # for i, im in enumerate(imlist):
    #     image = mpimg.imread(im.decode('UTF-8'))
    #     plt.subplot(2, 5, i+6)
    #     plt.imshow(image)
    #     plt.title("search output %d" % (i + 1))
    #     plt.axis('off')
    # plt.show()

    return np.array(result).tolist()

# get_result("DSC_0015.jpg")