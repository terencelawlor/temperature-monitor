from sense_hat import SenseHat
import time
from flask import Flask, render_template, jsonify

sense = SenseHat()
sense.clear()

GREEN = (0, 255, 0)
RED = (255, 0, 0)

app = Flask(__name__)

temperature_history = []

@app.route("/")

def home():

    temp = read_temperature()

    temperature_history.append(temp)

    status = display_status(temp)

    celsius = round(temp, 2)

    fahrenheit = round(1.8 * celsius + 32, 2)

    average_temp = round(sum(temperature_history) / len(temperature_history), 2)

    max_temp = round(max(temperature_history), 2)

    min_temp = round(min(temperature_history), 2)

    return render_template(
        "status.html",
        celsius=celsius,
        fahrenheit=fahrenheit,
        status=status,
        average_temp=average_temp,
        max_temp=max_temp,
        min_temp=min_temp
    )

@app.route("/data")
def data():
    temp = read_temperature()
    status = display_status(temp)
    log_data(temp, status)
    msg = {"temperature": temp, "status": status}
    return jsonify(msg)

# Read temperature
def read_temperature():
    return sense.get_temperature()

# Display status
def display_status(temp):
    if temp >= 25:
        print(f"Temperature: {temp}°C - HOT")
        sense.show_message("HOT!", text_colour=RED)
        return "HOT"
    else:
        print(f"Temperature: {temp}°C - OK")
        sense.show_message("OK", text_colour=GREEN)
        return "OK"

# Log data in log.txt
def log_data(temp, status):
    with open("log.txt", "a") as file:
        file.write(f"Temperature: {temp},{status}\n")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
