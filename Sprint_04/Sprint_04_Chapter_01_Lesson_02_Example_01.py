# Sprint 4: Statisttical Data Analysis
# Chapter 1: Descriptive Statistics
# Lesson 2: Frequency Histograms for Continuous Variablees

import pandas as pd

data = pd.Series([11, 20, 22, 31, 32, 33, 41, 42, 43, 44, 51, 52, 53, 54, 55, 61, 62, 63, 64, 65, 66, 71, 72, 73, 74, 75, 76, 77, 81, 82, 83, 84, 85, 86, 87, 88, 91, 92, 93, 94, 95, 96, 97, 98, 99])

data.hist(bins=4, alpha=0.5)  # builds a histogram with four bins

data.hist(bins=[11, 20, 30, 40, 50, 60, 70, 80, 90, 99], alpha=0.7)  # builds a histogram with nine bins, the boundaries for which are listed, where the alpha argument gives us an opaque graph
