# Running Implementations

### To run the implementations:  

`python main.py input.csv out.csv`  
input.csv is the file of the input data.  
out.csv

To change the number of tree estimators used change the `num_trees` variable in main.py

To change the samples to construct a tree used change the `num_points` variable in main.py  
  
Note: `num_trees * num_points <= dataset size`

### To change model hyperparameters:    
  

*w* for the feature bias method: adjust the `distribution` variable in forest.py  

*α* for the middle method: adjust the `α` variable in forest.py
