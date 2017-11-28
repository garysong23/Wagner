import librosa.display
import matplotlib.pyplot as plt

def chroma_comparison(t1, t2, c1, c2):
  ax1 = plt.subplot(2,1,1)
  im = librosa.display.specshow(c1, x_axis='time', y_axis='chroma')
  plt.title(t1)

  ax2 = plt.subplot(2,1,2, sharex=ax1)
  im2 = librosa.display.specshow(c2, x_axis='time', y_axis='chroma')
  plt.title(t2)

  plt.tight_layout()
  plt.show()
