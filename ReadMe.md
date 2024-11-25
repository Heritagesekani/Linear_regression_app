# Power Output Prediction
Power output prediction using sklearn, FastAPI and Streamlit_app

## Table of contents
- [Description](#description)
- [Requirements](#requirements)
- [Getting started](#getting-started)
- [1. Train and save the model](#1-train and save the model)
- [2. Deploy FastAPI](#2-deploy-fastapi)
- [3. Run streamlit](#3-streamlit)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Example input and output](#example-input-and-output)
- [Filestructure](#file-structure)
- [license](#lisence)

##Description
This project provides an API and a stremlit application for predicting power output based on enviromental factors.The model uses Linear Regressio from Scikit-learn,trained on features including:

- Ambient Tenperature (AT)
- Exhaust Vacuum(V)
- Ambient Pressure (AP)
- Relative Humidity (RH)

The API is deployed using FastAPI, and a streamlit app provides an interface

#Requirements
To set up and run project you will need the following python package:
- 'fastapi'
-  'uvicorn'
-  'scikit-learn'
-  'pandas'
-  'joblib'
-  'numpy'
-  'streamlit'

You can install these dependency by running.
```bash
pip install -r requirement.txt
```
## Getting Started
follow these steps to set up and run the project.

1.Train and save model

Train a Linear_regression modeling using scikit-learn, train and save the trained model to the file for deployment
```bash
python linear_regressin_model.py
```

2.Deploy the FastAPI
The FastAPI application (`api.py`) loads the saved model and provides an endpoint for the predictions. Run it using `uvicorn`
```commandline
uvicorn api:app --reload
```
This will start the FastAPI server at   `http://127.0.0.1:8000`

3. Run streamlit
The streamlit app allows users to input values and retieve predictions
```bash
streamlit run app.py
```

##Usage

FastAPI Endpoints
-post/predict
-Description: Accept environmental parameters and returns a precise parameters and returns a prediction power output (PE).
-Input JASON:
```
-output JSON:
```bash
{
  "AT": 15.0,
  "v": 40.0
  "AP": 1000.0
  "RH": 75.0
}
```
- Output JSON:
```bash
{
 "prediction": 465.84
}
```

### Streamlit Application

The Streamlit app provides an interface for users to input values for AT, V, AP, and RH. When the Predict button is clicked, the app sends the values to the FastAPI endpoint and displays the predicted power output (PE).

## Example Input and output
Example Input:
AT = 15, V = 40, AP = 1000, RH = 75

Example Output:
Predicted Power Output (PE) = 465.84


##File structure
The project directory is structured as follows

```commandline
📦 linear_regression_app
├─ data
│  └─ data.xlsx
├─ model
│  └─ model.pkl
├─ src
├─ .gitignore
├─ app.py
├─ api.py
├─ linear_regression_model.py
├─ README.md
└─ requirements.txt
```
 
#power output visualization 

###Actual vs predicted values
![Training and validation loss](src/figure_1.png)

##Lisense
