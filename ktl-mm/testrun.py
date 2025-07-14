num_return_sequences = 5
prompt = "最高の:"
input_ids = tokenizer.encode(prompt, return_tensors="pt",add_special_tokens=False).to(device)
with torch.no_grad():
    output = model.generate(
        input_ids,
        max_length=100,
        min_length=100,
        do_sample=True,
        top_k=500,
        top_p=0.95,
        pad_token_id=tokenizer.pad_token_id,
        bos_token_id=tokenizer.bos_token_id,
        eos_token_id=tokenizer.eos_token_id,
        bad_word_ids=[[tokenizer.unk_token_id]],
        num_return_sequences=5
    )
decoded = tokenizer.batch_decode(output,skip_special_tokens=True)
for i in range(num_return_sequences):
  print(decoded[i])
