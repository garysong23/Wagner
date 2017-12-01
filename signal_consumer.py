from kafka import KafkaConsumer
from system.AudioController import AudioController

audio_controller = AudioController()

consumer = KafkaConsumer('Wagner')
for msg in consumer:
  val = msg.value.decode()
  audio_controller.on_signal_input(val)
