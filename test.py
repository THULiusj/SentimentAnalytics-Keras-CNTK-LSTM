from __future__ import print_function
import pickle
import sys
import cntk
cntk.try_set_default_device(cntk.device.gpu(0))

from keras.preprocessing import sequence, text
from keras.models import Model, Sequential, load_model
from keras.preprocessing.text import Tokenizer
import os
from os.path import isfile, join



max_len = 100

# Load model and tokenizer
with open('Model/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

model = load_model("Model/bidir.hdf5")

testorigin = sys.argv[1]
test = tokenizer.texts_to_sequences([testorigin])
test = sequence.pad_sequences(test, maxlen=max_len)
print('Text: ', testorigin)
print('Result: ', model.predict(test))