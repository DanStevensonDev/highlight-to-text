# Highlight to text

## Intro

This repo is for a mini personal project as a way for me to learn more about computer vision and Python. 

It uses OpenCV to extract highlighted text from book page images. 

## Installation

To run the project you will need Python and Conda installed and might need to install dependencies:

```
conda update anaconda-navigator  
conda update navigator-updater  
pip install opencv-python
conda install opencv 
```

Following this, run `python3 extract_underlined_text.py img.jpg` to try out the highlight extraction.

There's a test image already added (`img.jpg`) which you can replace. Currently the project looks for images highlighted in orange highlight marker.

You can also see a test output file (created by running the extraction command) at `result.txt`. 