from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

import numpy as np
import pickle

app = FastAPI()

# Static + Templates
app.mount("/static", StaticFiles(directory="../frontend/static"), name="static")

templates = Jinja2Templates(directory="../frontend/templates")

# Load ML files
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
features = pickle.load(open("features.pkl", "rb"))



# HOME PAGE
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

# ABOUT PAGE
@app.get("/about", response_class=HTMLResponse)
async def about_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="about.html"
    )

# PREDICT PAGE
@app.get("/predict", response_class=HTMLResponse)
async def predict_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="predict.html"
    )

# PREDICTION LOGIC
@app.post("/predict")
async def predict(
    request: Request,

    aluminium: float = Form(...),
    arsenic: float = Form(...),
    barium: float = Form(...),
    cadmium: float = Form(...),
    chloramine: float = Form(...),
    chromium: float = Form(...),
    nitrates: float = Form(...),
    radium: float = Form(...),
    silver: float = Form(...),
    viruses: float = Form(...)
):

    data = np.array([[
    aluminium,
    arsenic,
    barium,
    cadmium,
    chloramine,
    chromium,
    viruses,
    nitrates,
    radium,
    silver
]])

    scaled = scaler.transform(data)

    prediction = model.predict(scaled)[0]
    
    print("Prediction Value =", prediction)

    result = "Safe Water" if prediction == 1 else "Unsafe Water"

    return templates.TemplateResponse(
    request=request,
    name="result.html",
    context={
        "prediction": result
    }
)