from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Placeholder functions that will be implemented later for Pi integration
def get_soil_moisture():
    # This will be implemented to read from the Pi's sensors
    return 75  # Placeholder value

def toggle_lights():
    # This will be implemented to control the Pi's GPIO pins
    return {"status": "success", "message": "Lights toggled"}

def water_plant():
    # This will be implemented to control the Pi's water pump
    return {"status": "success", "message": "Watering plant"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/soil-moisture')
def soil_moisture():
    moisture = get_soil_moisture()
    return jsonify({"moisture": moisture})

@app.route('/api/toggle-lights')
def api_toggle_lights():
    result = toggle_lights()
    return jsonify(result)

@app.route('/api/water-plant')
def api_water_plant():
    result = water_plant()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001) 