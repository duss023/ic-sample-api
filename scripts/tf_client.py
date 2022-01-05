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
import time
import numpy as np
import json
import requests
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input as pi_resnet50
from tensorflow.keras.applications.xception import preprocess_input as pi_xception
from tensorflow.keras.applications.imagenet_utils import decode_predictions

def print_time(st, ed, l):
    print('time(sec): %g' % ((ed - st) / l))

if len(sys.argv) < 4: 
    print('Usage: python %s model_type server image_path' % sys.argv[0])
    exit(-1)

model_type = sys.argv[1]
url = 'https://' + sys.argv[2] + ':8501/v1/models/ic:predict'
image_path = sys.argv[3]

print('Running: %s model_type=%s url=%s image_path=%s' \
    % (sys.argv[0], model_type, url, image_path))

if model_type == "xception":
    img = image.load_img(image_path, target_size=(299,299))
    preprocess=pi_xception
else:
    img = image.load_img(image_path, target_size=(224,224))
    preprocess=pi_resnet50

x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess(x)

payload = dict(instances=x.tolist())
#json.dump(payload, open('request.json', 'w'))
payload = json.dumps(payload)

st = time.time()
r = requests.post(url, data=payload)
ed = time.time()
print_time(st, ed, 1)

pred_json = json.loads(r.content.decode('utf-8'))
#print(pred_json)
pred = decode_predictions(np.asarray(pred_json['predictions']), top=5)
cls = pred[0][0][1]
conf = pred[0][0][2]
print('Prediction cls=%s, conf=%s' % (cls, str(conf)))
