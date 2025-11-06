from ast import Import
#from flask_ngrok import run_with_ngrok
import webbrowser
# from importlib.metadata import requires
from flask import Flask, flash, redirect, render_template, request
import cv2
from werkzeug.utils import secure_filename
import numpy
from matplotlib import pyplot as plt
import joblib
from functions import helpers


# Configure application
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Set secret key for session management
app.secret_key = "your_secret_key_here"

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# APP ROUTES

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")
    

@app.route("/crop_recommendation", methods=["GET", "POST"])
def crop_prediction():
    # If user reached route via POST
    if request.method == "POST":
        n = request.form.get("n")
        p = request.form.get("p")
        k = request.form.get("k")
        temperature = request.form.get("temperature")
        humidity = request.form.get("humidity")
        ph = request.form.get("ph")
        rainfall = request.form.get("rainfall")

        prediction = helpers.crop_predict(n, p, k, temperature, humidity, ph, rainfall)

        return render_template("crop_result.html", prediction=prediction)


    # If user reached route via GET
    else:
        return render_template("crop_form.html")


@app.route("/yield_prediction", methods=["GET", "POST"])
def yieldprediction():
    # def yieldPredict(state,Crop_Year,season,crop,area,model,mydict):
    # If user reached route via POST
    if request.method == "POST":
        state = request.form.get("state")
        crop_year = request.form.get("crop_year")
        season = request.form.get("season")
        crop = request.form.get("crop")
        area = request.form.get("area")

        prediction = helpers.yield_predict(state, crop_year, season, crop, area)

        return render_template("yield_result.html", prediction = prediction)

    # If user reached route via GET
    else:
        return render_template("yield_form.html")


@app.route("/disease_detection", methods=["GET", "POST"])
def disease():
    # If user reached route via POST
    if request.method == "POST":
        plant_name = request.form.get("plant_name")
        disease_name = request.form.get("disease_name")
        
        if not plant_name or not disease_name:
            flash('Please select both plant type and disease type')
            return render_template("disease_form.html")
        
        # Load disease information from JSON file
        import json
        import os
        
        json_path = os.path.join(app.root_path, 'functions', 'plant_diseases.json')
        try:
            with open(json_path, 'r') as f:
                diseases_data = json.load(f)
                
            disease_info = diseases_data.get(plant_name, {}).get(disease_name)
            return render_template("disease_result.html",
                                 plant_name=plant_name,
                                 disease_name=disease_name,
                                 disease_info=disease_info)
        except Exception as e:
            flash('Error loading disease information')
            return render_template("disease_form.html")

    # If user reached route via GET
    else:
        return render_template("disease_form.html")



@app.route("/weed_detection", methods=["GET", "POST"])
def weeddetection():
    # If user reached route via POST
    if request.method == "POST":
        soil_type = request.form.get("soil_type")
        moisture_level = request.form.get("moisture_level")
        season = request.form.get("season")
        weed_density = request.form.get("weed_density")
        weed_height = request.form.get("weed_height")
        leaf_shape = request.form.get("leaf_shape")

        # Load weed dataset
        import json
        import os
        
        json_path = os.path.join(app.root_path, 'functions', 'weed_dataset.json')
        try:
            with open(json_path, 'r') as f:
                weed_data = json.load(f)
            
            # Convert input values to match dataset format
            moisture_level = float(moisture_level) if moisture_level.isdigit() else moisture_level
            weed_density = float(weed_density)
            weed_height = float(weed_height)
            
            # Find best matching weed based on characteristics
            best_match = None
            min_diff = float('inf')
            
            for weed in weed_data['weed_data']:
                # Calculate similarity score based on input parameters
                moisture_diff = abs(weed['moisture'] - moisture_level) if isinstance(weed['moisture'], (int, float)) else 0
                density_diff = abs(weed['density'] - weed_density)
                height_diff = abs(weed['height'] - weed_height)
                
                # Give more weight to exact matches
                total_diff = moisture_diff + density_diff + height_diff
                if (weed['soil_type'] == soil_type and 
                    weed['season'] == season and 
                    weed['leaf_shape'] == leaf_shape):
                    total_diff *= 0.5
                
                if total_diff < min_diff:
                    min_diff = total_diff
                    best_match = weed
            
            if best_match:
                return render_template("weed_result.html",
                                     threat_level=best_match['weed_info']['threat_level'],
                                     threat_class=best_match['weed_info']['threat_class'],
                                     scientific_name=best_match['weed_info']['scientific_name'],
                                     common_name=best_match['weed_info']['common_name'],
                                     weed_description=best_match['weed_info']['weed_description'],
                                     control_measures=best_match['weed_info']['control_measures'])
            else:
                flash('No matching weed found in database')
                return render_template("weed_form.html")
        except Exception as e:
            flash('Error processing weed detection')
            return render_template("weed_form.html")
    
    # If user reached route via GET
    else:
        return render_template("weed_form.html")
    


if __name__ == '__main__':
    
    app.run(debug = True)
    # webbrowser.open_new("http://127.0.0.1:5000/")
