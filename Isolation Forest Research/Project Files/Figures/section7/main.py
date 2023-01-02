import numpy as np
import pandas as pd
import iforest
import anomaly_score_calculations
import sys

arg = sys.argv

def get_data(file_name):
    return pd.read_csv(file_name, header=None).to_numpy()


def score_dataset(data, forest, sample_size):
    scores = []
    for count, point in enumerate( data ):
        scores.append(anomaly_score_calculations.anomaly_score(point, forest, sample_size))
        if count % 1000 == 0:
            print("Evaluated to point: ", count)
    return scores


def main():

    data = get_data(arg[1])

    data_copy = np.copy(data) # copy into a new np array for shuffling
    np.random.shuffle(data_copy)  # shuffle so that sample method works

    num_trees = 100
    num_points = 256

    if(num_points*num_trees > data_copy.shape[0]):
        print("not enough points")
        exit()

    forest = iforest.iForest(data_copy, num_trees, num_points)
    print("\nForest constructed successfully\n")
    scores = np.array(score_dataset(data, forest, num_points))

    output_path = arg[2]
    np.savetxt(output_path, scores, delimiter=",")
    print("Run completed, results saved to: ", output_path)

main()
