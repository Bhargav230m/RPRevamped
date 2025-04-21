from datasets import load_dataset

ds = load_dataset("TechPowerB/RPRevamped-Small")
print(ds['train'])

## Process the dataset for your use case further