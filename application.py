import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

##import ridge regressor and standard scaler
ridge_model = pickle.load(open('models/ridge_reg.pkl','rb'))
std_scaler = pickle.load(open('models/std_scaler.pkl','rb'))

application = Flask(__name__)
app = application

@app.route("/") ##when there is nothing or '/' after port in the url we call index.html
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST']) ##when we add /predictdata after the port in url we call home.html
def predict_datapoint():
    
    if request.method=='POST':
        
        Temperature=float(request.form.get('Temperature')) ## this 'Temperature' it should match with the name of the html file.
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))
        
        data_scaled = std_scaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result = ridge_model.predict(data_scaled)
        return render_template('home.html',results=result[0]) ## name 'results' needs to match with the 'results' in html file and since we get a list we need to send result[0]
        
    else: ##means it is get
        return render_template('home.html') ## inisially it will be a get request after which we will go to post
    
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)