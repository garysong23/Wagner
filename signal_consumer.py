from kafka import KafkaConsumer
from system.AudioStream import AudioStream

audio_stream = AudioStream()
audio_stream.start_stream()

consumer = KafkaConsumer('Wagner')
for msg in consumer:
  val = msg.value.decode()
  audio_stream.on_signal_input(val)
  print('[SignalConsumer] Signal -', val)
