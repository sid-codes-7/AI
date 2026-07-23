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
