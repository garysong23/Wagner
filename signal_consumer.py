from kafka import KafkaConsumer
from system.AudioController import AudioController

audio_controller = AudioController()
audio_controller.start_stream()

consumer = KafkaConsumer('Wagner')
for msg in consumer:
  val = msg.value.decode()
  audio_controller.on_signal_input(val)
