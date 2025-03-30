from flask import Flask, render_template, jsonify
import RPi.GPIO as GPIO
import time
from src.plantData import plantData

app = Flask(__name__)

# GPIO Setup
PUMP_PIN = 17  # GPIO pin for water pump
LIGHT_PIN = 18  # GPIO pin for lights

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(PUMP_PIN, GPIO.OUT)
GPIO.setup(LIGHT_PIN, GPIO.OUT)

# Initialize plant data reader
plant = plantData()

# Track light state
light_state = False

def get_soil_moisture():
    try:
        return plant.readMoisture()
    except Exception as e:
        print(f"Error reading moisture: {e}")
        return 1000  # Return default value if error

def get_light_level():
    try:
        return int(plant.readLight())
    except Exception as e:
        print(f"Error reading light: {e}")
        return 0  # Return default value if error

def toggle_lights():
    global light_state
    try:
        light_state = not light_state
        GPIO.output(LIGHT_PIN, light_state)
        return {"status": "success", "message": f"Lights {'on' if light_state else 'off'}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def water_plant():
    try:
        # Activate pump for 1 second
        GPIO.output(PUMP_PIN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(PUMP_PIN, GPIO.LOW)
        return {"status": "success", "message": "Watering complete"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/soil-moisture')
def soil_moisture():
    moisture = get_soil_moisture()
    return jsonify({"moisture": moisture})

@app.route('/api/light-level')
def light_level():
    light = get_light_level()
    return jsonify({"light": light})

@app.route('/api/toggle-lights')
def api_toggle_lights():
    result = toggle_lights()
    return jsonify(result)

@app.route('/api/water-plant')
def api_water_plant():
    result = water_plant()
    return jsonify(result)

def cleanup():
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        app.run(debug=True, host='0.0.0.0', port=8080, use_reloader=False)
    finally:
        cleanup() 