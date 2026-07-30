# KV Caching Notes

KV Cache, or Key-Value Cache

## What is it?

KV Caching is what a model uses to help generate its next token, which can be a word, symbol, or number. It is one of the most important parts of a model. For example, if a user asks the question: I was raised in France, and I am fluent in ________.

Without KV Caching, models need to recalculate the key and value vectors from their previous tokens for every generation and go through every step again and again, even though humans can identify this faster. With KV Caching, the model stores many key and value vectors and reuses them. This helps the model generate faster.

The model compares the query with the keys from previous tokens to create attention weights. These weights help determine how much information from each value should be used. A higher attention weight means the previous token is more relevant to the current token, helping to predict the next token.

## Query:

What the current token needs to search for in its previous tokens.

## Key:

What information the previous token contains.

## Value:

The information from a previous token that is weighted and combined with the values from all other previous tokens.
----------------------------------------
https://openreview.net/pdf?id=XM31M3uSUU

This paper explains how tokens in KV Caches can be summarized. 
By:
1. concatenating key and value vectors
2. averaging across layers
3. combining the information across attention heads
4. combining the information across token positions


## 1. concatenating key and value vectors
For example, if a token has:

K = [1, 2]

And another token has:

V = [3, 4]

Concatenation:

[K;V] = [1, 2, 3, 4]

Upside:

Lets the classifier see both what kind of information the token represents and the contained information that might be used.

Downside:

The vector becomes larger.

## 2. averaging across layers
Why? The same token has different key and value vectors in every layer

for example, **France** has 3 vectors

V1 = [2,4]
V2 = [4,8]
V3 = [6,3]

The system will average the vectors:
( [2,4] + [4,8] + [6,3] ) / 3 = [4,5]

[4,5] becomes a summarized vector.

Each of the layers catches different levels of information 
The downside is that some information in specific layers is lost.

## 3. combining information across attention heads
each transformer layer has several attention heads

attention heads, for example, can focus on:
- nearby words
- grammar
- connection of words

Suppose one token has 3 attention heads

H1 = [1,3]
H2 = [5,1]
H3 = [2,8]


The attention heads can be averaged or merged/concatenated.

This is because the classifier needs an overview of the information instead of dozens of separate head outputs.

## 4. combining the information across token positions
Say if the prompt is for these tokens:

The | dog | met | other | dogs | at | the | dog | park | . |
The model assigns a key and value vector for each token

The summarizer might select:

the most recent token,
first token, 
previous token,
special tokens,
etc.

then combines and averages them

for example, it selects:

dogs = [6, 4]
at = [2, 3]
dog = [1, 4]
park = [2, 5]

then will average them to get [3, 4]

Why not use every token?
1. There will be thousands of tokens
2. Increase the # of unnecessary tokens
3. Slower processing speeds
4. Selecting specific positions can make the classifier faster

# KV Cache Size Formula:
KV cache bytes = L × T × H_KV × D × 2 × B × N
