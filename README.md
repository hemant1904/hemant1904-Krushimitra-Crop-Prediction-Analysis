# 🌾 Crop Prediction Analysis — Krushimitra

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-Image%20Processing-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**An AI-powered agricultural assistant that enables data-driven decisions for crop selection, yield prediction, disease detection & weed identification.**

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Model Accuracy](#model-accuracy)

</div>

---

## 📌 About the Project

Farmers often struggle with unpredictable climate, nutrient imbalance & lack of precise information. **Krushimitra** leverages Machine Learning & Image Processing to analyze soil properties, weather conditions & past performance — enabling smarter agricultural decisions.

---

## ✨ Core Features

### 🌱 Crop Recommendation
- Inputs: N, P, K, Temperature, Humidity, pH, Rainfall  
- Suggests the best suited crops  
- **Accuracy: 97.8%**

### 📊 Yield Prediction
- Predicts expected yield per hectare based on historical patterns  
- **Accuracy: 95.6%**

### 🦠 Disease Detection
- Uses OpenCV & CNN to identify plant diseases & recommend treatments  
- **Accuracy: 86.4%**

### 🌿 Weed Identification
- Detects weed species & suggests removal strategies  
- **Accuracy: 80.4%**

---

## 🛠 Tech Stack

| Category | Tools |
|---------|-------|
| Language | Python 3.x |
| ML | Scikit-learn, Pandas, NumPy |
| Image Processing | OpenCV |
| Dev Tools | Jupyter Notebook, VS Code, Git |
| Data Source | Kaggle (Agriculture datasets) |

---

## 🚀 Installation

```bash
git clone https://github.com/yourusername/crop-prediction-analysis.git
cd crop-prediction-analysis

python -m venv venv
source venv/bin/activate     # Windows → venv\Scripts\activate

pip install -r requirements.txt
Place datasets inside /data:

crop_recommendation.csv

yield_df.csv

disease_data.csv

weed_data.csv

Then run:

bash
Copy code
python app.py
Open in browser → http://127.0.0.1:5000

💻 Usage Examples
Crop Recommendation
python
Copy code
recommended_crop = predict_crop(14,15,20,35,90,7.0,200)
print(recommended_crop)
Yield Prediction
python
Copy code
predicted_yield = predict_yield("Maharashtra",2024,"Rabi","Chickpea",2500)
print(predicted_yield)
📈 Model Accuracy
Module	Algorithm	Accuracy
Crop Recommendation	Random Forest	97.8%
Yield Prediction	RF + Decision Tree	95.6%
Disease Detection	CNN + OpenCV	86.4%
Weed Detection	ML + Image Processing	80.4%

📞 Contact
Team Krushimitra
Project Link: https://github.com/yourusername/crop-prediction-analysis
Made with ❤️ for farmers & sustainable agriculture.
