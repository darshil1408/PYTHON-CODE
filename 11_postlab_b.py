# %%
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
img = Image.open(r"D:\ICT\SEM 3\PWP\LAB CODE\LAB 11\MU.jpg")
img_array = np.array(img)
padded_img = np.pad(img_array, ((50, 50), (50, 50), (0, 0)), mode='constant', constant_values=0)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img_array)
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(padded_img)
plt.title('Padded Image')
plt.axis('off')
plt.tight_layout()
plt.show()

