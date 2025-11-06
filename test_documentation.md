# Test Documentation for Crop Prediction Analysis

This document outlines the test cases for the various prediction models in the Crop Prediction Analysis system.

## 1. Crop Recommendation Model

### Input Parameters
- N (Nitrogen): 0-100 (mg/kg)
- P (Phosphorus): 0-100 (mg/kg)
- K (Potassium): 0-100 (mg/kg)
- Temperature: 0-50 (°C)
- Humidity: 0-100 (%)
- pH: 0-14
- Rainfall: 0-300 (mm)

### Test Cases

#### 1.1 Normal Case - Rice Cultivation
- Input:
  - N: 90
  - P: 42
  - K: 43
  - Temperature: 20.88
  - Humidity: 82.00
  - pH: 6.50
  - Rainfall: 202.94
- Expected Output: "rice"
- Validation: Check if prediction matches expected crop based on optimal conditions

#### 1.2 Boundary Cases
- Test minimum values (N=0, P=0, K=0)
- Test maximum values (N=100, P=100, K=100)
- Test extreme temperature conditions (0°C and 50°C)
- Test pH boundary values (0 and 14)

#### 1.3 Error Cases
- Negative values for any parameter
- Values exceeding maximum limits
- Missing parameters
- Non-numeric inputs

## 2. Yield Prediction Model

### Input Parameters
- State: String (e.g., 'NICOBARS')
- Crop Year: Integer (e.g., 2000)
- Season: String ('Kharif', 'Rabi')
- Crop: String (e.g., 'Arecanut')
- Area: Float (hectares)

### Test Cases

#### 2.1 Normal Case - Arecanut Yield
- Input:
  - State: 'NICOBARS'
  - Crop Year: 2000
  - Season: 'Kharif'
  - Crop: 'Arecanut'
  - Area: 1254.0
- Expected Output: Yield prediction in kg/hectare
- Validation: Compare with historical yield data

#### 2.2 Data Validation Cases
- Invalid state names
- Future crop years
- Invalid season names
- Unrecognized crop names
- Zero or negative area values

#### 2.3 Edge Cases
- Very large area values
- Historical crop years (e.g., before 1950)
- Uncommon crop-season combinations

## 3. Model Accuracy Metrics

### Crop Recommendation Model
- Training accuracy: ~95%
- Test accuracy: ~93%
- Key metrics to monitor:
  - Precision
  - Recall
  - F1 Score

### Yield Prediction Model
- Accuracy: 95.6%
- Mean Absolute Error (MAE)
- Root Mean Square Error (RMSE)
- R-squared value

## 4. Integration Test Cases

### 4.1 API Endpoint Testing
- Test all endpoints return correct HTTP status codes
- Verify response format and structure
- Check error handling and messages

### 4.2 Data Flow Testing
- Verify data preprocessing
- Check model input validation
- Test result formatting and display

## 5. Performance Test Cases

### 5.1 Response Time
- Single prediction request: < 1 second
- Multiple concurrent requests: < 2 seconds
- Batch processing: Scale with data size

### 5.2 Load Testing
- Normal load: 100 requests/minute
- Peak load: 500 requests/minute
- Stress test: 1000 requests/minute

## 6. Security Test Cases

### 6.1 Input Validation
- SQL injection prevention
- Cross-site scripting (XSS) prevention
- Input sanitization

### 6.2 Authentication
- API key validation
- Rate limiting
- Access control

## 7. Maintenance and Monitoring

### 7.1 Model Retraining
- Periodic model evaluation
- Performance degradation monitoring
- Data drift detection

### 7.2 Error Logging
- Log all prediction errors
- Track unusual predictions
- Monitor system resources