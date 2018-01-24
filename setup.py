from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext as _build_ext


# https://stackoverflow.com/questions/19919905
class build_ext(_build_ext):
    def finalize_options(self):
        _build_ext.finalize_options(self)
        # Prevent numpy from thinking it is still in its setup process:
        __builtins__.__NUMPY_SETUP__ = False
        import numpy
        self.include_dirs.append(numpy.get_include())


setup(
      name = "3d_volume",
      ext_modules = [
                     Extension("cumulative",
                               sources=["cumulative.pyx"],
                               libraries=["m"] # Unix-like specific
                               )
      ],
      cmdclass={'build_ext': build_ext},
      py_modules=['VolumeLocalisation',
                  'dpgmm',
                  'gaussian',
                  'gaussian_inc',
                  'gaussian_prior',
                  'gcp',
                  'generate_submit_file',
                  'student_t',
                  'wishart'
                 ],
      install_requires=['healpy', 'numpy', 'scipy'],
      setup_requires=['cython', 'numpy', 'setuptools>=18.0']
      )