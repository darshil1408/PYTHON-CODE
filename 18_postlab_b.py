import numpy as np
import matplotlib.pyplot as plt
fs = 500  # Sampling frequency
t = np.linspace(0, 1, fs)
freq = 5  # frequency of sinusoid
signal = np.sin(2 * np.pi * freq * t) + 0.5 * np.random.randn(fs)
autocorr = np.correlate(signal, signal, mode='full')
lags = np.arange(-len(signal) + 1, len(signal))
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(t, signal)
plt.title('Noisy Sinusoidal Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
plt.subplot(1, 2, 2)
plt.plot(lags, autocorr)
plt.title('Autocorrelation')
plt.xlabel('Lag')
plt.ylabel('Correlation')
plt.grid(True)
plt.tight_layout()
plt.show()