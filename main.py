from signal_generation import generate_chirp
from processing import simulate_target, mix_signals, compute_fft
import matplotlib.pyplot as plt
import numpy as np

# paramètres
fc = 77e9
B = 200e6
T = 1e-3
N = 1024

# génération
t, tx = generate_chirp(fc, B, T, N)

# cible
delay_samples = 50
rx = simulate_target(tx, delay_samples)

# mix
mix = mix_signals(tx, rx)

# FFT
fft = compute_fft(mix)

# affichage
plt.plot(np.abs(fft))
plt.title("FFT - détection distance")
plt.show()