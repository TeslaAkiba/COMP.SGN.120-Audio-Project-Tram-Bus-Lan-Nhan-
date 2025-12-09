import os
import numpy as np
import soundfile as sf
import librosa as lbs
import scipy 

# Normalizing the audio signals
# input_folder = "Usable Bus Sounds"
# output_folder = "Normalized Bus Sounds"
# os.makedirs(output_folder, exist_ok=True)

# for file in os.listdir(input_folder):
#     if file.endswith(".wav"):
#         path = os.path.join(input_folder, file)
#         x, sr = sf.read(path)
#         x = x.astype(np.float32)

#         # Standardization
#         mean = np.mean(x)
#         std = np.std(x)

#         if std < 1e-8:
#             x_norm = x - mean
#         else:
#             x_norm = (x - mean) / std

#         # Save normalized file
#         out_path = os.path.join(output_folder, file)
#         sf.write(out_path, x_norm, sr)


