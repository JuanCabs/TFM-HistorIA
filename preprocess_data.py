import os
from datasets import load_dataset
from transformers import AutoTokenizer

# Set the Hugging Face token
os.environ['HUGGINGFACE_HUB_TOKEN'] = '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'

# Load the dataset
dataset = load_dataset('json', data_files='dataset.json')

# Tokenizer
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.3", token=os.environ['HUGGINGFACE_HUB_TOKEN'])

def preprocess_function(examples):
    inputs = examples['prompt']
    targets = examples['response']
    model_inputs = tokenizer(inputs, max_length=128, truncation=True)

    # Setup the tokenizer for targets
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(targets, max_length=128, truncation=True)

    model_inputs['labels'] = labels['input_ids']
    return model_inputs

# Apply the preprocessing function
tokenized_dataset = dataset.map(preprocess_function, batched=True)

# Save the tokenized dataset to disk
tokenized_dataset.save_to_disk('tokenized_dataset')
