import paho.mqtt.client as mqtt

# MQTT Broker configuration
broker = "test.mosquitto.org"
port = 1883
temperature_topic = "iot/sensor/temperature"
humidity_topic = "iot/sensor/humidity"

# Create MQTT client
client = mqtt.Client()

# Define on_connect callback
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(temperature_topic)
    client.subscribe(humidity_topic)

# Define on_message callback
def on_message(client, userdata, msg):
    if msg.topic == temperature_topic:
        print(f"Received: Temperature = {msg.payload.decode()} from topic: {msg.topic}")
    elif msg.topic == humidity_topic:
        print(f"Received: Humidity = {msg.payload.decode()} from topic: {msg.topic}")

# Configure callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(broker, port, 60)

# Maintain connection and wait for messages
client.loop_forever()
