# Classification Algorithms (LSTM & BERT)
[Folder for classification Algorithms](https://github.com/Adrianc1234/Final_Integrate_Project/tree/main/NLP_notebooks/Classification%20Algorithms)

Files:
- prediction_classification.py : Script used in deployment to request a prediction to the model reading .h5 model
- trans_senty.py : Script used in deployment to request a prediction to a transformer for getting a sentiment prediction (POSITIVE/NEGATIVE)
- [Model.H5 (Overfitting)](https://drive.google.com/file/d/1HRmDCHWGGISm-Ad_481R3VC_xXBn7jrH/view?usp=sharing)
- BERT (Not implemented in the service): BERTH classification notebook is inside of the folder and you can run it using this data: [data](https://drive.google.com/file/d/1yDyEMYoqwp4MksNDYSOceUP8lv3WK4NR/view?usp=sharing)
## LSTM
<img src="https://snipboard.io/vwcCst.jpg" alt="Girl in a jacket" width="1000" height="150">


## BERT Classification Neural Network 
<img src="https://snipboard.io/Ng1xIZ.jpg" alt="Girl in a jacket" width="500" height="500">
<img src="https://snipboard.io/dq51iu.jpg" alt="Girl in a jacket" width="1000" height="150">

----

# Generative Neural Network (RNN & LSTM)
[Generative Folder](https://github.com/Adrianc1234/Final_Integrate_Project/tree/main/NLP_notebooks/Generative%20Text)

Files:
- LSTM text generator notebook: LSTM_Text_Generator.ipynb(inside of the folder)
- RNN text generator notebook:  RNN.ipynb(Inside of the folder) - you can run this with more opochs using this data: [data](https://drive.google.com/file/d/1yDyEMYoqwp4MksNDYSOceUP8lv3WK4NR/view?usp=sharing)
- RNN model beta 1 (20 epochs): [Model_Download](https://drive.google.com/drive/folders/1PzpdcldvvEk2RXuRsmvamBajXgchD8X1?usp=sharing)

## LSTM text generator
<img src="https://snipboard.io/a3ldOr.jpg" alt="LSTM Generator" width="1000" height="150">


## RNN Recurence Neural Network 
<img src="https://snipboard.io/t1xIhq.jpg" alt="Model layers" width="400" height="380">

You can generate text with our model beta version after downloading the folder [here](https://drive.google.com/drive/folders/1PzpdcldvvEk2RXuRsmvamBajXgchD8X1?usp=sharing)
Using it:
````python3
import tensorflow as tf
import pandas as pd
import numpy as np
import os
import time
from google.colab import drive
import nltk
nltk.download('stopwords')
drive.mount('/content/drive')

one_step_reloaded = tf.saved_model.load('/content/drive/MyDrive/cuatrimestres/Noveno cuatri/Natural Language Preprocessing/Project/one_step')
states = None
next_char = tf.constant(['I really hate this '])
result = [next_char]

for n in range(1500):
  next_char, states = one_step_reloaded.generate_one_step(next_char, states=states)
  result.append(next_char)

print(tf.strings.join(result)[0].numpy().decode("utf-8"))

````
You can insert your string in `next_chart` variable, running our model with that one we got:
<img src="https://snipboard.io/jaQ2V0.jpg" alt="Model layers" width="1000" height="380">
