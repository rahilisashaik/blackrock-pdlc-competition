import torch

class DocumentationDataset(torch.utils.data.Dataset):
    def __init__(self, encodings):
        self.encodings = encodings

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        return item

    def __len__(self):
        return len(self.encodings["input_ids"])

train_encodings = {
    "input_ids": [item["input_ids"] for item in tokenized_training_data],
    "attention_mask": [item["attention_mask"] for item in tokenized_training_data],
    "labels": [item["labels"] for item in tokenized_training_data]
}

train_dataset = DocumentationDataset(train_encodings)
