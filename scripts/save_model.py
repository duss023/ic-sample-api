#
# Copyright 2022 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

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

tf.keras.models.save_model(model, 'ic/1')
