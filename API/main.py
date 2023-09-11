# Importing necessary libraries
import uvicorn
import dill as pickle
import pandas as pd
import numpy as np
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Initializing the fast API server
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Loading up the model
with open('../model/sentiment.pkl', 'rb') as file:
    model = pickle.load(file)
    
# Defining the model input types
class Analysis(BaseModel):
    input: str

# Setting up the home route
@app.get("/")
def read_root():
    return {"data": "This is a machine learning sentiment analysis model"}

# Setting up the analyze route
@app.post("/analyze/")
async def perform_analysis(data: Analysis):

    
    result = model(data.input)

    return {
        "data": {
            'result': result 
        }
    }

# Configuring the server host and port
if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
    
