from transformers import AutoModelForCausalLM, Trainer, TrainingArguments, AutoTokenizer
from datasets import load_from_disk

# Cargar el dataset tokenizado
tokenized_dataset = load_from_disk('tokenized_dataset')

model = AutoModelForCausalLM.from_pretrained("meta-llama/Meta-Llama-3-8B")
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-8B")

training_args = TrainingArguments(
  output_dir='./results',
  evaluation_strategy="epoch",
  learning_rate=2e-5,
  per_device_train_batch_size=2,
  per_device_eval_batch_size=2,
  num_train_epochs=3,
  weight_decay=0.01,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset['train'],
    eval_dataset=tokenized_dataset['test']
)

trainer.train()

# Guardar el modelo fine-tuned
model.save_pretrained("./fine_tuned_model")
tokenizer.save_pretrained("./fine_tuned_model")
