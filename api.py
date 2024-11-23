import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from statsmodels.tsa.base import prediction

#load the saved model
model = joblib.load ("model/model.pkl")

# Instantiate FastAPI app
app = FastAPI()


class predictionInput(BaseModel):
    ambiant_temperature: float
    exhuast_vacuum: float
    ambiant_pressure: float
    relative_humdity: float


@app.post("/predict")
def predict(input_data: predictionInput):
    # prepare input data as numpy array
    data= np.array([[
        input_data.ambient_temperature,
        input_data.exhuast_vacuum,
        input_data.ambiant_pressure,
        input_data.relative_humidity
    ]])

    # make prediction
    prediction = model.predict(data)

    # return the prediction
    return {
        "prediction": prediction[0]
    }

# run the app with uvicorn
if __name__== "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)





