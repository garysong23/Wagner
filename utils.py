# This is the number of beats we wish to transition, should be a multiple of 4
# Mix in and mix out points have to be set accordingly
MIX_LENGTH = 32

def transition_length(bpm):
  return (MIX_LENGTH / (bpm / 60) * 1000)
