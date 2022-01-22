
import tensorflow as tf  
import tflearn
import json
from tensorflow.python.framework import ops
import numpy as np
import nltk
import random
from nltk.stem.lancaster import LancasterStemmer

global stemmer,model,data
stemmer= LancasterStemmer()

def train():
  ops.reset_default_graph()
  words=[]
  docx=[]
  docy=[]
  labels=[]
  f=open('intents.json')
  data=json.load(f)
  for intent in data['intents']:
      for pattern in intent["patterns"]:
          wrds= nltk.word_tokenize(pattern)
          words.extend(wrds)
          docx.append(wrds)
          docy.append(intent['tag'])
      
      if intent["tag"] not in labels:
          labels.append(intent['tag'])
  words = [stemmer.stem(w.lower()) for w in words if w not in "?" ]
  words= sorted(list(set(words)))

  labels=sorted(labels)
  training=[]
  output=[]

  out_empty=[0 for _ in range(len(labels))]

  for x, doc in enumerate(docx):
      bag=[]
      wrds=[stemmer.stem(w) for w in doc]
      for w in words:
          if w in wrds:
              bag.append(1)
          else:
              bag.append(0)
      output_row=out_empty[:]
      output_row[labels.index(docy[x])]=1

      training.append(bag)
      output.append(output_row)

  training=np.array(training)
  output= np.array(output)

  net = tflearn.input_data(shape=[None, len(training[0])])
  net = tflearn.fully_connected(net, 8)
  net = tflearn.fully_connected(net, 8)
  net = tflearn.fully_connected(net, len(output[0]), activation='softmax')
  net = tflearn.regression(net)
  model = tflearn.DNN(net)
  model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
  model.save('model.tflearn')

def bag_of_words(s,words):
    bag=[0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words=[stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i,w in enumerate(words):
            if w==se:
                bag[i]=1
    return np.array(bag)

def chat(inp): 
  results = model.predict([bag_of_words(inp, words)])[0]
  results_index = np.argmax(results)
  tag = labels[results_index]
  if results[results_index]>0.6:
    for tg in data ["intents"]:
      if tg ['tag'] == tag: 
        responses = tg['responses']
    return random.choice(responses)
