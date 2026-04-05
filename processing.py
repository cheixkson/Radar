import numpy as np

def simulate_target(signal, delay_samples):
    return np.roll(signal, delay_samples)

def mix_signals(tx, rx):
    return tx * rx

def compute_fft(signal):
    #return np.fft.fft(signal)
    return np.fft.rfft(signal)