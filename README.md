# picture-coloring

## 1. Prerequisites 
### 1.1 python & jupyter notebook
python version: 3.7 (available [here](https://www.python.org/downloads/))
Anaconda3 (available [here](https://www.anaconda.com/distribution/))

### 1.2 python packages
numpy, cv2, tensorflow (or tensorflow-gpu)

### 1.3 Colab
Our model is implemented by Tensorflow, and it is run and tested on Colab platform provided by Google. Thanks Google for providing free GPU to help fasten our building of our training and testing process.

## 2. Download Leeds Butterfly Dataset Locally
### 2.1 Clone this repository
```
cd "your desired directory"
git clone https://github.com/comp4901j-course-project/picture-coloring.git
cd picture-coloring/dataset
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

### 2.3 Get the input (edge map and grayscale) and output images
```
python cGANs_get_input_output.py
python CycleGAN_get_input_output.py
```

### 2.4 (Optional) Remove the original dataset
```
python remove_original_dataset.py
```
## 3. Upload Files to Colab (Your Google Drive)
### 3.1 Set up your Colab for your google drive account
After the default set up, there will be a directory named "Colab Notebooks" under your google drive. This is the directory where your files need to be uploaded.
```
For your setup, you can refer to:
```
### 3.2 Things needed to be uploaded
Things you need to uploaded to the directory "Colab Notebooks" on your google drive include:
```
# create directory on Google Drive
1. create a directory named "cGANs" under "Colab Notebooks"
2. create a directory named "dataset" under "Colab Notebooks/cGANs"

# cGANs model:
1. upload cGANs.ipynb into "Colab Notebooks/cGANs" directory
2. upload cGANs_input folder & cGANs_output folder into "Colab Notebooks/cGANs/dataset" directory

# CycleGAN model:
1. upload CycleGAN folder into "Colab Notebooks" directory
2. upload trainA & testA in CycleGAN_input_edge folder into "Colab Notebooks/CycleGAN/dataset/butterfly_edge" directory
3. upload trainB & testB in CycleGAN_output folder into "Colab Notebooks/CycleGAN/dataset/butterfly_edge" directory
4. upload trainA & testA in CycleGAN_input_grayscale folder into "Colab Notebooks/CycleGAN/dataset/butterfly_grayscale" directory
5. upload trainB & testB in CycleGAN_output folder into "Colab Notebooks/CycleGAN/dataset/butterfly_grayscale" directory
```

