
import csv

import h5py
import numpy as np
from extract_cnn_vgg16_keras import VGGNet

'''
 Extract features and index the images
 Returns a list of filenames for all jpg images in a directory. 
'''
def get_imlist(path):
    with open(path, 'r') as f:
        first_column = [row[0] for row in csv.reader(f, delimiter=' ')]
        return first_column[2:]


if __name__ == "__main__":

    db = img_paths = 'list_eval_partition.txt'
    img_list = get_imlist(db)

    print("--------------------------------------------------")
    print("         feature extraction starts")
    print("--------------------------------------------------")

    feats = []
    names = []

    model = VGGNet()
    for i, img_path in enumerate(img_list):
        norm_feat = model.extract_feat(".."+img_path)
        #img_name = os.path.split(img_path)[1]
        feats.append(norm_feat)
        names.append(img_path)
        print("extracting feature from image No. %d , %d images in total" %
              ((i + 1), len(img_list)))

    feats = np.array(feats)
    output = 'featureCNN.h5'

    print("--------------------------------------------------")
    print("      writing feature extraction results ...")
    print("--------------------------------------------------")

    h5f = h5py.File(output, 'w')
    h5f.create_dataset('dataset_feat', data=feats)
    h5f.create_dataset('dataset_name', data=np.array(names, dtype='S'))
    h5f.close()
