# Temperature Monitor System

# Overview
This project is an IoT-based temperature monitor built with a Raspberry Pi, Sense HAT, Flask, and HTML.

The system reads live temperature data from the Sense HAT, processes the data using threshold-based logic, and displays the results through a web dashboard.

The project demonstrates the base layers of an IoT system:
- Data Source
- Processing
- Networking
- Application Layer

# Features
- Live temperature monitoring
- HOT / OK status detection
- Sense HAT LED message output
- Flask web dashboard
- Temperature logging to file
- Temperature statistics:
  - Average temperature
  - Maximum temperature
  - Minimum temperature

# Technologies Used
- Raspberry Pi
- Sense HAT
- Python
- Flask
- HTML

# How It Works
1. The Sense HAT collects temperature data
2. The system processes the data and determines the device status, (HOT or OK)
3. The Sense HAT displays the status
4. Temperature readings are logged in a file
5. Flask shows the data to a web dashboard
6. Stats are calculated based on temperature recordings

# Example Output
{
  "temperature": 32.5,
  "status": "HOT"
}
