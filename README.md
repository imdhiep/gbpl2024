
# **IoT Water Level Management System for Automatic Watering**

This project was developed as part of the **gPBL 2024 (Global Project-Based Learning)** initiative, organized by **Shibaura Institute of Technology (SIT)** in collaboration with **HUST**, **FPT University**, and **Phenikaa University**. The theme for this year's program is **Internet of Things (IoT)**.

Over the course of **10 days**, students participated in a variety of practical activities, ranging from discussions to hands-on projects focusing on IoT applications in sectors such as **Agriculture** and **Industry**. These activities enhanced students' **research, teamwork, presentation**, and **language skills**.

Our team's project focuses on **"Using Sensors to Manage the Water Level of an Automatic Watering System."** This system aims to **optimize water usage** by monitoring soil moisture and automatically adjusting water levels.

---

## **How to run:**

### **Step 1: Hardware Setup**

Ensure that your hardware is connected correctly as shown in the image below (image of your hardware setup should be inserted here).

### **Step 2: Software Setup**

For the **Raspberry Pi (Python)**:
```bash
python3 main.py
```

For the **ESP8266 (Arduino IDE)**: Upload `v3.ino` to the ESP8266 using the Arduino IDE.

### **Step 3: View Output**

The system will monitor soil moisture and display data on the **LCD**. You can also monitor data remotely using the **ESP8266 module**.

---

## **List of Devices Needed**

- **Soil Moisture Sensor**: Measures the moisture level of the soil.
- **Humidity and Temperature Sensor**: Monitors humidity and temperature levels.
- **LCD Display**: Displays real-time soil moisture values.
- **Raspberry Pi Pico 2**: Controls the sensors and the overall system.
- **ESP8266 Module**: Enables wireless communication for remote monitoring.

---

## **Installation Guide**

### 1. **Adafruit_DHT Library**:

**Purpose**: This Python library is used for interfacing with DHT sensors (e.g., DHT11, DHT22) to read temperature and humidity data.

**Installation**:
```bash
pip install Adafruit_DHT
```

### 2. **RPi.GPIO Library**:

**Purpose**: `RPi.GPIO` is a library that enables you to control the GPIO (General Purpose Input/Output) pins on the Raspberry Pi. These pins allow your Pi to interface with external hardware like LEDs, buttons, motors, and more.

**Installation**:
```bash
pip install RPi.GPIO
```

### 3. **smbus2 Library**:

**Purpose**: This library allows your Raspberry Pi to communicate with I2C devices (like sensors and displays) via the SMBus (System Management Bus) protocol. It’s commonly used to read data from external sensors or control I2C modules such as an LCD.

**Installation**:
```bash
pip install smbus2
```

### 4. **RPLCD Library**:

**Purpose**: `RPLCD` is a Python library for controlling LCD displays. It supports both direct GPIO connections and I2C connections. This library helps you easily send text or data to an LCD screen connected to your Raspberry Pi.

**Installation**:
```bash
pip install RPLCD
```

### 5. **ESP8266 Board Package (for Arduino IDE)**:

**Purpose**: To program and upload code to the ESP8266, you need to install the ESP8266 board package in the Arduino IDE.

**Installation Steps**:

1. In Arduino IDE, go to **File > Preferences**.
2. In the **Additional Boards Manager URLs** field, add the following URL:
```bash
http://arduino.esp8266.com/stable/package_esp8266com_index.json
```
3. Go to **Tools > Board > Boards Manager**, search for **ESP8266**, and click **Install**.
4. After installation, go to **Tools > Board** and select **Generic ESP8266 Module**.

**Required Libraries**:
- The code uses two libraries: `ESP8266WiFi.h` and `WiFiClient.h`. These libraries are bundled with the ESP8266 board package, so no additional installation is required.

### **6. Verify Port Selection:**

Make sure the correct port is selected by going to **Tools > Port** and choosing the port to which your ESP8266 is connected.

---
**Demo Video**:


https://github.com/user-attachments/assets/ea052261-6f07-445e-86cd-aaba6d0418da




## **License**

[MIT](https://choosealicense.com/licenses/mit/)
