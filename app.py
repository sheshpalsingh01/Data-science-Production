from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
import sys
from src.Datascience.pipeline.prediction_pipelien import PredictionPipeline


app = Flask(__name__, template_folder="template")

@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")

    

@app.route("/train",methods=["GET"])
def train():
    os.system(f"{sys.executable} main.py")
    return "Training Pipeline has run successfully."

@app.route("/predict",methods=["POST","GET"])
def predict():
    if request.method == "POST":
        try:
            fixed_acidity = float(request.form.get("fixed_acidity"))
            volatile_acidity = float(request.form.get("volatile_acidity"))
            citric_acid = float(request.form.get("citric_acid"))
            residual_sugar = float(request.form.get("residual_sugar"))
            chlorides = float(request.form.get("chlorides"))
            free_sulfur_dioxide = float(request.form.get("free_sulfur_dioxide"))
            total_sulfur_dioxide = float(request.form.get("total_sulfur_dioxide"))
            density = float(request.form.get("density"))
            pH = float(request.form.get("pH"))
            sulphates = float(request.form.get("sulphates"))
            alcohol = float(request.form.get("alcohol"))

            data = np.array([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]])
            prediction = PredictionPipeline().predict(data)
            return render_template("results.html", prediction=prediction[0])
        except Exception as e:
            # logger.error(f"Error in prediction: {e}")
            return f"Error in prediction: {e}"
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)
    