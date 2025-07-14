python3 transformers/examples/pytorch/language-modeling/run_clm.py \
    --model_name_or_path rinna/japanese-gpt2-small \
    --train_file x-yotaro-train.json \
   --validation_file x-yotaro-dev.json \
    --per_device_train_batch_size 8 \
    --per_device_eval_batch_size 8 \
    --do_train \
    --do_eval \
    --output_dir finmodel/ \
  --low_cpu_mem_usage
