import os
import shutil
import random

# Paths
base_dir = r"C:\Users\Multimatics\plat_nomor\textplat"
mentah_dir_angka = os.path.join(base_dir, "mentah", "angka")
mentah_dir_huruf = os.path.join(base_dir, "mentah", "huruf")
tensor_dir = os.path.join(base_dir, "tensor")

# Tensor directories for angka and huruf
tensor_train_angka = os.path.join(tensor_dir, "angka", "train")
tensor_test_angka = os.path.join(tensor_dir, "angka", "test")
tensor_train_huruf = os.path.join(tensor_dir, "huruf", "train")
tensor_test_huruf = os.path.join(tensor_dir, "huruf", "test")

# Step 1: Delete tensor directory if it exists
if os.path.exists(tensor_dir):
    shutil.rmtree(tensor_dir)

# Step 2: Recreate directories
os.makedirs(tensor_train_angka, exist_ok=True)
os.makedirs(tensor_test_angka, exist_ok=True)
os.makedirs(tensor_train_huruf, exist_ok=True)
os.makedirs(tensor_test_huruf, exist_ok=True)

# Function to split files and move them
def split_and_move_files(source_dir, train_dir, test_dir, split_ratio=0.8):
    files = os.listdir(source_dir)
    random.shuffle(files)
    split_index = int(len(files) * split_ratio)
    train_files = files[:split_index]
    test_files = files[split_index:]

    # Move files to train directory
    for file in train_files:
        shutil.copy2(os.path.join(source_dir, file), os.path.join(train_dir, file))

    # Move files to test directory
    for file in test_files:
        shutil.copy2(os.path.join(source_dir, file), os.path.join(test_dir, file))

# Step 3: Split and move files for angka and huruf
split_and_move_files(mentah_dir_angka, tensor_train_angka, tensor_test_angka)
split_and_move_files(mentah_dir_huruf, tensor_train_huruf, tensor_test_huruf)

print("Files have been split and moved successfully.")
