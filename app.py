from flask import Flask, render_template, jsonify
import RPi.GPIO as gpio
import src.pump
from time import sleep
from src.plantData import plantData
# PUMP_PIN = 18
app = Flask(__name__)
# GPIO Setup
# PUMP_PIN = 17  # GPIO pin for water pump
# LIGHT_PIN = 18  # GPIO pin for lights

# Initialize GPIO

# Initialize plant data reader
plant = plantData()
pump = src.pump.pump()


def get_soil_moisture():
    try:
        return int(plant.getData()[1])
    except Exception as e:
        print(f"Error reading moisture: {e}")
        return 2000  # Return default value if error

def get_light_level():
    try:
        return int(plant.getData()[0])
    except Exception as e:
        print(f"Error reading light: {e}")
        return 0  # Return default value if error

def toggle_lights():
    global light_state
    try:
        light_state = not light_state
        #GPIO.output(LIGHT_PIN, light_state)
        return {"status": "success", "message": f"Lights {'on' if light_state else 'off'}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def water_plant():
    try:
        # Activate pump for 3 second
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
    try:
        light = get_light_level()
        if light == 0:
            return jsonify({"light": "ON"})
        elif light == 1:
            return jsonify({"light": "OFF"})
    except Exception as e:
        print(f"Error in light_level endpoint: {e}")
        return jsonify({"light": "ERROR", "message": str(e)})

@app.route('/api/toggle-lights')
def api_toggle_lights():
    result = toggle_lights()
    return jsonify(result)

@app.route('/api/water-plant')
def api_water_plant():
    pump.water()
    result = water_plant()
    return jsonify(result)

def cleanup():
    if hasattr(app, 'plant'):
        app.plant.close()
        gpio.cleanup()

if __name__ == '__main__':
    try:
        # gpio.setmode(gpio.BCM)
        # gpio.setup(PUMP_PIN, gpio.OUT)
        # gpio.output(PUMP_PIN, gpio.LOW)
        app.run(debug=True, host='0.0.0.0', port=8080, use_reloader=False)
    finally:
        cleanup() 