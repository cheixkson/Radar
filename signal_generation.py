import numpy as np

def generate_chirp(fc, B, T, N):
    t = np.linspace(0, T, N)
    signal = np.cos(2 * np.pi * (fc * t + (B/(2*T)) * t**2))
    return t, signal