# Power Output Prediction
Power output prediction using sklearn, FastAPI and Streamlit_app

## Table of contents
- [Description](#description)
- [Requirements](#requirements)
- [Getting started](#getting-started)
- [1. Train and save the model](#1-train and save the model)
- [2. Deploy FastAPI](@2-deploy-fastapi)
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

