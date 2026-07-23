import tensorflow as tf
import kagglehub
import os

model_path = "/kaggle/input/models/wafaaelhusseini/cats-vs-dogs-classifier/tensorflow2/fine-tuned-mobilenetv2/1/"

#connect the path directly to the model
file_complete_path = os.path.join(model_path, 'cats_dogs_finetuned_FT.keras')

# load the model using standard Keras 3
model = tf.keras.models.load_model(file_complete_path)

print("Model successfully wrapped and loaded in Keras 3")
model.summary()
