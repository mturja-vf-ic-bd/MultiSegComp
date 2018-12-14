import os
from glob import glob
import nrrd #pip install pynrrd, if pynrrd is not already installed
import nibabel as nib #pip install nibabel, if nibabel is not already installed
import numpy as np
import sys
import pprint
file = sys.argv[1]

#load nrrd
_nrrd = nrrd.read(file)
data = _nrrd[0]
header = _nrrd[1]
affine = np.array([[-1, 0, 0, 0], [0, -1, 0, 0], [0, 0 , 1, 0], [0, 0, 0, 1]])
img = nib.Nifti1Image(data, affine)
outfile = os.path.join(file.split('.')[0] + '.nii.gz')
print(outfile)
nib.save(img, outfile)