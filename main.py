import Adafruit_DHT
import smtplib
from email.mime.text import MIMEText
import time
import RPi.GPIO as GPIO
from smbus2 import SMBus
from RPLCD.i2c import CharLCD
import socket

# Sensor type and GPIO pin configuration
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  # GPIO pin for the temperature and humidity sensor
SOIL_MOISTURE_PIN = 17  # GPIO pin for the soil moisture sensor
LED_PIN = 18  # GPIO pin for the LED

# Email configuration
smtp_host = 'smtp.gmail.com'
smtp_port = 587
username = 'af21080@shibaura-it.ac.jp'
password = 'flyn zaeu newn xvlm'
from_addr = 'af21080@shibaura-it.ac.jp'
to_addr = 'ma23100@shibaura-it.ac.jp'

# Threshold settings
TEMP_THRESHOLD = 30.0  # Trigger when temperature exceeds 30°C
HUMIDITY_THRESHOLD = 70.0  # Trigger when humidity exceeds 70%
SOIL_MOISTURE_THRESHOLD = 0  # Soil moisture sensor threshold (0 is dry, 1 is wet)

# Measurement interval
MEASUREMENT_INTERVAL = 3  # Measure every 3 seconds

# LCD configuration
lcd = CharLCD(i2c_expander='PCF8574', address=0x3F, port=1, cols=16, rows=2, backlight_enabled=True)

# Socket configuration
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 8585))
s.listen(0)

def send_alert(temp, humidity, soil_moisture):
    """Function to send an alert for temperature, humidity, and soil moisture levels"""
    subject = 'Alert: Temperature, Humidity, and Soil Moisture'
    body = f'Alert: Temperature is {temp}C, Humidity is {humidity}%, Soil Moisture is {"Wet" if soil_moisture == 1 else "Dry"}'
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr

    try:
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()
            server.login(username, password)
            server.sendmail(from_addr, to_addr, msg.as_string())
            print("Email has been sent!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def read_sensors():
    """Function to read temperature, humidity, and soil moisture sensor values"""
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    soil_moisture = GPIO.input(SOIL_MOISTURE_PIN)
    return temperature, humidity, soil_moisture

# GPIO configuration
GPIO.setmode(GPIO.BCM)
GPIO.setup(SOIL_MOISTURE_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)  # Set LED GPIO pin as output

# Socket connection handling loop
while True:
    client, addr = s.accept()
    client.settimeout(3)
    content = client.recv(1024)
    if len(content) == 0:
        break
    if str(content, 'utf-8') == '\r\n':
        continue
    else:
        print(str(content, 'utf-8'))
        #client.send(b'Hello From Python')

# Main monitoring loop
while True:
    temperature, humidity, soil_moisture = read_sensors()

    if temperature is not None and humidity is not None:
        print(f"Temp={temperature}C Humidity={humidity}% Soil Moisture={'Wet' if soil_moisture == 1 else 'Dry'}")

        # Check if temperature, humidity, or soil moisture exceed the thresholds
        if (temperature > TEMP_THRESHOLD) or (humidity > HUMIDITY_THRESHOLD) or (soil_moisture == SOIL_MOISTURE_THRESHOLD):
            send_alert(temperature, humidity, soil_moisture)
            GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on the LED
        else:
            GPIO.output(LED_PIN, GPIO.LOW)  # Turn off the LED

    time.sleep(MEASUREMENT_INTERVAL)

# Clear the LCD display
lcd.clear()

# Close the LCD bus
lcd.close()
