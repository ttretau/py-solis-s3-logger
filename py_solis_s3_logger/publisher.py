import os, logging
import paho.mqtt.publish as publish
from .data_fetcher import fetch_data
from .data_classes import InverterData
from timed_count import timed_count

MQTT_HOST = os.getenv("MQTT_HOST", "192.168.128.171")
PUBLISH_DELAY = os.getenv("PUBLISH_DELAY", 30.0)


def publish_mqtt(data: InverterData):
    publish.single("solar/power", data.current_power, hostname=MQTT_HOST)


def publish_loop():
    for count in timed_count(PUBLISH_DELAY):
        logging.info(count)
        publish_mqtt(fetch_data())
