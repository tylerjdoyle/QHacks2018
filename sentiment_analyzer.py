import string
from random import shuffle

from nltk.tokenize import TweetTokenizer

from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from gensim.models import KeyedVectors

import numpy

fname = 'GoogleNews-vectors-negative300.bin' # Pre-trained word vectors. Available for download at https://code.google.com/archive/p/word2vec/.
w2v = KeyedVectors.load_word2vec_format(fname, binary=True)

"""weights = w2v.wv.syn0
vocab_size, emdedding_size = weights.shape"""

train = []
test = []

tokenizer = TweetTokenizer()

for l, label in enumerate(['negative', 'positive']):

    with open('imdb/train/{}.txt'.format(label), 'r') as file:
    
        for line in file:
            
            tokens = tokenizer.tokenize(line)
            
            sequence = []
            for token in tokens:
                
                try:
                    sequence.append(w2v[token])
                except KeyError:
                    #print('KeyError in train load.')
                    pass
            
            if len(sequence) > 0:
                sequence = numpy.array(sequence)
                print(numpy.shape(sequence))
                train.append((sequence, l))
                print(numpy.shape(train))

#train = shuffle(train)

x_train = []
y_train = []
for x, y in train:
    x_train.append(x)
    y_train.append(y)
x_train = numpy.array(x_train)
y_train = numpy.array(y_train)

for l, label in enumerate(['negative', 'positive']):

    with open('imdb/test/{}.txt'.format(label), 'r') as file:
        
        for line in file:

            tokens = tokenizer.tokenize(line)
            
            sequence = []
            for token in tokens:
                try:
                    sequence.append(w2v[token])
                except KeyError:
                    #print('KeyError in test load.')
                    pass
                   
            if len(sequence) > 0:
                sequence = numpy.array(sequence)
                print(numpy.shape(sequence))
                test.append((sequence, l))

#test = shuffle(test)

x_test = []
y_test = []
for x, y in train:
    x_test.append(x)
    y_test.append(y)
x_test = numpy.array(x_train)
y_test = numpy.array(y_train)

print(numpy.shape(train))
print(train[0])

model = Sequential()
model.add(LSTM(input_shape=(None, 300), units=50, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=100, return_sequences=False))
model.add(Dropout(0.2))
model.add(Dense(units=1))
model.add(Activation('linear'))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

model.fit(x=x_train, y=y_train, epochs=5, validation_split=0.05)
model.evaluate(x=x_test, y=y_test)
model.save('sentiment.w2v')