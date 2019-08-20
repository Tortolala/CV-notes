# Author: @tortolala
import argparse
import cv2 as cv
import numpy as np

parser = argparse.ArgumentParser(description='I/O files')
parser.add_argument('--input', help='Input file name', default='fprint3.pgm')
parser.add_argument('--output', help='Output file name', default='fprint3_ccl.png')
args = parser.parse_args()
# print(args.input, args.output) # Check arguments

def imgpad(img, r):

    v_padding = np.zeros((r, img.shape[1]))
    temp_matrix = np.r_[v_padding, img, v_padding]
    h_padding = np.zeros((temp_matrix.shape[0], r))
    new_matrix = np.c_[h_padding, temp_matrix, h_padding]
    return new_matrix


def connected_c(img):
    return True


def labelview(labels):
    return True

a = np.array([[ 1.,  1.,  1.,  1.,  1.],
            [ 1.,  1.,  1.,  1.,  1.],
            [ 1.,  1.,  1.,  1.,  1.]])


print(imgpad(a, 2))

