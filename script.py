import rembg
import numpy as np
from PIL import Image
import time

start_time = time.time()

input_image = Image.open('ass.jpg')

input_array = np.array(input_image)

output_array = rembg.remove(input_array)

output_image = Image.fromarray(output_array)

output_image = output_image.convert('RGB')

output_image.save('output_image.jpg')

end_time = time.time()

time_spent = end_time - start_time
print(f"Time spent: {time_spent:.2f} seconds")
