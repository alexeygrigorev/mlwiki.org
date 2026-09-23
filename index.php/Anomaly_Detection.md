---
layout: default
permalink: /Anomaly_Detection
tags:
- machine-learning
- statistics
- data-mining
title: Anomaly Detection
---
## Anomaly Detection

Anomaly detection (also called outlier detection) is the task of identifying observations that deviate markedly from the majority of the data and do not conform to an expected pattern. The statistical notion of such observations is described in [Outliers](Outliers).

## Problem Setup

- **supervised** — both normal and anomalous examples are labeled; can be treated as an imbalanced classification problem
- **unsupervised** — no labels; anomalies are found as points that look different from the rest (most common setting)
- **semi-supervised** — learn a model of normal behavior from clean data, then flag deviations from it

## Approaches

- **statistical** — flag points that are unlikely under a model, e.g. more than 3 standard deviations from the mean of a [Normal Distribution](Normal_Distribution), or outside the IQR fences; see [Outliers](Outliers)
- **density- and distance-based** — points in low-density regions or far from their neighbors are anomalous, e.g. Local Outlier Factor (LOF) or k-NN distance
- **clustering-based** — cluster the data first; small clusters and noise points (e.g. in [DBSCAN](DBSCAN)) are candidates for anomalies; see [Cluster Analysis](Cluster_Analysis)
- **classification-based** — train a model to separate normal from abnormal, e.g. one-class [Kernel Methods](Kernel_Methods) such as one-class SVM, or isolation forests that isolate anomalies with few random splits

## Applications

- fraud detection in financial transactions
- intrusion detection in computer networks
- fault detection in industrial systems
- [Data Cleaning](Data_Cleaning) — detecting noise and bad records before analysis; part of the data preparation stage in [CRISP-DM](CRISP-DM)

## Evaluation

When ground-truth labels for anomalies are available, detection quality is typically evaluated with precision/recall curves and ROC analysis — see [ROC Analysis](ROC_Analysis).

## See Also

- [Outliers](Outliers)
- [DBSCAN](DBSCAN)
