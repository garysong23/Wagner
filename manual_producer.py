import time
import cv2
from kafka import SimpleProducer, KafkaClient

kafka = KafkaClient('localhost:9092')
producer = SimpleProducer(kafka)

while True:
  print('[SignalProducer] - Waiting for user input')
  msg = input()
  producer.send_messages('Wagner', msg.encode())
  print('[SignalProducer] - Sent:', msg)
