# skin-care

## Description
In this project we were tasked with creating a neural network that can identify images of skin lesions in 7 classes and with deploying this model.  This project was based on [This Kaggle Challenge](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000?select=HAM10000_metadata.csv). The neural net is inspired on the [AlexNet](https://dl.acm.org/doi/10.1145/3065386) architecture

The deployed app can be found [here](https://ancient-bastion-46676.herokuapp.com/)

## Installation

### The app

To run the app one can create a Docker container with the Dockerfile. If you are not familiar with docker, you can create a virtual environment and download everything mentioned in the requirements.txt file. Then run app.py. Open a browser. The app should load when surfing to [http://127.0.0.1:4000/](http://127.0.0.1:4000/)

### Notebooks
This repository also contains two notebooks. These notebooks were used to create the neural net and are not necessary for running the app. 

The notebooks expect the [HMNIST dataset](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000?select=HAM10000_metadata.csv), downloaded inside a folder called data. The folder_creator.ipynb notebook will create new directories from this data based on the type of lesion and wether it shoudl go in the train, test or validation set.
The model_creator.ipynb is where the model is trained.

