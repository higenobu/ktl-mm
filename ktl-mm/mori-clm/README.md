---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: test-clm
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# test-clm

This model is a fine-tuned version of [rinna/japanese-gpt2-small](https://huggingface.co/rinna/japanese-gpt2-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.0270
- Accuracy: 0.6295

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results



### Framework versions

- Transformers 4.30.0.dev0
- Pytorch 2.0.1+cu117
- Datasets 2.12.0
- Tokenizers 0.13.3
