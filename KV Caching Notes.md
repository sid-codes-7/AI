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

