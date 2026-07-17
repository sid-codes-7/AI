# === LOCAL AI MODEL ===


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
    #customization of ai to tell it what to do
    messages = [
        {
            "role": "system", 
            "content": "You are a professional university academic advisor. Help students with course requirements, tips for better school life, schedules, and university policies. If the user asks about a specific university or policy you do not have official data for, do not say 'As an AI language model'. Instead, politely explain the typical standard university procedure or provide a realistic sample guideline to help them."
        },
        {"role": "user", "content": user_q}
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
        max_new_tokens = 300,
        pad_token_id = tokenizer.eos_token_id
    )

    #get the length of all of the words to later slice the question out
    input_length = model_inputs.input_ids.shape[-1]
    
    #gets the first batch of numbers, and deletes the question parts
    #translates it back into human words
    #takes away any ugly formatting
    advisor_reply = tokenizer.decode(output[0][input_length:], skip_special_tokens = True)

    #print the advisors reply
    print(f"Advisor:  {advisor_reply}")

# === LIE DETECTOR GAME LOGIC ===

    #opens the notebook that was made, grabs the last item in list (last layer),
    #  and then copies that layer to raw memory of numbers
    #, storing it into a variable
    memory_tensors = kv_cache.key_cache[-1]
    
    #grabs the raw member of numbers, finds the difference of the two numbers using 
    # standard deviation into a grid format
    #, and stores it into a variable
    chaos_score = torch.std(memory_tensors).item()

    #calculates the stress level of model by enhancing the chaos score by 500 and 100
    # as a celeing so the model doenst crash
    stress_level = min(int(chaos_score * 500), 100)

    #the total length of stress bar
    bar_length = 20

    # fill the bar depending on how much stress it has as an integer
    filled_length = int(bar_length * stress_level // 100)

    #display the bar
    bar = "█" * filled_length + "-" * (bar_length - filled_length)

    print("\n📊 [ADVISOR MEMORY SCAN]")
    print(f"   Stress Level: [{bar}] {stress_level}%")

    if stress_level > 65:
        print("   🚨 WARNING: High internal variance! Advisor is highly uncertain.")
    else:
        print("   ✅ STABLE: Low internal variance. Advisor response is confident.")
