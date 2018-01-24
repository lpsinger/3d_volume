# 3d_volume
DPGMM implementation for 3D, 2D and 1D density estimate from MCMC samples. 
Requirements:

* numpy
* scipy
* healpy
* lal
* cython

Based on the DPGMM mixture model implementation of https://github.com/thaines/helit/tree/master/dpgmm 

Installation (also installs dependencies if necessary):

    pip install git+https://github.com/wdpozzo/3d_volume

# HOT TO SETUP A VIRTUALENV ENVIRONMENT ON CLUSTERS AND INSTALLING THE REQUIRED PACKAGES THERE

    virtualenv destination_folder
    source destination_folder/bin/activate
    pip install git+https://github.com/wdpozzo/3d_volume

After logging out, one will need to activate the virtual environment by typing:

    source destination_folder/bin/activate
