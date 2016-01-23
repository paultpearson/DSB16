# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 19:08:19 2016

@author: pearsonp
"""

#####################################
#  Comments on running this file

"""
To run this file, you will need Anaconda Python 2 installed and also the 
pydicom package, which can be installed by running

    pip install pydicom
    
at the windows command prompt.

The files are organized as follows:

    tutorial_02_plotting_and_fourier_analysis.py
    train/1/study/sax_5/IM-4557-0001.dcm
    ...
    train/1/study/sax_5/IM-4557-0030.dcm

Open "tutoral_02_plotting_and_fourier_analysis.py" in Spyder (Python 2.7).
In Spyder, click the green "run" arrow.
The output should be visible in the console panel of Spyder.
"""

#####################################
#  Load packages

import dicom # import the pydicom package for working with MRI data
import numpy as np # import the numerical python package for working with arrays of numbers, and refer to it as "np" instead of "numpy"
import os # import the operating system package for interacting with files
import matplotlib.pyplot as plt # for plotting
from skimage import exposure # for histogram equalization

#import cv2 # for histogram equalization
#from skimage import data, img_as_float


#####################################
#  Read a dcm file of an MRI image

"""
The code below is a user defined method (or function) named dicom_to_array().
Notice the declaration def for "define" at the beginning and the colon at the end of the first line.
Each line in the method is indented, and the function ends when the indentation stops.
The method reads a dicom file (input) and returns a numpy.array() of pixel values (output).
The input to this method is a path to a file that is referred to as "filename" throughout.
"""

def dicom_to_array(filename):
    d = dicom.read_file(filename)
    a = d.pixel_array
    return np.array(a)

t = 1
path_to_file = os.path.join("train","1","study","sax_5","IM-4557-%04d.dcm" % t)
a1 = dicom_to_array(path_to_file)


####################################
#  View some properties of the image

print(a1)

print( a1.shape ) # image width and height in pixels
print( 256 * 230 ) # total number of pixels in the image

# Use numpy.ndarray.min() and numpy.ndarray.max() to find the smallest and largest values in the array a1
print( np.ndarray.min(a1) )
print( np.ndarray.max(a1) )

# Use numpy.histogram() to calculate histogram data for the values in the ndarray a1
#hist,bins = np.histogram(a1.flatten(),256,[0,256])
hist,bins = np.histogram(a1, bins=256)
print( "histogram of pixel values", hist )
print( sum(hist) )

plt.figure() # create a new figure
plt.hist(a1) # plot a histogram of the pixel values


#########################################
#  Histogram equalization
#  http://scikit-image.org/docs/dev/auto_examples/plot_equalize.html

a1_eq = exposure.equalize_hist(a1)
hist_eq,bins_eq = np.histogram(a1_eq, bins=256)
print( "histogram equaliation of pixel values", hist_eq )
print( sum( hist_eq ) )
print( a1_eq )
print( np.ndarray.min(a1_eq) )
print( np.ndarray.max(a1_eq) )
print( a1_eq.shape )


#########################################
#  Plotting the image

"""
Now, we plot the original image (unmodified) and its histogram equalization.
We will do this with the "gray" colormap and the "spectral" colormap.
"""

############
# grayscale

fig1  = plt.figure()
plt.imshow(a1, cmap="gray", interpolation="bicubic")
plt.colorbar()
fig1.suptitle("Original + Gray colormap", fontsize=12)

fig2 = plt.figure()
plt.imshow(a1_eq, cmap="gray", interpolation="bicubic")
plt.colorbar()
fig2.suptitle("Histogram equalization + Gray colormap", fontsize=12)


############
# spectral

fig3  = plt.figure()
plt.imshow(a1, cmap="spectral", interpolation="bicubic")
plt.colorbar()
fig3.suptitle("Original + Spectral colormap", fontsize=12)

fig4  = plt.figure()
plt.imshow(a1_eq, cmap="spectral", interpolation="bicubic")
plt.colorbar()
fig4.suptitle("Histogram Equalization + Spectral colormap", fontsize=12)
