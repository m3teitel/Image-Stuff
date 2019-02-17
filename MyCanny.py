import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import time
import scipy.signal

def Mycanny(sigma):
<<<<<<< Updated upstream
    xKernal = cv.getGaussianKernel(ksize=5, sigma=0.4)
=======
    xKernal = cv.getGaussianKernel(ksize=15, sigma=0.05)
>>>>>>> Stashed changes
    yKernal = np.transpose(xKernal)

    img = cv.imread("3.jpg", cv.IMREAD_GRAYSCALE)

    conImg = scipy.signal.convolve(img, xKernal)
    conImg = scipy.signal.convolve(conImg, yKernal).astype(np.uint8)

<<<<<<< Updated upstream
    sobel_y = cv.Sobel(conImg, cv.CV_16S, 0, 1, ksize=3)
    sobel_x = cv.Sobel(conImg, cv.CV_16S, 1, 0, ksize=3)
    sobel_y = cv.convertScaleAbs(sobel_y)
    sobel_x = cv.convertScaleAbs(sobel_x)
    sobel_xy = cv.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)
    lopImgFinal = cv.convertScaleAbs(sobel_xy)
    angleMat = np.arctan2(sobel_y, sobel_x)
    angleMat = (angleMat * 180/np.pi)
    zeroMax = getHighestIntensity(sobel_xy, angleMat)
    cv.namedWindow("Image", cv.WINDOW_NORMAL)
    cv.resizeWindow("Image", 500, 500)
    cv.imshow("Image", zeroMax)
=======
    lopImg = cv.Laplacian(conImg, cv.CV_64F, 5)
    lopImgFinal = cv.convertScaleAbs(lopImg)

    cv.imshow("lop", lopImgFinal)
>>>>>>> Stashed changes
    cv.waitKey(0)
    cv.destroyAllWindows()

def getHighestIntensity(grad, angle):
    zeroMax = np.zeros((grad.shape[0], grad.shape[1]), dtype=np.uint8)

    for i in range(1, len(grad) - 1):
        for j in range(1, len(grad[0]) - 1):
            before = 255
            after = 255
            if (0 <= angle[i,j] < 22.5) or (157.5 <= angle[i,j] <= 180):
                before = grad[i, j - 1]
                after = grad[i, j + 1]
            elif (22.5 <= angle[i, j] < 67.5):
                before = grad[i - 1, j + 1]
                after = grad[i + 1, j - 1]
            elif (67.5 <= angle[i ,j] < 112.5):
                before = grad[i - 1, j]
                after = grad[i + 1, j]
            elif (112.5 <= angle[i,j] < 157.5):
                before = grad[i + 1, j - 1]
                after = grad[i - 1, j + 1]

            if (grad[i,j] >= before) and (grad[i,j] >= after):
                zeroMax[i,j] = grad[i,j]
            else:
                zeroMax[i,j] = 0
    return zeroMax
Mycanny(3)