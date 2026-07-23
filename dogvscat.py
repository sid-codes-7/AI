import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from PIL import Image, UnidentifiedImageError


# ============================================================
# 1. PATHS
# ============================================================

# Folder containing the three saved Cats vs Dogs models
MODEL_DIRECTORY = (
    "/kaggle/input/models/"
    "wafaaelhusseini/cats-vs-dogs-classifier/"
    "tensorflow2/fine-tuned-mobilenetv2/1"
)

# Search all Kaggle datasets for the individual cat and dog images
IMAGE_DIRECTORY = "/kaggle/input/datasets"

# ============================================================
# 2. FIND THE SAVED MODEL
# ============================================================

model_paths = []

#get the complete location of that file and save it into model_paths
for root, folders, files in os.walk(MODEL_DIRECTORY):
    for filename in files:
        if filename.lower().endswith((".keras", ".h5")):
            full_path = os.path.join(root, filename)
            model_paths.append(full_path)
