#Creating Components for the Model Training
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from TextSummarizerLLM.entity import ModelTrainingConfig
from datasets import load_dataset, load_from_disk
import torch
import os 


class ModelTrainer:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config

    
    def train(self):
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)

        #load Data into the model including parameters
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=self.config.num_train_epochs,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            warmup_steps=self.config.warmup_steps,
            weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps,
            evaluation_strategy=self.config.evaluation_strategy,
            eval_steps=self.config.eval_steps,
            save_steps=1e6,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps,
            per_device_eval_batch_size=self.config.per_device_train_batch_size
        )

        trainer = Trainer(
            model=model_pegasus,
            args=trainer_args,
            tokenizer=tokenizer,
            data_collator=seq2seq_data_collator,
            train_dataset=dataset_samsum_pt['test'],
            eval_dataset=dataset_samsum_pt['validation'],
        )

        trainer.train()

        #save the model into the model file
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir, 'pegasus-samsum-model'))

        #save the tokenizer into the token file
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, 'tokenizer'))
        
