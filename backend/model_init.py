import tensorflow as tf

#tf.keras lib
from tensorflow import keras
from keras.models import Model

#efficient lib
from efficientnet.keras import EfficientNetB3

# import time
# for i in range(10):
#     print(i)
#     time.sleep(1)

# model_ = 'model'

# 전역 변수
model_dict = {
        "detection": tf.saved_model.load('.\model\detection\saved_model'),
        "leaf_branch": tf.keras.models.load_model('./model/classification/leaf_branch.h5'),
        "tree_type": tf.keras.models.load_model('./model/classification/tree_type.h5'),
        "root": tf.keras.models.load_model('./model/classification/root.h5'),
    }
