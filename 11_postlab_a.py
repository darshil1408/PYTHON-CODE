# %%
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
img = Image.open(r'D:\ICT\SEM 3\PWP\LAB CODE\LAB 11\MU.jpg')
img = np.array(img)
print(img.shape)
plt.imshow(img)
plt.title('Image')
plt.axis('off')
plt.show()
print("Dimensions of the image:", img.ndim)
print("Shape of the image:", img.shape)
print("Minimum pixel value at channel B:", np.min(img[:, :, 2]))