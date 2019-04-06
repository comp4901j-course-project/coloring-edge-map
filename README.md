# coloring-edges

## 1. Prerequisites
### "python" and "MATLAB"
python version: 3.7 <br>
MATLAB version: 2014b

## 2. Download BSDS500 dataset
### 2.1 Clone this repository
```
git clone "your desired directory"
git clone https://github.com/comp4901j-course-project/coloring-edges.git
cd coloring-edges
```
### 2.2 Download BSDS500 dataset
```
python get_datasets.py
```
dataset citation: 
Contour Detection and Hierarchical Image Segmentation
P. Arbelaez, M. Maire, C. Fowlkes and J. Malik.
IEEE TPAMI, Vol. 33, No. 5, pp. 898-916, May 2011.

### 2.3 Get the input and output images
```
# 1. get the input images
run the matlab file "get_input_images.m" in the pre-installed MATLAB software

# 2. get the output images
python get_output_images.py
```

### 2.4 Remove the original dataset
```
python remove_original_dataset.py
```
