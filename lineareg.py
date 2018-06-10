import numpy as np
from numpy.linalg import inv
import sys

def main(argv):
    inputfile = argv[0]
    dataset = np.genfromtxt(inputfile, delimiter=',', skip_header=True)
    print("Dataset: ", inputfile)
    print(dataset)
    b = dataset[:, -1].copy()  # for last column
    A = dataset
    A[:, -1] = 1
    print("Matrix: ")
    print(A)
    print("Class Values: ")
    print(b)

    x = inv(np.transpose(A).dot(A)).dot(np.transpose(A)).dot(b)

    print("Weights: ")
    print(x)

if __name__ == "__main__":
 main(sys.argv[1:])