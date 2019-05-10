# picture-coloring

## 1. Prerequisites
### 1.1 python
python version: 3.7 (available [here](https://www.python.org/downloads/))

### 1.2 jupyter notebook
Anaconda3 (available [here](https://www.anaconda.com/distribution/))

### 1.3 python packages
numpy, cv2, tensorflow

## 2. Download Leeds Butterfly Dataset
### 2.1 Clone this repository
```
cd "your desired directory"
git clone https://github.com/comp4901j-course-project/coloring-edge-map.git
cd coloring-edges/dataset
```
### 2.2 Download Leeds Butterfly Dataset
```
python get_datasets.py
```
dataset available [here](http://www.josiahwang.com/dataset/leedsbutterfly/) <br>
citation: <br>
Josiah Wang, Katja Markert, and Mark Everingham <br>
Learning Models for Object Recognition from Natural Language Descriptions <br>
In Proceedings of the 20th British Machine Vision Conference (BMVC2009)

### 2.3 Get the input and output images
```
python get_input_output.py
```

### 2.4 Remove the original dataset
```
python remove_original_dataset.py
```
