# %%
import numpy as np
import matplotlib.pyplot as plt
fs = 500  
f = 10  
t = np.linspace(0, 1, fs, endpoint=False)  
sine_wave = np.sin(2 * np.pi * f * t)
scaled_sine_wave = 3 * sine_wave
plt.figure(figsize=(10, 5))
plt.plot(t, sine_wave, label='Original Sine Wave (10 Hz)')
plt.plot(t, scaled_sine_wave, label='Scaled Sine Wave (10 Hz, x3)', linestyle='--')
plt.title('Original and Scaled Sine Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
