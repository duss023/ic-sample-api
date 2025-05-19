import sys
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.applications.xception import Xception

if len(sys.argv) < 2:
    print('Usage: python %s model_type' % sys.argv[0])
    exit(-1)
    
model_type = sys.argv[1]
print('Running: %s model_type=%s' % (sys.argv[0], model_type))

if model_type == "xception":
    model = Xception(weights='imagenet')
else:
    model = ResNet50(weights='imagenet')

model.export('ic/1')
