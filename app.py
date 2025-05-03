from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('hvac.pickle', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the form
        data = request.json
        generator_duty = float(data['generatorDuty'])
        pump_pressure = float(data['pumpPressure'])
        mass_flow_rate = float(data['massFlowRate'])
        chiller_in_temp = float(data['chillerInTemp'])

        # Prepare input for the model (using 3 features)
        input_data = np.array([[generator_duty, pump_pressure, mass_flow_rate]])

        # Make prediction
        prediction = model.predict(input_data)[0]

        # Check prediction format
        if not isinstance(prediction, (list, np.ndarray)) or len(prediction) != 4:
            raise ValueError("Model prediction must be a list or array with 4 elements")

        # Extract prediction values
        predicted_output_temp = float(prediction[0])
        evaporator_duty = float(prediction[1])
        generator_output = float(prediction[2])
        cop = float(prediction[3])

        # Calculate chiller output temperature
        # Assuming the model predicts the temperature drop, adjust chiller_in_temp
        output_temp = chiller_in_temp - predicted_output_temp

        # Prepare result
        result = {
            'outputTemp': round(output_temp, 2),
            'evaporatorDuty': round(evaporator_duty, 2),
            'generatorOutput': round(generator_output, 2),
            'cop': round(cop, 2)
        }

        return jsonify({'status': 'success', 'result': result})

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)