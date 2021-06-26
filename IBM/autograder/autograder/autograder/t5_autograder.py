
import numpy as np
import torch
from transformers import T5Tokenizer

model = torch.load('C:\\Users\\varta\\harsh_lab\\IBM Project\\IBM\\autograder\\autograder\\autograder\\model.pt')
model.eval()

tokenizer = T5Tokenizer.from_pretrained('C:\\Users\\varta\\harsh_lab\\IBM Project\\IBM\\autograder\\autograder\\autograder\\spiece.model')
device = torch.device('cpu')

def preprocess(sA, rA):
	stsb = "stsb sentence1:"+sA+" sentence2:"+rA
	return tokenizer.encode(stsb, return_tensors="pt").to(device)

def find_correctness(sA, rA1,model, rA2="", rA3=""):

	rA_list = []

	rA_list.append(rA1)
	if rA2 != "":
		rA_list.append(rA2)
	if rA3 != "":
		rA_list.append(rA3)

	scores = []

	for rA in rA_list:
	    stsb_tokenized = preprocess(sA, rA)
	    output = model.generate(stsb_tokenized, early_stopping=True)
	    scores.append(float(tokenizer.decode(output[0], skip_special_tokens=True)))

	max_score = max(scores)
	if max_score >= 2:
		return "CORRECT"
	else:
		return "INCORRECT"