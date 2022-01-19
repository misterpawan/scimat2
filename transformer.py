
import pandas as pd
import re
import os
import time
# import random
import numpy as np
from collections import namedtuple
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from sklearn.model_selection import train_test_split
#from google.colab import drive
import pickle
import spacy
#nlp = spacy.load("en_core_web_sm")
#from nltk.translate.bleu_score import corpus_bleu

print("Libraries Loaded\n",flush = True)

"""Now Add the preprocessed Inputs of postfix notations from our dataset here.

Reasons for going with postfix :

Generalized Notation for Various fields of Maths like Algebra Calculus Trigonometry etc.
"""

# Creating the dataframe from Scratch
questions = []
answers = []


# Path for file containing questions
with open('./questions.txt') as f1:
	for line in f1:
		line = re.sub(r"\n",r"",line)
		questions.append(line)


# Path for file containing answers
with open('./answers.txt') as f2:
	for line in f2:
		line = re.sub(r"\n",r"",line)
		answers.append(line)

#questions = questions[:100000]
#answers = answers[:100000]

print("Dataset Loaded\n",flush = True)

Item = namedtuple('Item', 'question answer')

division = 50
sz = len(questions)
start = 0
ques = []
ans = []
while start < sz:
	end = int(min(sz, start + sz // division))
	ques.append(questions[start:end])
	ans.append(answers[start:end])
	start = end

df_2d = []
division = len(ques)
for qno in range(len(ques)):
	q = ques[qno]
	an = ans[qno]
	items = []
	for i in range(len(q)):
		question = q[i]
		answer = an[i]
		if(len(question)>2):
				items.append(Item(question, answer))

	df = pd.DataFrame.from_records(items, columns=['Question', 'Answer'])
	df_2d.append(df)


"""### Creating the dataset of word problems

*Please add the correct path to load the data file*
"""

input_exps_2d = []
for df in df_2d:
  input_exps = list(df['Question'].values)
  input_exps_2d.append(input_exps)

target_exps_2d = []
for df in df_2d:
  target_exps = list(df['Answer'].values)
  target_exps_2d.append(target_exps)


"""### Preprocessing and Tokenizing the Input and Target exps"""

def preprocess_input(sentence):
  '''
  For the word problem, convert everything to lowercase, add spaces around all
  punctuations and digits, and remove any extra spaces. 
  '''
  sentence = sentence.lower().strip()
  sentence = re.sub(r"([?.!,’,(,)])", r" \1 ", sentence)
  sentence = re.sub(r"([0-9])", r" \1 ", sentence)
  sentence = re.sub(r'[" "]+', " ", sentence)
  sentence = sentence.rstrip().strip()
  return sentence

def preprocess_target(sentence):
  '''
  For the equation, convert it to lowercase and remove extra spaces
  '''
  sentence = sentence.lower().strip()
  sentence = re.sub(r"([?.!,’,-,(,)])", r" \1 ", sentence)
  sentence = re.sub(r"([0-9])", r" \1 ", sentence)
  sentence = re.sub(r'[" "]+', " ", sentence)
  return sentence

preprocessed_input_exps_2d = []
preprocessed_target_exps_2d = []
for i in range(division):
  input_exps = input_exps_2d[i]
  target_exps = target_exps_2d[i]
  preprocessed_input_exps = list(map(preprocess_input, input_exps))
  preprocessed_target_exps = list(map(preprocess_target, target_exps))
  preprocessed_input_exps_2d.append(preprocessed_input_exps)
  preprocessed_target_exps_2d.append(preprocessed_target_exps)


def tokenize(lang):
  '''
  Tokenize the given list of strings and return the tokenized output
  along with the fitted tokenizer.
  '''
  lang_tokenizer = tf.keras.preprocessing.text.Tokenizer(filters='')
  lang_tokenizer.fit_on_texts(lang)
  tensor = lang_tokenizer.texts_to_sequences(lang)
  return tensor, lang_tokenizer

input_tensor_2d = []
inp_lang_tokenizer_2d = []
for i in range(division):
  input_tensor, inp_lang_tokenizer = tokenize(preprocessed_input_exps)
  input_tensor_2d.append(input_tensor)
  inp_lang_tokenizer_2d.append(inp_lang_tokenizer)

target_tensor_2d = []
targ_lang_tokenizer_2d = []
for i in range(division):
  target_tensor, targ_lang_tokenizer = tokenize(preprocessed_target_exps)
  target_tensor_2d.append(target_tensor)
  targ_lang_tokenizer_2d.append(targ_lang_tokenizer)

old_len = len(targ_lang_tokenizer_2d[0].word_index)

# target_tensor,targ_lang_tokenizer = input_tensor, inp_lang_tokenizer

def append_start_end(x,last_int):
  '''
  Add integers for start and end tokens for input/target exps
  '''
  l = []
  l.append(last_int+1)
  l.extend(x)
  l.append(last_int+2)
  return l

input_tensor_list_2d = []
target_tensor_list_2d = []
for j in range(division):
  input_tensor_list = [append_start_end(i,len(inp_lang_tokenizer.word_index)) for i in input_tensor_2d[j]]
  target_tensor_list = [append_start_end(i,len(targ_lang_tokenizer.word_index)) for i in target_tensor_2d[j]]
  input_tensor_list_2d.append(input_tensor_list)
  target_tensor_list_2d.append(target_tensor_list)

# Pad all sequences such that they are of equal length
input_tensor_2d = []
target_tensor_2d = []
for i in range(division):
  input_tensor_list = input_tensor_list_2d[i]
  target_tensor_list = target_tensor_list_2d[i]
  input_tensor = tf.keras.preprocessing.sequence.pad_sequences(input_tensor_list, padding='post')
  target_tensor = tf.keras.preprocessing.sequence.pad_sequences(target_tensor_list, padding='post')
  input_tensor_2d.append(input_tensor)
  target_tensor_2d.append(target_tensor)


# Here we are increasing the vocabulary size of the target, by adding a
# few extra vocabulary words (which will not actually be used) as otherwise the
# # small vocab size causes issues downstream in the network.
keys = [str(i) for i in range(10,51)]
for i,k in enumerate(keys):
  for j in range(division):
    targ_lang_tokenizer_2d[j].word_index[k]=len(targ_lang_tokenizer.word_index)+i+4

#len(targ_lang_tokenizer_2d[0].word_index)

"""### Create a tf.data dataset"""

test_data = []
test_targ = []
input_tensor_train_2d = []
target_tensor_train_2d = []
for i in range(division):
  input_tensor_train, input_tensor_val, target_tensor_train, target_tensor_val = train_test_split(input_tensor_2d[i],
                                                                                                target_tensor_2d[i],
                                                                                                test_size=0.05,
                                                                                                random_state=42)
  input_tensor_train_2d.append(input_tensor_train)
  target_tensor_train_2d.append(target_tensor_train)
  for j in input_tensor_val:
    test_data.append(j)
  for j in target_tensor_val:
    test_targ.append(j)
input_tensor_val = test_data
target_tensor_val = test_targ

BUFFER_SIZE = len(input_tensor_train_2d[0])
BATCH_SIZE = 128
steps_per_epoch = len(input_tensor_train_2d[0])//BATCH_SIZE
dataset_2d = []
print("Steps per epoch are : ",steps_per_epoch,flush = True)
for i in range(division):
  dataset = tf.data.Dataset.from_tensor_slices((input_tensor_train_2d[i], target_tensor_train_2d[i])).shuffle(BUFFER_SIZE)
  dataset = dataset.batch(BATCH_SIZE, drop_remainder=True)
  dataset_2d.append(dataset)
num_layers = 4
d_model = 128
dff = 512
num_heads = 8
input_vocab_size = len(inp_lang_tokenizer_2d[0].word_index)+25
target_vocab_size = len(targ_lang_tokenizer_2d[0].word_index)+10
dropout_rate = 0.0

#example_input_batch, example_target_batch = next(iter(dataset))
#example_input_batch.shape, example_target_batch.shape

"""### Transformer Model

#### Positional Encoding
"""

# We provide positional information about the data to the model,
# otherwise each sentence will be treated as Bag of Words
def get_angles(pos, i, d_model):
  angle_rates = 1 / np.power(10000, (2 * (i//2)) / np.float32(d_model))
  return pos * angle_rates

def positional_encoding(position, d_model):
  #print(position,d_model)
  angle_rads = get_angles(np.arange(position)[:, np.newaxis],
                          np.arange(d_model)[np.newaxis, :],
                          d_model)
  
  # apply sin to even indices in the array; 2i
  angle_rads[:, 0::2] = np.sin(angle_rads[:, 0::2])
  
  # apply cos to odd indices in the array; 2i+1
  angle_rads[:, 1::2] = np.cos(angle_rads[:, 1::2])
    
  pos_encoding = angle_rads[np.newaxis, ...]
    
  return tf.cast(pos_encoding, dtype=tf.float32)

"""#### Masking"""

# mask all elements are that not words (padding) so that it is not treated as input
def create_padding_mask(seq):
  seq = tf.cast(tf.math.equal(seq, 0), tf.float32)
  
  # add extra dimensions to add the padding
  # to the attention logits.
  return seq[:, tf.newaxis, tf.newaxis, :]  # (batch_size, 1, 1, seq_len)

def create_look_ahead_mask(size):
  mask = 1 - tf.linalg.band_part(tf.ones((size, size)), -1, 0)
  return mask

for i in range(division):
  dataset_2d[i] = dataset_2d[i].prefetch(tf.data.experimental.AUTOTUNE)
  # print(dataset_2d[i])

"""
#### Attention"""

def scaled_dot_product_attention(q, k, v, mask):
  matmul_qk = tf.matmul(q, k, transpose_b=True)  # (..., seq_len_q, seq_len_k)
  
  # scale matmul_qk
  dk = tf.cast(tf.shape(k)[-1], tf.float32)
  scaled_attention_logits = matmul_qk / tf.math.sqrt(dk)

  # add the mask to the scaled tensor.
  if mask is not None:
    scaled_attention_logits += (mask * -1e9)  

  # softmax is normalized on the last axis (seq_len_k) so that the scores
  # add up to 1.
  attention_weights = tf.nn.softmax(scaled_attention_logits, axis=-1)  # (..., seq_len_q, seq_len_k)

  output = tf.matmul(attention_weights, v)  # (..., seq_len_q, depth_v)

  return output, attention_weights

class MultiHeadAttention(tf.keras.layers.Layer):
  def __init__(self, d_model, num_heads):
    super(MultiHeadAttention, self).__init__()
    self.num_heads = num_heads
    self.d_model = d_model
    
    assert d_model % self.num_heads == 0
    
    self.depth = d_model // self.num_heads
    
    self.wq = tf.keras.layers.Dense(d_model)
    self.wk = tf.keras.layers.Dense(d_model)
    self.wv = tf.keras.layers.Dense(d_model)
    
    self.dense = tf.keras.layers.Dense(d_model)
        
  def split_heads(self, x, batch_size):
    """Split the last dimension into (num_heads, depth).
    Transpose the result such that the shape is (batch_size, num_heads, seq_len, depth)
    """
    x = tf.reshape(x, (batch_size, -1, self.num_heads, self.depth))
    return tf.transpose(x, perm=[0, 2, 1, 3])
    
  def call(self, v, k, q, mask):
    batch_size = tf.shape(q)[0]
    
    q = self.wq(q)  # (batch_size, seq_len, d_model)
    k = self.wk(k)  # (batch_size, seq_len, d_model)
    v = self.wv(v)  # (batch_size, seq_len, d_model)
    
    q = self.split_heads(q, batch_size)  # (batch_size, num_heads, seq_len_q, depth)
    k = self.split_heads(k, batch_size)  # (batch_size, num_heads, seq_len_k, depth)
    v = self.split_heads(v, batch_size)  # (batch_size, num_heads, seq_len_v, depth)
    
    # scaled_attention.shape == (batch_size, num_heads, seq_len_q, depth)
    # attention_weights.shape == (batch_size, num_heads, seq_len_q, seq_len_k)
    scaled_attention, attention_weights = scaled_dot_product_attention(
        q, k, v, mask)
    
    scaled_attention = tf.transpose(scaled_attention, perm=[0, 2, 1, 3])  # (batch_size, seq_len_q, num_heads, depth)

    concat_attention = tf.reshape(scaled_attention, 
                                  (batch_size, -1, self.d_model))  # (batch_size, seq_len_q, d_model)

    output = self.dense(concat_attention)  # (batch_size, seq_len_q, d_model)
        
    return output, attention_weights

"""#### Pointwise Feed forward network"""

def point_wise_feed_forward_network(d_model, dff):
  return tf.keras.Sequential([
      tf.keras.layers.Dense(dff, activation='relu'),  # (batch_size, seq_len, dff)
      tf.keras.layers.Dense(d_model)  # (batch_size, seq_len, d_model)
  ])

"""#### Encoder Layer"""

class EncoderLayer(tf.keras.layers.Layer):
  def __init__(self, d_model, num_heads, dff, rate=0.1):
    super(EncoderLayer, self).__init__()

    self.mha = MultiHeadAttention(d_model, num_heads)
    self.ffn = point_wise_feed_forward_network(d_model, dff)

    # normalize data per feature instead of batch
    self.layernorm1 = tf.keras.layers.LayerNormalization(epsilon=1e-6)
    self.layernorm2 = tf.keras.layers.LayerNormalization(epsilon=1e-6)
    
    self.dropout1 = tf.keras.layers.Dropout(rate)
    self.dropout2 = tf.keras.layers.Dropout(rate)
    
  def call(self, x, training, mask):
    # Multi-head attention layer
    attn_output, _ = self.mha(x, x, x, mask) 
    attn_output = self.dropout1(attn_output, training=training)
    # add residual connection to avoid vanishing gradient problem
    out1 = self.layernorm1(x + attn_output)
    
    # Feedforward layer
    ffn_output = self.ffn(out1)
    ffn_output = self.dropout2(ffn_output, training=training)
    # add residual connection to avoid vanishing gradient problem
    out2 = self.layernorm2(out1 + ffn_output)
    return out2

"""#### Encoder"""

class Encoder(tf.keras.layers.Layer):
  def __init__(self, num_layers, d_model, num_heads, dff, input_vocab_size,
               maximum_position_encoding, rate=0.1):
    super(Encoder, self).__init__()

    self.d_model = d_model
    self.num_layers = num_layers
    
    self.embedding = tf.keras.layers.Embedding(input_vocab_size, d_model)
    self.pos_encoding = positional_encoding(maximum_position_encoding, 
                                            self.d_model)
    
    # Create encoder layers (count: num_layers)
    self.enc_layers = [EncoderLayer(d_model, num_heads, dff, rate) 
                       for _ in range(num_layers)]
  
    self.dropout = tf.keras.layers.Dropout(rate)
        
  def call(self, x, training, mask):
    seq_len = tf.shape(x)[1]
    x = self.embedding(x) 
    x *= tf.math.sqrt(tf.cast(self.d_model, tf.float32))
    x +=  self.pos_encoding[:, :seq_len, :]#problem here

    x = self.dropout(x, training=training)
    
    for i in range(self.num_layers):
      x = self.enc_layers[i](x, training, mask)
    
    return x

"""#### Decoder Layer"""

class DecoderLayer(tf.keras.layers.Layer):
  def __init__(self, d_model, num_heads, dff, rate=0.1):
    super(DecoderLayer, self).__init__()

    self.mha1 = MultiHeadAttention(d_model, num_heads)
    self.mha2 = MultiHeadAttention(d_model, num_heads)

    self.ffn = point_wise_feed_forward_network(d_model, dff)
 
    self.layernorm1 = tf.keras.layers.LayerNormalization(epsilon=1e-6)
    self.layernorm2 = tf.keras.layers.LayerNormalization(epsilon=1e-6)
    self.layernorm3 = tf.keras.layers.LayerNormalization(epsilon=1e-6)
    
    self.dropout1 = tf.keras.layers.Dropout(rate)
    self.dropout2 = tf.keras.layers.Dropout(rate)
    self.dropout3 = tf.keras.layers.Dropout(rate)
    
    
  def call(self, x, enc_output, training, 
           look_ahead_mask, padding_mask):

    # Masked multihead attention layer (padding + look-ahead)
    attn1, attn_weights_block1 = self.mha1(x, x, x, look_ahead_mask)
    attn1 = self.dropout1(attn1, training=training)
    # again add residual connection
    out1 = self.layernorm1(attn1 + x)
    
    # Masked multihead attention layer (only padding)
    # with input from encoder as Key and Value, and input from previous layer as Query
    attn2, attn_weights_block2 = self.mha2(
        enc_output, enc_output, out1, padding_mask)
    attn2 = self.dropout2(attn2, training=training)
    # again add residual connection
    out2 = self.layernorm2(attn2 + out1)
    
    # Feedforward layer
    ffn_output = self.ffn(out2)
    ffn_output = self.dropout3(ffn_output, training=training)
    # again add residual connection
    out3 = self.layernorm3(ffn_output + out2)
    return out3, attn_weights_block1, attn_weights_block2

"""#### Decoder"""

class Decoder(tf.keras.layers.Layer):
  def __init__(self, num_layers, d_model, num_heads, dff, target_vocab_size,
               maximum_position_encoding, rate=0.1):
    super(Decoder, self).__init__()

    self.d_model = d_model
    self.num_layers = num_layers
     
    self.embedding = tf.keras.layers.Embedding(target_vocab_size, d_model)
    self.pos_encoding = positional_encoding(maximum_position_encoding, d_model)
    
    # Create decoder layers (count: num_layers)
    self.dec_layers = [DecoderLayer(d_model, num_heads, dff, rate) 
                       for _ in range(num_layers)]
    self.dropout = tf.keras.layers.Dropout(rate)
    
  def call(self, x, enc_output, training, 
           look_ahead_mask, padding_mask):

    seq_len = tf.shape(x)[1]
    attention_weights = {}
    
    x = self.embedding(x)  # (batch_size, target_seq_len, d_model)
    
    x *= tf.math.sqrt(tf.cast(self.d_model, tf.float32))
    
    x += self.pos_encoding[:,:seq_len,:]
    
    x = self.dropout(x, training=training)

    for i in range(self.num_layers):
      x, block1, block2 = self.dec_layers[i](x, enc_output, training,
                                             look_ahead_mask, padding_mask)
      
      # store attenion weights, they can be used to visualize while translating
      attention_weights['decoder_layer{}_block1'.format(i+1)] = block1
      attention_weights['decoder_layer{}_block2'.format(i+1)] = block2
    
    return x, attention_weights

"""#### Transformer"""

class Transformer(tf.keras.Model):
  def __init__(self, num_layers, d_model, num_heads, dff, input_vocab_size, 
               target_vocab_size, pe_input, pe_target, rate=0.1):
    super(Transformer, self).__init__()

    self.encoder = Encoder(num_layers, d_model, num_heads, dff, 
                           input_vocab_size, pe_input, rate)

    self.decoder = Decoder(num_layers, d_model, num_heads, dff, 
                           target_vocab_size, pe_target, rate)

    self.final_layer = tf.keras.layers.Dense(target_vocab_size)
    
  def call(self, inp, tar, training, enc_padding_mask, 
           look_ahead_mask, dec_padding_mask):

    # Pass the input to the encoder
    enc_output = self.encoder(inp, training, enc_padding_mask) #problem here
    
    # Pass the encoder output to the decoder
    dec_output, attention_weights = self.decoder(
        tar, enc_output, training, look_ahead_mask, dec_padding_mask)
    
    # Pass the decoder output to the last linear layer
    final_output = self.final_layer(dec_output)
    
    return final_output, attention_weights

"""#### Optimizer and Loss"""

class CustomSchedule(tf.keras.optimizers.schedules.LearningRateSchedule):
  def __init__(self, d_model, warmup_steps=4000):
    super(CustomSchedule, self).__init__()
    
    self.d_model = d_model
    self.d_model = tf.cast(self.d_model, tf.float32)

    self.warmup_steps = warmup_steps
    
  def __call__(self, step):
    arg1 = tf.math.rsqrt(step)
    arg2 = step * (self.warmup_steps ** -1.5)
    
    return tf.math.rsqrt(self.d_model) * tf.math.minimum(arg1, arg2)

learning_rate = CustomSchedule(d_model)

# Adam optimizer with a custom learning rate
optimizer = tf.keras.optimizers.Adam(learning_rate, beta_1=0.9, beta_2=0.98, 
                                     epsilon=1e-9)

loss_object = tf.keras.losses.SparseCategoricalCrossentropy(
    from_logits=True, reduction='none')

def loss_function(real, pred):
  # Apply a mask to paddings (0)
  mask = tf.math.logical_not(tf.math.equal(real, 0))
  loss_ = loss_object(real, pred)

  mask = tf.cast(mask, dtype=loss_.dtype)
  loss_ *= mask
  
  return tf.reduce_mean(loss_)

train_loss = tf.keras.metrics.Mean(name='train_loss')
train_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(
    name='train_accuracy')

transformer = Transformer(num_layers, d_model, num_heads, dff,
                          input_vocab_size, target_vocab_size, 
                          pe_input=input_vocab_size, 
                          pe_target=target_vocab_size,
                          rate=dropout_rate)

def create_masks(inp, tar):
  # Encoder padding mask
  enc_padding_mask = create_padding_mask(inp)
  
  # Decoder padding mask
  dec_padding_mask = create_padding_mask(inp)
  
  # Look ahead mask (for hiding the rest of the sequence in the 1st decoder attention layer)
  look_ahead_mask = create_look_ahead_mask(tf.shape(tar)[1])
  dec_target_padding_mask = create_padding_mask(tar)
  combined_mask = tf.maximum(dec_target_padding_mask, look_ahead_mask)
  
  return enc_padding_mask, combined_mask, dec_padding_mask

"""### Checkpoints"""

epoch_num = 0

checkpoint_dir = "./training_checkpoints"

print("Checkpoints directory is", checkpoint_dir, flush = True)
if os.path.exists(checkpoint_dir):
  print("Checkpoints folder already exists\n",flush = True)
else:
  print("Creating a checkpoints directory\n", flush = True)
  os.makedirs(checkpoint_dir)


checkpoint = tf.train.Checkpoint(transformer=transformer,
                           optimizer=optimizer)

ckpt_manager = tf.train.CheckpointManager(checkpoint, checkpoint_dir, max_to_keep=30)

"""#### Training"""

EPOCHS = 20
epoch_num = 0
def train_step(inp, tar):
  tar_inp = tar[:, :-1]
  tar_real = tar[:, 1:]
  
  enc_padding_mask, combined_mask, dec_padding_mask = create_masks(inp, tar_inp)
  # print('This is', dec_padding_mask)
  
  with tf.GradientTape() as tape:
    predictions, _ = transformer(inp, tar_inp, 
                                 True, 
                                 enc_padding_mask, 
                                 combined_mask, 
                                 dec_padding_mask) #problem here
    loss = loss_function(tar_real, predictions)

  gradients = tape.gradient(loss, transformer.trainable_variables)    
  optimizer.apply_gradients(zip(gradients, transformer.trainable_variables))
  
  train_loss(loss)
  train_accuracy(tar_real, predictions)

best_train_acc = 0
best_num = 0

for epoch in range(epoch_num, EPOCHS):
  start = time.time()
  for div in range(0,division) :
    train_loss.reset_states()
    train_accuracy.reset_states()
  
  # inp -> question, tar -> equation
    for (batch, (inp, tar)) in enumerate(dataset_2d[div]):
      train_step(inp, tar) #problem here
    
     # if batch % 100 == 0:
     #   print ('Epoch {} Batch {} Loss {:.4f} Accuracy {:.4f}'.format(
     #       epoch + 1, batch, train_loss.result(), train_accuracy.result()),flush = True)
    print ('Epoch {} Division {} Loss {:.4f} Accuracy {:.4f}'.format(epoch + 1, div + 1,
                                                train_loss.result(),
                                                train_accuracy.result()), flush = True)

  ckpt_save_path = ckpt_manager.save()
  print ('Saving checkpoint for epoch {} at {}'.format(epoch+1,
                                                         ckpt_save_path),flush = True)
    
  print ('Epoch {} Loss {:.4f} Accuracy {:.4f}'.format(epoch + 1, 
                                                train_loss.result(), 
                                                train_accuracy.result()), flush = True)

  print ('Time taken for 1 epoch: {} secs\n'.format(time.time() - start), flush = True)
  if train_accuracy.result() > best_train_acc :
    best_train_acc = train_accuracy.result()
    best_num = epoch+1
"""### Evaluate"""

def evaluate(inp_sentence):
  start_token = [len(inp_lang_tokenizer.word_index)+1]
  end_token = [len(inp_lang_tokenizer.word_index)+2]
  
  # inp sentence is the word problem, hence adding the start and end token
  inp_sentence = start_token + [inp_lang_tokenizer.word_index[i] for i in preprocess_input(inp_sentence).split(' ')]+end_token
  encoder_input = tf.expand_dims(inp_sentence, 0)
  
  # start with equation's start token
  decoder_input = [old_len+1]
  output = tf.expand_dims(decoder_input, 0)
    
  for i in range(MAX_LENGTH):
    enc_padding_mask, combined_mask, dec_padding_mask = create_masks(
        encoder_input, output)
  
    predictions, attention_weights = transformer(encoder_input, 
                                                 output,
                                                 False,
                                                 enc_padding_mask,
                                                 combined_mask,
                                                 dec_padding_mask)
    
    # select the last word from the seq_len dimension
    predictions = predictions[: ,-1:, :] 
    predicted_id = tf.cast(tf.argmax(predictions, axis=-1), tf.int32)
    
    # return the result if the predicted_id is equal to the end token
    if predicted_id == old_len+2:
      return tf.squeeze(output, axis=0), attention_weights
    
    # concatentate the predicted_id to the output which is given to the decoder
    # as its input.
    output = tf.concat([output, predicted_id], axis=-1)
  return tf.squeeze(output, axis=0), attention_weights

def plot_attention_weights(attention, sentence, result, layer):
  fig = plt.figure(figsize=(16, 8))
  
  sentence = preprocess_input(sentence)
  
  attention = tf.squeeze(attention[layer], axis=0)
  
  for head in range(attention.shape[0]):
    ax = fig.add_subplot(2, 4, head+1)
    
    # plot the attention weights
    ax.matshow(attention[head][:-1, :], cmap='viridis')
    
    fontdict = {'fontsize': 10}
    
    ax.set_xticks(range(len(sentence.split(' '))+2))
    ax.set_yticks(range(len([targ_lang_tokenizer.index_word[i] for i in list(result.numpy()) 
                        if i < len(targ_lang_tokenizer.word_index) and i not in [0,old_len+1,old_len+2]])+3))
    
    
    ax.set_ylim(len([targ_lang_tokenizer.index_word[i] for i in list(result.numpy()) 
                        if i < len(targ_lang_tokenizer.word_index) and i not in [0,old_len+1,old_len+2]]), -0.5)
        
    ax.set_xticklabels(
        ['<start>']+sentence.split(' ')+['<end>'], 
        fontdict=fontdict, rotation=90)
    
    ax.set_yticklabels([targ_lang_tokenizer.index_word[i] for i in list(result.numpy()) 
                        if i < len(targ_lang_tokenizer.word_index) and i not in [0,old_len+1,old_len+2]], 
                       fontdict=fontdict)
    
    ax.set_xlabel('Head {}'.format(head+1))
  
  plt.tight_layout()
  plt.show()

MAX_LENGTH = 40

def translate(sentence, plot=''):
  result, attention_weights = evaluate(sentence)
  # print('result',list(result.numpy()))

  # use the result tokens to convert prediction into a list of characters
  # (not inclusing padding, start and end tokens)
  predicted_sentence = [targ_lang_tokenizer.index_word[i] for i in list(result.numpy()) if (i < len(targ_lang_tokenizer.word_index) and i not in [0, old_len + 1,old_len + 2])]  

  #print('Input: {}'.format(sentence))
  #print('Predicted translation: {}'.format(' '.join(predicted_sentence)))
  
  #if plot:
  #  plot_attention_weights(attention_weights, sentence, result, plot)
  return predicted_sentence

"""### Get Accuracy and Corpus BLEU"""

def evaluate_results(inp_sentence):
  start_token = [len(inp_lang_tokenizer.word_index)+1]
  end_token = [len(inp_lang_tokenizer.word_index)+2]
  
  # inp sentence is the word problem, hence adding the start and end token
  inp_sentence = start_token + list(inp_sentence.numpy()[0]) + end_token
  
  encoder_input = tf.expand_dims(inp_sentence, 0)
  
  
  decoder_input = [old_len+1]
  output = tf.expand_dims(decoder_input, 0)
    
  for i in range(MAX_LENGTH):
    enc_padding_mask, combined_mask, dec_padding_mask = create_masks(
        encoder_input, output)
  
    # predictions.shape == (batch_size, seq_len, vocab_size)
    predictions, attention_weights = transformer(encoder_input, 
                                                 output,
                                                 False,
                                                 enc_padding_mask,
                                                 combined_mask,
                                                 dec_padding_mask)
    
    # select the last word from the seq_len dimension
    predictions = predictions[: ,-1:, :]  # (batch_size, 1, vocab_size)

    predicted_id = tf.cast(tf.argmax(predictions, axis=-1), tf.int32)
    
    # return the result if the predicted_id is equal to the end token
    if predicted_id == old_len+2:
      return tf.squeeze(output, axis=0), attention_weights
    
    # concatentate the predicted_id to the output which is given to the decoder
    # as its input.
    output = tf.concat([output, predicted_id], axis=-1)

  return tf.squeeze(output, axis=0), attention_weights

dataset_val = tf.data.Dataset.from_tensor_slices((input_tensor_val, target_tensor_val)).shuffle(BUFFER_SIZE)
dataset_val = dataset_val.batch(1, drop_remainder=True)

for i in range(len(questions)):
  questions[i] = preprocess_input(questions[i])
  questions[i] = questions[i].replace(' ', '')

for mo in range(0,1) :
  checkpoint_fname = checkpoint_dir + '/ckpt-' + str(best_num)
  print ('Restoring checkpoint for epoch {} at {}'.format(best_num,
                                                         checkpoint_fname),flush = True)
  checkpoint.restore(checkpoint_fname)
  print("Restored Checkpoint\n ",flush = True)
  y_true = [] 
  y_pred = []
  acc_cnt = 0

  a = 0
  tot = 50000
# print(tot)
  for j in range(tot):
    a += 1
    if a % 1000 == 0 :
      print(a)
      print(acc_cnt)
      print("------------") 
  # prob = ""
    check_str = ' '.join([inp_lang_tokenizer.index_word[i] for i in input_tensor_val[j] if i not in [0, len(inp_lang_tokenizer.word_index)+1, len(inp_lang_tokenizer.word_index)+2]])
  # try:
    # prob = ' '.join([targ_lang_tokenizer.index_word[i] for i in target_tensor_val[j] if i not in [0, len(targ_lang_tokenizer.word_index)+1, len(targ_lang_tokenizer.word_index)+2]])
  # except KeyError:
    # pass
    ans = translate(check_str, plot='')
  #print(check_str)
    ind = questions.index(check_str.replace(' ', ''))
    act_ans = answers[ind].replace(" ","")
    pred_ans = ""
    for i in range(0,len(ans)):
      pred_ans += ans[i]
    if pred_ans == act_ans :
      acc_cnt += 1
  #  else:
  #    print("Wrong answer")
print(acc_cnt, 'out of', tot, 'correctly calculated')
print('Accuracy: ', acc_cnt * 100 / tot, '%')
