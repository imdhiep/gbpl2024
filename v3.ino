#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <WiFiClient.h>

const uint16_t port = 8585;
const char *host = "192.168.137.37";
const int analogInPin = A0;  // ESP8266 Analog Pin ADC0 = A0

WiFiClient client;

void setup()
{
    Serial.begin(115200);
    Serial.println("Connecting...\n");

    WiFi.mode(WIFI_STA);
    WiFi.begin("NAKAMURA", "98}7g86O"); // change it to your SSID and password

    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }

    Serial.println("Connected to WiFi");
}

void loop()
{
    // Read the analog input value
    int sensorValue = analogRead(analogInPin);

    if (!client.connect(host, port))
    {
        Serial.println("Connection to host failed");
        delay(1000);
        return;
    }

    Serial.println("Connected to server successfully!");

    // Send sensor value to the server
    client.println(sensorValue);

    Serial.println();  // Print a newline for better readability
    client.stop();
    delay(5000);  // Delay before the next iteration
}
