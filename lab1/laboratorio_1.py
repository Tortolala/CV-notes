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

    new_img = img
    # Add padding to new_img

    return new_img


def connected_c(img):
    return True


def labelview(labels):
    return True

a = np.array([[ 1.,  1.,  1.,  1.,  1.],
            [ 1.,  1.,  1.,  1.,  1.],
            [ 1.,  1.,  1.,  1.,  1.]])

print(imgpad(a, 1))