import joblib
import os
import json

def crop_predict(N, P, K, temperature, humidity, ph, rainfall):
    """Predict suitable crop based on environmental parameters"""
    try:
        # Use relative path and proper path handling
        base_dir = os.path.dirname(__file__)
        model_path = os.path.join(base_dir, "crop_predict.pkl")
        
        # Load model with error handling
        try:
            model = joblib.load(model_path)
        except FileNotFoundError:
            return "Error: Crop prediction model not found. Please ensure the model file exists."
        
        # Validate and convert inputs
        inputs = [
            float(N), float(P), float(K),
            float(temperature), float(humidity),
            float(ph), float(rainfall)
        ]
        
        # Make prediction
        prediction = model.predict([inputs])
        return prediction[0]
    
    except Exception as e:
        return f"Prediction error: {str(e)}"

def disease_predict(plant_name, disease_name):
    """Get disease information and solution based on plant and disease name"""
    try:
        # Load disease dataset
        base_dir = os.path.dirname(__file__)
        data_path = os.path.join(base_dir, "plant_diseases.json")
        
        with open(data_path, 'r') as f:
            disease_data = json.load(f)
        
        # Validate inputs
        if plant_name not in disease_data:
            return None
            
        if disease_name not in disease_data[plant_name]:
            return None
            
        return disease_data[plant_name][disease_name]
        
    except json.JSONDecodeError:
        return None
    except FileNotFoundError:
        return None
    except Exception as e:
        return None

def yield_predict(state, crop_year, season, crop, area):
    """Predict agricultural yield with improved error handling"""
    try:
        # Validate numerical input
        area = float(area)
        if area <= 0:
            return "Error: Area must be a positive number"

        # Path handling
        base_dir = os.path.dirname(__file__)
        data_path = os.path.join(base_dir, "yieldpred.json")

        # Load JSON data directly
        with open(data_path, 'r') as f:
            data = json.load(f)

        # Validate inputs
        if state not in data:
            return f"Error: State '{state}' not found"
            
        if season not in data[state]:
            return f"Error: Season '{season}' not found in {state}"
            
        if crop not in data[state][season]:
            return f"Error: Crop '{crop}' not found in {state}/{season}"

        # Get base yield value
        base_yield = data[state][season][crop]
        
        # Calculate prediction (removed arbitrary 1.5 multiplier)
        prediction = area * base_yield
        
        return {

            "predicted_yield": round(prediction, 2),
            "base_yield_per_hectare": base_yield
        }

    except json.JSONDecodeError:
        return "Error: Invalid JSON data format"
    except FileNotFoundError:
        return "Error: Data file not found"
    except ValueError:
        return "Error: Invalid numerical input"
    except Exception as e:
        return f"Unexpected error: {str(e)}"