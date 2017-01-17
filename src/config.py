# -*- coding: utf-8 -*-
import os
#%%
BOXCARS_DATASET_ROOT = "/mnt/matylda1/isochor/Datasets/BoxCars116k/"
BOXCARS_IMAGES_ROOT = os.path.join(BOXCARS_DATASET_ROOT, "images")
BOXCARS_DATASET = os.path.join(BOXCARS_DATASET_ROOT, "dataset.pkl")
BOXCARS_ATLAS = os.path.join(BOXCARS_DATASET_ROOT, "atlas.pkl")
BOXCARS_CLASSIFICATION_SPLITS = os.path.join(BOXCARS_DATASET_ROOT, "classification_splits.pkl")

#%%
BATCH_SIZE = 8
LEARNING_RATE = 0.0025

#%%
OUTPUT_DATA_DIR = "data"
OUTPUT_TENSORBOARD_DIR = os.path.join(OUTPUT_DATA_DIR, "tensorboard")
OUTPUT_SNAPSHOTS_DIR = os.path.join(OUTPUT_DATA_DIR, "snapshots")
OUTPUT_FINAL_MODEL = os.path.join(OUTPUT_DATA_DIR, "final_model.h5")
OUTPUT_FINAL_WEIGHTS = os.path.join(OUTPUT_DATA_DIR, "final_model_weights.h5")