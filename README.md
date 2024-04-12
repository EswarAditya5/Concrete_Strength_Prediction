# Concrete_Strength_Prediction

## Abstract:
A Cement and Concrete Research company has gathered raw data regarding the concrete mixture and wants to analyze it. Concrete is the most important material in civil engineering. The concrete compressive strength is a highly nonlinear function of age and ingredients. These ingredients include cement, blast furnace slag, fly ash, water, superplasticizer, coarse aggregate, and fine aggregate. You are hired as a DL Engineer to help the company predict the concrete strength based on the data that they have gathered from a laboratory.

## Problem Statement:
Predict the actual concrete compressive strength (MPa) for a given mixture under a specific age (days) based on the data provided using ANN.

## Data Description:
|Column|	Description|
|--|--|
|Cement|	kg in a m3 mixture|
|Blast Furnace Slag	|kg in a m3 mixture|
|Fly Ash	| kg in a m3 mixture|
|Water|	kg in a m3 mixture|
|Superplasticizer|	kg in a m3 mixture|
|Coarse Aggregate	|  kg in a m3 mixture|
|Fine Aggregate|	  kg in a m3 mixture|
|Age|	  Day (1~365)|
|Concrete compressive strength	|MPa (target variable)|

## Scope:
-	Exploratory data analysis
-	Data Pre-processing
-	Training ANN model for prediction
-	Tuning the model to improve the performance

## Required Packages:
- Python == 3.11
- tensorflow
- streamlit
- pandas
- numpy
- matplotlib
- seaborn
- pyplot
