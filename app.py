# 2.2. Import necessary libraries, initialize the flask app, and load our ML model
# import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Initialize the flask App
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

# 2.3. Define the app route for the default page of the web-app
# default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')
# 2.4. Redirecting the API to predict the CO2 emission
# To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Khí thải CO2 của xe là :{}'.format(output))
# 2.5. Starting the Flask Server
if __name__ == "__main__":
    app.run(debug=True)