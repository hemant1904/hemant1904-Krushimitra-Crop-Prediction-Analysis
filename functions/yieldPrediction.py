import json
def yieldPredict(state,Crop_Year,season,crop,area,model,mydict):
	
    mydict= json.load(open("C:\Users\heman\Crop-Prediction-Analysis\functions\yieldpred.txt"))
    state=mydict[state]
    season=mydict[season]
    crop=mydict[crop]
    prediction=model.predict([[crop]])
    return(print(prediction))

# //////////////////////uncomment below to test///////////////////////////

# state='NICOBARS'	
# crop_year=2000.0	
# season='Kharif'	
# crop='Arecanut'	
# area=1254.0	
# yieldPredict(state,crop_year,season,crop,area,model,mydict)
