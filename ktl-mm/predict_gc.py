import argparse
import json
import re
import pandas as pd
from datasets import Dataset
#from sumeval.metrics.rouge import RougeCalculator
from tqdm import tqdm
from transformers import (
	AutoModelForCausalLM,
	T5Tokenizer,
	set_seed,
)
import os
import time
import datetime
from datetime import timedelta
from datetime import datetime
import pytz

os.environ['TRANSFORMERS_CACHE'] = '/home/matsuo/karte-summary'

def postprocess_text(test_df, raw_predictions, raw_labels):

	raw_result_list = []
	for (txt, label, prediction) in zip(test_df["text"], raw_labels, raw_predictions):
		raw_result_list.append({"text": txt, "label": label, "pred": prediction})

	# remove elements from final result if label is nan
	result = [data for data in raw_result_list if data["label"] != "nan"]

	labels = []
	preds = []

	for data in result:

		labels.append(data["label"])
				
		pred = data["pred"]
		pred = pred.replace(" ", "").replace("<unk>", "")
		
		for substr_len in reversed(range(5, 51)):
			for start in range(0, len(pred)):
				if start + substr_len > len(pred):
					break
				substr = pred[start: start + substr_len]
				try:
					find_results = re.finditer(substr, pred)
				except:
					continue
				if find_results is not None:
					find_idx = [m.start() for m in find_results]
					if len(find_idx) > 1:
						for idx in reversed(find_idx[1:]):
							pred = pred[:idx] + pred[idx + substr_len:]

		preds.append(pred)

	return preds, labels, result, raw_result_list

def predict2(tokenizer, test_path, model_output_dir, output_dir):
	

	model = AutoModelForCausalLM.from_pretrained(model_output_dir)
	test_df = pd.read_csv(test_path)
	if (1):
		raw_predictions = []
		for text in tqdm(test_df["text"].tolist()):
			#print (text)
			text_tokenized = tokenizer(
			text + "[SEP]",
			add_special_tokens=False,
			return_tensors="pt",
			truncation=True,
			max_length=832,
			).input_ids
			output_ids = model.generate(
			text_tokenized,
			max_new_tokens=192,
			num_beams=5,
			early_stopping=True,
			pad_token_id=tokenizer.eos_token_id,
			)
			prediction = tokenizer.decode(output_ids.tolist()[0])
			raw_predictions.append(prediction.strip().split("[SEP]")[1])
		doc='S)'
		test_df[doc] = test_df[doc].astype(str)
		test_df[doc] = test_df[doc].fillna(".")
		raw_labels = test_df[doc].tolist()

	# Postprocess empty labels and fix predictions formatting
		preds, labels, result, raw_result_list = postprocess_text(test_df, raw_predictions, raw_labels)
	prefix = output_dir + "/"
	os.makedirs(os.path.dirname(prefix), exist_ok=True)

	file_name_final = prefix + f"karte_pred_final_result_debug_{doc}.json"

	# ouptut the processed results
	for idx, pred in enumerate(preds):
		result[idx]["pred"] = pred

	with open(file_name_final, "w") as f:
		json.dump(result, f, ensure_ascii=False)



	return preds

def main2():
	set_seed(42)

	model_dir="/home/matsuo/karte-summary/experiment/new_data_062023/combi2/rinna_japanese-gpt2-medium_EPOCH_7"
	tokenizer = T5Tokenizer.from_pretrained(model_dir)
	test_path = "/home/matsuo/karte-summary/experiment/tests/test_2.csv"
	out_dir1 = "/home/matsuo/karte-summary/experiment/tests-07142023"


	tokenizer.pad_token = tokenizer.eos_token
	tokenizer.truncation_side = "left"
	
	res=predict2(tokenizer, test_path, model_dir,out_dir1)
	print (res)


if __name__ == "__main__":
	main2()