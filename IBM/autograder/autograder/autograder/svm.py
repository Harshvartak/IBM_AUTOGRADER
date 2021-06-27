import numpy as np
import torch
from transformers import T5Tokenizer
import random

def preprocess(sA, rA):
	stsb = "stsb sentence1:"+sA+" sentence2:"+rA
	return tokenizer.encode(stsb, return_tensors="pt").to(device)


#MODEL TO BE ADDED LATER, ADDED FOR NORMALIZATION

def find_correctness_svm(sA, rA1, rA2="", rA3=""):

	rA_list = []

	rA_list.append(rA1)
	if rA2 != "":
		rA_list.append(rA2)
	if rA3 != "":
		rA_list.append(rA3)

	scores = round(random.uniform(3.0,5.0),2)

	print(scores)

	return scores