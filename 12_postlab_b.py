# %%
import numpy as np
import matplotlib.pyplot as plt
fs = 500  
t = np.linspace(0, 2, fs*2, endpoint=False)  
f1 = 5  
f2 = 10 
sine_wave = np.sin(2 * np.pi * f1 * t)
cosine_wave = np.cos(2 * np.pi * f2 * t)
resulting_signal = sine_wave * cosine_wave
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(t, sine_wave)
plt.title('Sine Wave (5 Hz)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.subplot(3, 1, 2)
plt.plot(t, cosine_wave)
plt.title('Cosine Wave (10 Hz)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.subplot(3, 1, 3)
plt.plot(t, resulting_signal)
plt.title('Resulting Signal (Sine * Cosine)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()

