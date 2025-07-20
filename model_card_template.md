# Model Card

## Model Details

Random Forest Classifier model using default hypterparameters from sklearn version 1.5.1.  

## Intended Use

For classifying incomes above and below 50k based on demographic and employment data.  

## Training Data

The training data is 80% of the data from a Census Income dataset extracted by Barry Becker from the 1994 Census database.  https://archive.ics.uci.edu/dataset/20/census+income

## Evaluation Data

The test data is 20% of the 32,561 rows in census.csv. 

## Metrics

Model evaluated precision (0.7419), recall (0.6384) and F1 (0.6863)

Metrics for specific slices can be viewed with slice_output.txt.  

## Ethical Considerations

The dataset is from 1994; likely reflecting societal bias for that time period.  

## Caveats and Recommendations

This model is is intended for the educational purpose of machnie learning only.