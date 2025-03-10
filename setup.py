import sys

from setuptools import setup

sys.argv.append('sdist')

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='char_art',
    version='0.1.0',
    packages=['char_art'],
    install_requires=['opencv-python', 'numpy'],
    python_requires='>=3.6.0',
    license='MIT',
    description='方便地制作字符画与字符视频 ~',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['char_art', 'character image', 'character video'],
    author='Liu Wei',
    author_email='23S112099@stu.hit.edu.cn',
    maintainer='Liu Wei',
    maintainer_email='23S112099@stu.hit.edu.cn',
    url='https://github.com/AomandeNiuma/char_art',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13'
    ]
)
