# from videollama2 import model_init, mm_infer
# # import os
# # os.environ['HF_HOME'] = "/home/135/qc2666/dg/VideoLLaMA2/cache"

# model, processor, tokenizer = model_init()


# from datasets import load_dataset

# ds = load_dataset("MBZUAI/VideoInstruct-100K")
# ds = load_dataset("luoruipu1/Valley-Instruct-65k")


from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2", local_files_only=False)
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2", local_files_only=False)
