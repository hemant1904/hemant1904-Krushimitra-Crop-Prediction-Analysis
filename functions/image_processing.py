import cv2
import numpy as np
import os
import json
from pathlib import Path

def preprocess_image(image):
    """Preprocess image for comparison"""
    # Resize image to standard size
    image = cv2.resize(image, (224, 224))
    # Convert to RGB if needed
    if len(image.shape) == 2:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    elif image.shape[2] == 4:
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2RGB)
    elif image.shape[2] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def extract_features(image):
    """Extract features from image using color histograms and edge detection"""
    # Calculate color histogram
    hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    
    # Calculate edge features using Canny
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    edge_percentage = np.count_nonzero(edges) / (edges.shape[0] * edges.shape[1])
    
    # Combine features
    features = np.append(hist, edge_percentage)
    return features

def compare_images(img1_features, img2_features):
    """Compare two images using their features"""
    return np.linalg.norm(img1_features - img2_features)

def detect_disease(image_path, dataset_path):
    """Detect disease in plant image by comparing with dataset"""
    try:
        # Read and preprocess input image
        input_image = cv2.imread(image_path)
        if input_image is None:
            return None, "Error: Could not read input image"
        
        input_image = preprocess_image(input_image)
        input_features = extract_features(input_image)
        
        best_match = None
        min_distance = float('inf')
        
        # Load disease dataset
        dataset_dir = Path(dataset_path)
        if not dataset_dir.exists():
            return None, "Error: Dataset directory not found"
            
        # Compare with each image in dataset
        for plant_dir in dataset_dir.iterdir():
            if plant_dir.is_dir():
                for disease_dir in plant_dir.iterdir():
                    if disease_dir.is_dir():
                        for img_path in disease_dir.glob('*.jpg'):
                            dataset_image = cv2.imread(str(img_path))
                            if dataset_image is not None:
                                dataset_image = preprocess_image(dataset_image)
                                dataset_features = extract_features(dataset_image)
                                
                                distance = compare_images(input_features, dataset_features)
                                if distance < min_distance:
                                    min_distance = distance
                                    best_match = {
                                        'plant': plant_dir.name,
                                        'disease': disease_dir.name
                                    }
        
        if best_match and min_distance < 0.5:  # Threshold for matching
            # Get disease information from JSON
            with open(os.path.join(os.path.dirname(__file__), 'plant_diseases.json'), 'r') as f:
                disease_data = json.load(f)
            
            if (best_match['plant'] in disease_data and 
                best_match['disease'] in disease_data[best_match['plant']]):
                disease_info = disease_data[best_match['plant']][best_match['disease']]
                return best_match, disease_info
        
        return None, "No matching disease found"
        
    except Exception as e:
        return None, f"Error during disease detection: {str(e)}"