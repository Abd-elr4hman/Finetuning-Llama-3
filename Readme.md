# Finetuning Llama 3
In this repo I experiment with finetuning llama3 8b model on synthetic dataset created using gpt4-o.

## Problem statment
I want to generate a medical report based on patient history and some measurments on the patient current health status.

I want the report to be detailed and describe each measurment.

I want the report to deduce a diagnostics.

## Data
The dataset was created using an existing dataset [Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

The steps to create and produce the data was as follows:
1. Turn every column of the dataset into into text description of the patient using prepared text templates.
2. Prompt gpt4-o asking for a complete analysis, detailed illustration and diagnostics.
3. Use gpt4-o output to train a smaller model like llama 8b


## Finetuning
I used the finetuning notebook offerd by [unsloth](https://github.com/unslothai/unsloth) using the data in ```data/synthetic.csv``` file. 

Complete notebook can be found in ```notebooks/Create_synthetic_dataset``` or on [GoogleColab](https://colab.research.google.com/drive/1iSAv8jwN3-fV9NVGqd_xEgAnu4p7kttq?usp=sharing)


## Outcome
llama 8b finetuned adheres very well to the format in the training data.

## Inference Examples
Examples can be fount in examples directory.
