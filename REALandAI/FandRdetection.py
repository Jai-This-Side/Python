import os
import pandas as pd
import numpy as np
import cv2
from PIL import Image
import tensorflow as tf
from tensorflow.keras import models, layers
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
from tqdm import tqdm

# --------------------------------------------------
# 1. CHECK WORKING DIRECTORY
# --------------------------------------------------
print("Current working directory:", os.getcwd())

# ---------- FIXED PATHS ----------
BASE_TRAIN_FAKE = "INPUTS/archive/train/FAKE"
BASE_TRAIN_REAL = "INPUTS/archive/train/REAL"
BASE_TEST_FAKE  = "INPUTS/archive/test/FAKE"
BASE_TEST_REAL  = "INPUTS/archive/test/REAL"

# --------------------------------------------------
# 2. TEST A SAMPLE IMAGE
# --------------------------------------------------
test_img_path = os.path.join(BASE_TRAIN_FAKE, "5999.jpg")

if os.path.exists(test_img_path):
    test_img = Image.open(test_img_path)
    test_img.show()
else:
    print("❌ SAMPLE IMAGE NOT FOUND:", test_img_path)

# --------------------------------------------------
# 3. BUILD TRAINING DATAFRAME
# --------------------------------------------------
def generate_paths(base_folder, index_start, index_end):
    """Generate paths including augmented forms like filename (2).jpg."""
    paths = []
    print(f"\n📁 Generating file paths in: {base_folder}")
    for i in tqdm(range(index_start, index_end)):
        paths.append(f"{base_folder}/{i}.jpg")
        for j in range(2, 11):
            paths.append(f"{base_folder}/{i} ({j}).jpg")
    return paths

# --- FAKE TRAIN ---
train_fake_paths = generate_paths(BASE_TRAIN_FAKE, 1000, 6000)
df_train_fake = pd.DataFrame({"path": train_fake_paths, "label": 0})

# --- REAL TRAIN ---
train_real_paths = []
train_real_paths += generate_paths(BASE_TRAIN_REAL, 0, 10)
train_real_paths += generate_paths(BASE_TRAIN_REAL, 10, 100)
train_real_paths += generate_paths(BASE_TRAIN_REAL, 100, 1000)
train_real_paths += generate_paths(BASE_TRAIN_REAL, 1000, 5000)

df_train_real = pd.DataFrame({"path": train_real_paths, "label": 1})

# --- COMBINE ---
df_train = pd.concat([df_train_fake, df_train_real], ignore_index=True)
print("Train dataset size:", df_train.shape)

# --------------------------------------------------
# 4. LOAD TRAIN IMAGES WITH LOADING BAR
# --------------------------------------------------
print("\n📦 Loading TRAIN images...")
X_train, y_train = [], []

for path, label in tqdm(zip(df_train["path"], df_train["label"]), total=len(df_train)):
    img = cv2.imread(path)
    if img is None:
        continue
    img = cv2.resize(img, (32, 32))
    X_train.append(img)
    y_train.append(label)

X_train = np.array(X_train) / 255.0
y_train = np.array(y_train)

print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)

# --------------------------------------------------
# 5. BUILD TEST DATAFRAME
# --------------------------------------------------
# --- FAKE TEST ---
test_fake_paths = generate_paths(BASE_TEST_FAKE, 0, 1000)
df_test_fake = pd.DataFrame({"path": test_fake_paths, "label": 0})

# --- REAL TEST ---
test_real_paths = []
test_real_paths += generate_paths(BASE_TEST_REAL, 0, 10)
test_real_paths += generate_paths(BASE_TEST_REAL, 10, 100)
test_real_paths += generate_paths(BASE_TEST_REAL, 100, 1000)

df_test_real = pd.DataFrame({"path": test_real_paths, "label": 1})

df_test = pd.concat([df_test_fake, df_test_real], ignore_index=True)
print("Test dataset size:", df_test.shape)

# --------------------------------------------------
# 6. LOAD TEST IMAGES WITH LOADING BAR
# --------------------------------------------------
print("\n📦 Loading TEST images...")
X_test, y_test = [], []

for path, label in tqdm(zip(df_test["path"], df_test["label"]), total=len(df_test)):
    img = cv2.imread(path)
    if img is None:
        continue
    img = cv2.resize(img, (32, 32))
    X_test.append(img)
    y_test.append(label)

X_test = np.array(X_test) / 255.0
y_test = np.array(y_test)

print("X_test shape:", X_test.shape)
print("y_test shape:", y_test.shape)

# --------------------------------------------------
# 7. BUILD CNN MODEL
# --------------------------------------------------
model = models.Sequential([
    layers.Conv2D(80, (3,3), activation='relu', input_shape=(32,32,3)),
    layers.MaxPool2D((2,2)),

    layers.Conv2D(40, (3,3), activation='relu'),
    layers.MaxPool2D((2,2)),

    layers.Conv2D(20, (3,3), activation='relu'),
    layers.MaxPool2D((2,2)),

    layers.Flatten(),
    layers.Dense(10, activation='relu'),
    layers.Dense(2, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# --------------------------------------------------
# 8. TRAIN MODEL
# --------------------------------------------------
print("\n🚀 Training model...\n")
model.fit(X_train, y_train, epochs=5)

# --------------------------------------------------
# 9. SAVE MODEL IN 4 FORMATS
# --------------------------------------------------
model.save("real_fake_model.keras")
print("Saved: real_fake_model.keras")

model.save("real_fake_model.h5")
print("Saved: real_fake_model.h5")

model.export("real_fake_model")
print("Saved: real_fake_model (TensorFlow SavedModel)")

converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
with open("real_fake_model.tflite", "wb") as f:
    f.write(tflite_model)

print("Saved: real_fake_model.tflite")
