import os
import random

def clean_label_file():
    dataset_path = "dataset\\ocr_rec_ocst"
    with open(os.path.join(dataset_path, "labels.txt"), "r") as f:
        labels = f.readlines()

    for label in labels:
        file_name, label_text = label.split(",")

        with open(os.path.join(dataset_path, "labels_clean.txt"), "a") as f:
            f.write(f"images/{file_name}\t{label_text}")

clean_label_file()


def split_label_file(train_ratio=0.85):

    dataset_path = "dataset\\ocr_rec_ocst"
    with open(os.path.join(dataset_path, "labels_clean.txt"), "r") as f:
        labels = f.readlines()

    random.shuffle(labels)
    split_index = int(len(labels) * train_ratio)

    train_labels = labels[:split_index]
    val_labels = labels[split_index:]

    with open(os.path.join(dataset_path, "train.txt"), "w") as f:
        f.write("".join(train_labels))

    with open(os.path.join(dataset_path, "val.txt"), "w") as f:
        f.write("".join(val_labels))


split_label_file()