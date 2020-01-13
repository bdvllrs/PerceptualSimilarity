from setuptools import find_packages, setup

setup(name='perceptual_similarity',
      version='1.0',
      install_requires=["torch>=0.4.0", "torchvision>=0.2.1", "numpy>=1.14.3",
                        "scipy>=1.0.1", "scikit-image>=0.13.0", "opencv-python>=2.4.11",
                        "matplotlib>=1.5.1", "tqdm>=4.28.1"],
      packages=find_packages(),
      package_data={'perceptual_similarity': ['weights/v0.0/*',
                                              'weights/v0.1/*']},
      include_package_data=True,
      )
