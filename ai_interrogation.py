# === LOCAL AI MODEL ===

from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers import AutoModelForCausalLM, AutoTokenizer, DynamicCache
import torch

# the model from Hugging Face
model_id = "Qwen/Qwen2.5-0.5B-Instruct"

# the model and text tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

print("Model successfully loaded!")

# === INTERROGATION INTERFACE & CACHE ===

while True:
    user_q = input("What is your question? ")

    if(user_q.lower() in ['q', 'quit', 'exit', 'close', 'bye', 'cya']):
        print("Interrogration Ended.")
        break

    #customization of ai to tell it what to do
    messages = [    
        {"role": "system", "content": "You are a criminal suspect being interrogated. You can choose to lie or tell the truth, but you are incredibly nervous."},
        {"role" : "user", "content": user_q}
        ]
    
    #glue together the words into long piece of text so it is later converted with a tokenizer
    #takes the script and wraps it around special tags to tell it where it starts and ends
    #the tokenize=False means to delay the tokenization, keeping it human letters for another second
    prompt_text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

    #the final package of numbers sent to the model
    #it turns the human words/letters into mathmatical codes
    #and formats it intro a grid shape(aka. tensor) that the torch can read
    model_inputs = tokenizer(prompt_text, return_tensors = 'pt')

    #A brand new notebook that the model refers to the lastest info on the book
    kv_cache = DynamicCache()


# === EXTRACT MEMORY TENSORS AFTER GENERATION ===

    #the output of the model
    #unwrap the numbers
    #pass in the blank notebook so the model can refer to it later
    #set a limit of tokens for model (aka. max it can generate)
    #signal an end of sentence marker
    output = model.generate(
        **model_inputs,
        past_key_values = kv_cache,
        max_new_tokens = 40,
        pad_token_id = tokenizer.eos_token_id
    )



# === CUSTOM LIE DETECTOR GAME LOGIC ===

