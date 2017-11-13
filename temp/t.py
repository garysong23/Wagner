in_bpm, out_bpm = 128, 135
mix_len = 32

incre_diff = (out_bpm - in_bpm) / 32
incre_bpm = [in_bpm + (incre_diff * i) for i in range(1,33)]

print(incre_bpm)
