#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Creator:        Qin Liu (https://github.com/qinliu0901)
    Programm name:  Financial data fraud detection
    Kaggle url:     https://www.kaggle.com/ntnu-testimon/paysim1
    Data set download: https://www.kaggle.com/ntnu-testimon/paysim1/downloads/paysim1.zip
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
import zipfile
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc


if __name__ == '__main__':
    run_main()