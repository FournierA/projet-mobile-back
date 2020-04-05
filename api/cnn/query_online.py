
import h5py
import keras.backend.tensorflow_backend as tb
import numpy as np
from rest_framework.utils import json

from .extract_cnn_vgg16_keras import VGGNet


def get_result(new_img):
    # this line is important because of the attributeerror thread_local (when launched with Django !)
    tb._SYMBOLIC_SCOPE.value = True

    # read in indexed images' feature vectors and corresponding image names
    h5f = h5py.File('./cnn/featureCNN.h5', 'r')
    feats = h5f['dataset_feat'][:]
    imgNames = h5f['dataset_name'][:]
    h5f.close()

    print("--------------------------------------------------")
    print("               searching starts")
    print("--------------------------------------------------")

    # read query image
    queryDir = "./media/upload/"+new_img
    model = VGGNet()

    # extract query image's feature, compute similarity score and sort
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

    return np.array(result).tolist()