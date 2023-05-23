from setuptools import setup, find_packages

setup(
  name = 'super_resolution',
  include_package_data = True,
  install_requires=[
    'accelerate',
    'beartype',
    'click',
    'datasets',
    'einops',
    'einops-exts',
    'ema-pytorch>=0.0.3',
    'fsspec',
    'kornia',
    'numpy',
    'packaging',
    'pillow',
    'pydantic',
    'pytorch-lightning',
    'pytorch-warmup',
    'sentencepiece',
    'torch>=1.6',
    'torchvision',
    'transformers',
    'tqdm'
  ],
)