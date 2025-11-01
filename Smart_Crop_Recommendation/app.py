from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('XGBoost.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('front_page.html')

@app.route('/english')
def english():
    return render_template('english.html')


@app.route('/english_result', methods=['POST'])
def home():
    data1 = float(request.form['N'])
    data2 = float(request.form['P'])
    data3 = float(request.form['K'])
    data4 = float(request.form['temperature'])
    data5 = float(request.form['humidity'])
    data6 = float(request.form['ph'])
    data7 = float(request.form['rainfall'])
    arr = np.array([[data1, data2, data3, data4, data5, data6, data7]])
    pred = model.predict(arr)
    return render_template('english_result.html', data=pred)


@app.route('/kannada')
def kannada():
    return render_template('kannada.html')


@app.route('/kannada_result', methods=['POST'])
def result():
    data1 = float(request.form['N'])
    data2 = float(request.form['P'])
    data3 = float(request.form['K'])
    data4 = float(request.form['temperature'])
    data5 = float(request.form['humidity'])
    data6 = float(request.form['ph'])
    data7 = float(request.form['rainfall'])
    arr = np.array([[data1, data2, data3, data4, data5, data6, data7]])
    pred = model.predict(arr)
    return render_template('kannada_result.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)
