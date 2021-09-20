# CS: GO Regression Project: Predicting Player Ratings

## Project Description
 - This purpose of this project is to create a Regression model that predicts the player ratings of CS: GO professional players in the esports scene.
 - Project created using the data science pipeline (Acquisition, Preparation, Exploration, Analysis & Statistical Testing, and finally Modeling and Evaluation)

## Project Goals
 - Create a Final Jupyter Notebook that reads like a report and follows the data science pipeline
 - In the Jupyter Notebook Create a regression model that performs bettern than our baseline mean RMSE and R-squared scores
 - Create Function Files to help peers execute project reproduction
 - Create a baseline Machine Learning Model that creates a baseline for easy and equal player prediction.

 ## Deliverables
 - Final Jupyter Notebook
 - Function Files for reproduction
 - Detailed Readme

 ## Executive Summary
 - The purpose of this notebook is create a regression model that predicts professional counter strike player ratings form a dataset provided from kaggle.com
 - Target variable: player_rating
 - Best features determined: kd, kd_diff
 - In conclusion, the end result and real world application is provide a baseline for counter strike esports to create an efficient and equal rating system for all professional players in the Counter Strike GO esport.
 - R^2 value of 0.964
 - RMSE: 0.014

 ## Hypothesis
 - Kill death ratio will most likely be the biggest factor in determining player ratings within the dataset


## Findings & Takeaways
 - The features that I hypothesized (kd, kd_diff) had the strongest correlation in relation to our target variable (player_rating)
 - Our OLS: Linear Regression Model
 - Our model performed extremely and outperformed the baseline.
 - With more time I'd like to use feature engineering to help make the model more accurate in predicting player ratings

 # The Pipeline

 ## Planninng

 With some domain knowledge I want to test some regression models using the features hypothesized above: kill death ratio and kill death difference. It is my belief that these will have the strongest correlation with our target: player_rating

### Features Used in Modeling
 - kd
 - kd_diff

 ### Model Performance
 - Using the mean for baseline and not the median

| Model                            | RMSE Train Score | RMSE Validate Score | R-squared |
|----------------------------------|------------------|---------------------|-----------|
| Baseline                         | 0.0748           | 0.0773              | 0         |
| LinearRegression                 | 0.0146           | 0.0135              | 0.9695    |
| LassoLars                        | 0.0146           | 0.0773              | 0         |
| TweedieRegressor                 | 0.0146           | 0.1349              | 0.9695    |
| PolynomialRegression (2 degrees) | 0.0146           | 0.1349              | 0.9695    |

### Test on OLS: Linear Regression
 - RMSE of test: 0.1414
 - R-squared of test: 0.9648

 ### This is better than our baseline

 ## Project Recreation
 - Use the functions in the .py files and follow the pipeline flow of the notebook
 - Link to dataset: https://www.kaggle.com/patrasaurabh/csgo-player-and-team-stats/version/1

