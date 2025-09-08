# %%
import numpy as np
import matplotlib.pyplot as plt
fs = 500
f = 5
t = np.linspace(0, 1, fs, endpoint=False)
sine_wave = np.sin(2 * np.pi * f * t)
reversed_sine_wave = sine_wave[::-1]
plt.figure(figsize=(10, 5))
plt.plot(t, sine_wave, label='Original Sine Wave (5 Hz)')
plt.plot(t, reversed_sine_wave, label='Reversed Sine Wave (5 Hz)', linestyle='--')
plt.title('Original and Reversed Sine Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
