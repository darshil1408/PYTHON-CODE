# %%
import numpy as np
import matplotlib.pyplot as plt
fs = 500  
f = 5  
t = np.linspace(0, 1, fs, endpoint=False)  
sine_wave = np.sin(2 * np.pi * f * t)
time_shift = 0.1 
shifted_t = t + time_shift
shifted_sine_wave = np.sin(2 * np.pi * f * shifted_t)
plt.figure(figsize=(10, 5))
plt.plot(t, sine_wave, label='Original Sine Wave (5 Hz)')
plt.plot(t, shifted_sine_wave, label='Shifted Sine Wave (5 Hz, +0.1s)', linestyle='--')
plt.title('Original and Time-Shifted Sine Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
