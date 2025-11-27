#!/usr/bin/env python3
"""
MQTT to MySQL Logger
Kuuntelee MQTT-viestejä ja tallentaa ne tietokantaan.
"""
import json
import logging
from datetime import datetime
import paho.mqtt.client as mqtt
import mysql.connector
from mysql.connector import pooling
# Konfiguraatio
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "chat/messages"
DB_CONFIG = {
 "host": "localhost",
 "user": "mqtt_user",
 "password": "salasana123", # Vaihda!
 "database": "mqtt_chat"
}
# Lokitus
logging.basicConfig(
 level=logging.INFO,
 format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
# Tietokantapooli
db_pool = pooling.MySQLConnectionPool(
 pool_name="mqtt_pool",
 pool_size=5,
 **DB_CONFIG
)
def save_message(nickname, message, client_id):