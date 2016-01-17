# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 19:08:19 2016

@author: pearsonp
"""

# Note: if a line starts with #, everything after # is a comment.
# Note: if a block is enclosed by """  """, it is a block comment.

#####################################
#  Comments on running this file

"""
To run this file, you will need Anaconda Python installed and also the 
pydicom package, which can be installed by running

    pip install pydicom
    
at the windows command prompt.

The files are organized as follows:

    tutorial_01_read_dicom_file.py
    train/1/study/sax_5/IM-4557-0001.dcm

Open "tutoral_01_read_dicom_file.py" in Spyder (Python 2.7).
In Spyder, click the green "run" arrow.
The output should be visible in the console panel of Spyder.
"""

#####################################
#  Load packages

"""
Note: Any time you run Python, some core packages are loaded 
automatically for you (so that things like addition, etc. are defined).
To use functions outside of the Python core, such as packages
for image processing, we need to load packages written by others
and contributed to Python.  These packages contain functions (or methods)
we can use so that we do not have to write them ourselves.
"""

import dicom # import the pydicom package for working with MRI data
import numpy as np # import the numerical python package for working with arrays of numbers, and refer to it as "np" instead of "numpy"
import os # import the operating system package for interacting with files


#####################################
#  Read a dcm file of an MRI image

"""
The dicom package has a method named read_file(filename).
If we just call read_file(filename), Python won't know where to find
The code.  If we call dicom.read_file(filename), then Python knows
to look for the read_file() method in the dicom package.  The syntax
"dicom.read_file()" is an example of using object oriented programming
in the sense that the syntax is of the form "object.method()".
"""

d = dicom.read_file("./train/1/study/sax_5/IM-4557-0001.dcm")

"""
Since the syntax for directories is slighty different in Windows, Mac,
and Linux operating systems (OS's), the Python "os" package provides a 
path.join() method that will work no matter what the OS is.  Here's
an alternative to what we just did:
"""

path_to_file = os.path.join("train","1","study","sax_5","IM-4557-0001.dcm")
d = dicom.read_file(path_to_file)

"""
We now have an object named d in Python's memory that contains all the 
information from the .dcm file.  By reading the pydicom package 
documentation, we could get a list of all the methods we could apply
to this object d.  If you open the file "IM-4557-0001.dcm" in Mango,
choose "File --> Image Info" from the menu, and then choose the "Header"
tab, you get a long list of properties for this particular MRI scan.
One of the properties listed is

  (0018,0050) Slice Thickness [6]

Let's try to access the Slice Thickness property of the object d and
print it to the screen.
"""

print(d.SliceThickness)

"""
It is possible that some of the MRI scans do not have a Slice Thickness
property.  So, in the future, we're going to want to write some code
that loops through all of the .dcm files, reads the properties of the
.dcm file, and writes the properties to a .csv spreadsheet file.  Doing
this will enable us to know which images are missing certain properties.
But, that's a future assignment.  Back to the task at hand!

The Slice Thickness should be a single number.  Some properties of the
object d are not a single number.  For instance, the Pixel Spacing 
property has both a horizontal and a vertical component to it, so it's
naturally a list of two numbers.  For our particular MRI scan, Mango
reports that the Pixel Spacing is
 
  (0028,0030) Pixel Spacing [1.5625,1.5625]

Let's try to access the Pixel Spacing attributes of the object d 
and print them to the screen.
"""

(x_pix_sp, y_pix_sp) = d.PixelSpacing
print(x_pix_sp, y_pix_sp)

"""
Assignment: Use Mango to look at the attributes of the .dcm file.
Then, find attributes that are relevant and try to access and view 
them in Python.  Relevant attributes may include:

- Manufacturer **
- Series Description
- Manufacturer's Model Name
- Patient ID **
- Patient's Sex **
- Angio Flag **
- Slice Thickness **
- Repetition Time **
- Echo Time **
- Number of Averages **
- Imaging Frequency **
- Echo Number(s)
- Magnetic Field Strength
- Percent Sampling
- Percent Phase Field of View
- Pixel Bandwidth **
- Software Version(s) **
- Trigger Time
- Nominal Interval
- Cardiac Number of Images **
- In-plane Phase Encoding Direction
- Flip Angle
- Variable Flip Angle Flag
- Patient Position
- Series Number **
- Acquisition Number **
- Instance Number **
- Image Position (Patient)
- Image Orientation (Patient)
- Slice Location **
- Samples per Pixel
- Rows **
- Columns **
- Smallest Image Pixel Value **
- Largest Image Pixel Value **
- Window Center **
- Window Width **
- Window Center & Width Explanation
""" 


############################################
#  Convert the pixels in the image to an array of numbers

"""
The object d of class dicom in Python has a pixel_array method defined
on it.  We can convert this pixel array into an honest-to-goodness 
array of numbers using the numpy (numerical python) package.  We then
print this array of numbers (it gets truncated because it's large).
"""

d_pix_ar = d.pixel_array
a = np.array(d_pix_ar)
print(a)


############################################
#  Accessing entries in the array of numbers

"""
We can access particular values of the array by their row and column index.
Since indexing in Python starts at 0 (not 1), we need to access the 
value in row 2 column 3 of the ndarray "a" as follows:
"""

print( a[1,2] ) # row 2, column 3 is indexed by 1,2

"""
We can also access multiple values of the array at once.  To access all 
entries in the first two rows and the first three columns use:
"""

print( a[0:2, 0:3]) # access rows indexed by 0,1 and columns indexed by 0,1,2

"""
So, a[x:y,:] means x is the index of the first row that you want, y is 
the index of the first row you do not want, and the colon in the second slot
means select all entries.  So, to print all the entries in the first two rows,
use:
"""

print( a[0:2,:] )


#############################################
#  Attributes of the array of numbers

"""
The number of rows and columns in the array can be found using the shape method.

"""

print( a.shape )

"""
We can find the number of rows and columns and then assign them names.
The "L" means "of integer type" (I think...)
"""

[nrow, ncol] = a.shape
print(nrow, ncol)

"""
For more on Python's ndarray see

    http://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html
"""