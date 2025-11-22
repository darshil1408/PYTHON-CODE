# %%
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
img = Image.open(r'D:\ICT\SEM 3\PWP\LAB CODE\LAB 11\MU.jpg')
img = np.array(img)
print(img.shape)
red_channel = img[:, :, 0]
plt.imshow(red_channel, cmap='Reds')
plt.title('Red Channel')
plt.axis('off')
plt.show()
green_channel = img[:, :, 1]
plt.imshow(green_channel, cmap='Greens')
plt.title('Green Channel')
plt.axis('off')
plt.show()
blue_channel = img[:, :, 2]
plt.imshow(blue_channel, cmap='Blues')
plt.title('Blue Channel')
plt.axis('off')
plt.show()

