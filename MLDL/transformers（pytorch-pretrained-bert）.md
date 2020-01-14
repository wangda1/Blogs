---
title: Huggingface's transformers
date: 2020-01-14 10:25:00
categories:
- MLDL
tags:
- MLDL
---

# huggingface's `transformers`（`pytorch-pretrained-bert`）


## mdoel 的保存与加载

```python
# Save a trained model
model_to_save = model.module if hasattr(model, 'module') else model  # Only save the model it-self
output_model_file = os.path.join(args.output_dir, "pytorch_model.bin")
if args.do_train:
    torch.save(model_to_save.state_dict(), output_model_file)

# Load tsaved model
model_state_dict = torch.load(output_model_file)
model = BertForSequenceClassification.from_pretrained(args.bert_model, state_dict=model_state_dict, num_labels=num_labels)
```