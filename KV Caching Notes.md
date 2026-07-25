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
