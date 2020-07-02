# app.py
from flask import Flask, render_template, request, jsonify
from src.data_provider import get_used_car_cities, evaluate_used_car, load_saved_artifacts, get_used_car_names

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('used_car_evaluation.html')


@app.route('/api/get-cities', methods=['GET'])
def get_cities():
    response = jsonify({
        'cities': get_used_car_cities()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/api/get-car-names', methods=['GET'])
def get_car_names():
    response = jsonify({
        'car_names': get_used_car_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/api/predict-used-car-price', methods=['GET', 'POST'])
def predict_used_car_price():
    km_driven = int(request.form['km_driven'])
    reg_year = int(request.form['reg_year'])
    owner_type = int(request.form['owner_type'])
    variant_name = request.form['variant_name']
    location = request.form['location']

    est_price = evaluate_used_car(km_driven, reg_year, owner_type, variant_name, location)

    response = jsonify({
        'estimated_price': est_price
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# load data on app start so that we dont need to load and process data for each request
load_saved_artifacts()
if __name__ == "__main__":
    app.run(debug=True)
