import os
from collections import Counter

# Set this to your dataset path
DATASET_PATH = r"path/to/your/dataset/train"

images_path = os.path.join(DATASET_PATH, "images")
labels_path = os.path.join(DATASET_PATH, "labels")

images = os.listdir(images_path)
labels = os.listdir(labels_path)

print("Number of training images:", len(images))
print("Number of label files:", len(labels))

print("\nSample image files:", images[:5])
print("Sample label files:", labels[:5])

sample_label = labels[0]

with open(os.path.join(labels_path, sample_label), "r") as f:
    content = f.read()

print("Sample label content:\n", content)

# Update this path to your data.yaml file
with open(r"path/to/your/data.yaml", "r") as f:
    data = yaml.safe_load(f)

print(data)

labels_dir = os.path.join(DATASET_PATH, "labels")

class_counter = Counter()

for file in os.listdir(labels_dir):
    with open(os.path.join(labels_dir, file), "r") as f:
        for line in f.readlines():
            class_id = int(line.split()[0])
            class_counter[class_id] += 1

print(class_counter)

safe = 0
penalty = 0

for file in os.listdir(labels_dir):
    with open(os.path.join(labels_dir, file), "r") as f:
        classes = [int(line.split()[0]) for line in f.readlines()]
        if 1 in classes:
            penalty += 1
        else:
            safe += 1

print("SAFE images:", safe)
print("PENALTY images:", penalty)

import cv2
import matplotlib.pyplot as plt

img_dir = os.path.join(DATASET_PATH, "images")
img_name = os.listdir(img_dir)[0]

img = cv2.imread(os.path.join(img_dir, img_name))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.axis("off")

import os
import shutil

IMG_DIR = os.path.join(DATASET_PATH, "images")
LBL_DIR = os.path.join(DATASET_PATH, "labels")

SAFE_DIR = r"path/to/classification/dataset/safe"
PENALTY_DIR = r"path/to/classification/dataset/penalty"

os.makedirs(SAFE_DIR, exist_ok=True)
os.makedirs(PENALTY_DIR, exist_ok=True)

count_safe = 0
count_penalty = 0

for label_file in os.listdir(LBL_DIR):
    label_path = os.path.join(LBL_DIR, label_file)

    with open(label_path, "r") as f:
        classes = [int(line.split()[0]) for line in f]

    img_file = label_file.replace(".txt", ".jpg")
    img_path = os.path.join(IMG_DIR, img_file)

    if not os.path.exists(img_path):
        continue

    if 1 in classes:
        shutil.copy(img_path, PENALTY_DIR)
        count_penalty += 1
    else:
        shutil.copy(img_path, SAFE_DIR)
        count_safe += 1

print("SAFE images:", count_safe)
print("PENALTY images:", count_penalty)
