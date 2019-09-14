---
title: "Automated Diagnosis of Epilepsy from EEG Signals using Ensemble Learning Approach"
collection: publications
excerpt: 'Entropy based features, higher order Spectra based features and non linear features are used for classification'
date: May 2017
venue: 'Elsevier'
paperurl: 'https://www.sciencedirect.com/science/article/abs/pii/S0167865517301691'
---
Note : I helped Dr. narasimhan for finishing this research paper.</br> 
EEG signals are non stationary, nonlinear and non Gaussian. In this paper, in order to tackle this problem, 
we have used three different methods for feature extraction namely wavelet based entropy (approximation entropy, sample entropy, permutation entropy), nonlinear features (Hurst exponent, Higuchi Fractal Dimension) and higher order spectra (mean, normalized entropy-1 and normalized entropy-2). 
Further multiclass classification using indirect approach with One vs One method is employed using heterogenous ensemble learning approach. Entropy features are used for classifying normal and interictal class using k-Nearest Neighbor. 
Higher Order Spectra features are used for classifying normal and ictal class using Support Vector Machine with Radial basis function as kernel and non linear features are used for classifying interictal and ictal class using Naive Bayes.
Final verdict is taken by meta classifier with meta learning algorithm Stacking Correspondence Analysis and Nearest Neighbor (SCANN). 
The proposed method surpasses the existing methods in literature in terms of sensitivity and specificity.


[Download paper here](http://hackin123.github.io/files/SecondPaper.pdf)

