# cebd1160_project_template
Instructions and template for final projects.

| Name | Date |
|:-------|:---------------|
|Yao Chen | june.14.2019|

-----

### Resources
Your repository should include the following:

- Python script for your analysis
- Results figure/saved file
- Dockerfile for your experiment
- runtime-instructions in a file named RUNME.md

-----

## Research Question

1 sentence description of your research question.

i want to find corrolation and make prediction between variables

### Abstract

4 sentence longer explanation about your research question. Include:

- opportunity (what data do we have)

   boston.housing data. 
- challenge (what is the "problem" we could solve with this dataset)

  how can i predict housing price with some variables?
- action (how will we try to solve this problem/answer this question)
  find corrolation between price and other variables, build model to make prediction through those variables.
  
- resolution (what did we end up producing)
  an model that can predict housing price by fitting some needed variables.
### Introduction

We will take the Housing dataset which contains information about different houses in Boston. 
This data was originally a part of UCI Machine Learning Repository and has been removed now. 
We can also access this data from the scikit-learn library. There are 506 samples and 13 feature variables in this dataset. 
The objective is to predict the value of prices of the house using the given features.


### Methods

My method is come from internet. Basiclly it is loading the data from sklearn. make housing price as target.
Then i need to find the corrolation between price and other variables. Find the most important variables that effect
the housing price. Then build model. Make prediction through Linear Regression. I choose this method because it is
easy to understand.


### Results

<img src="check_corrolation.png">

- At least 1 figure
- At least 1 "value" that summarizes either your data or the "performance" of your method
- A short explanation of both of the above

### Discussion
So i find LSTAT and RM have strong corrolation with housing price through heating map. And find that housing price 
going up with more rooms, also will going up with less lower-income population.When i build the model, trying to
 predict the value of house, the accurate is around 64% and prediction error is 5.5 in average. So the result is not good
 enough. I think i need to try to add more variables into model so i can improve the accurate of prediction.


### References
All of the links
resouce:https://towardsdatascience.com/linear-regression-on-boston-housing-dataset-f409b7e4a155
https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html
https://medium.com/@haydar_ai/learning-data-science-day-9-linear-regression-on-boston-housing-dataset-cd62a80775ef
-------
