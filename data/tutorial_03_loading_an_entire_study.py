# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 14:29:40 2016

@author: pearsonp
"""

from segment import * # read all of segment.py into working memory
import matplotlib.pyplot as plt # for plotting

d = Dataset("train/1","1") # could replace 1 by anything between 1 and 500
d.load()

print( d.images.shape ) # should be a 4d array (num slices, num times, height, width)

# Calculate the average images over all times.
# In the 4d array d.images, time is in the "second slot" (so use index "axis = 1" since indexing is zero based.)

m = np.mean( d.images, axis=1 )

# reality check: what is the shape of m?
print( m.shape ) # should get a 3d array (num slices, height, width)


# plot the first slice (index 0) -- double check: does this make sense?
fig1  = plt.figure()
plt.imshow(m[0,:,:], cmap="gray", interpolation="bicubic")
plt.colorbar()
fig1.suptitle("Mean (over time) + Gray colormap", fontsize=12)

