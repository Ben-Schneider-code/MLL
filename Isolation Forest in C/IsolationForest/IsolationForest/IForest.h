#pragma once
#include "Rnd.h"
#include <math.h>
#include <vector>

struct ITree {
	int feature; //not needed
	double split; //not needed
	int size = -1;
	ITree* left = nullptr;
	ITree* right = nullptr;
};

class IForest {
public:
	IForest(int num_trees, int sub_sample_size, int data_dimension, int num_data_points, double* instance) {
		int max_depth = ceil(log2(sub_sample_size));
		tree_array = new ITree*[num_trees];

		for (int i = 0; i < num_trees; i++) {
			std::vector<double*>* X = rnd_sample(sub_sample_size, data_dimension, instance, num_data_points);
			tree_array[i] = gen_itree(0, X, max_depth, data_dimension);
		}

	}
private:

	ITree* gen_itree(int curr_depth, std::vector<double*>* X, int max_depth, int data_dimension) {
		ITree* return_node = new ITree();

		//base case
		if (curr_depth >= max_depth || X->size() == 1) { 
			return_node->size = X->size();
		}
		//recursive case
		else {
			int feature = rnd_int(0, data_dimension - 1);
			std::vector<double*>* left_data = new std::vector<double*>();
			std::vector<double*>* right_data = new std::vector<double*>();
			// split point, split data,double recursive call, populate return node

			double split_point = get_split_point(X, feature);

			for (int i = 0; i < X->size(); i++) {
				if (X->at(i)[feature] < split_point)
					left_data->push_back(X->at(i));
				else if ((X->at(i)[feature] > split_point))
					right_data->push_back(X->at(i));
				else if(left_data->size() < right_data->size())
					left_data->push_back(X->at(i));
				else
					right_data->push_back(X->at(i));
			}
			
			return_node->feature = feature; //not needed
			return_node->split = split_point; //not needed
			if (left_data->size() == 0 || right_data->size() == 0)
				std::cout << "";


			return_node->left = gen_itree(curr_depth + 1, left_data, max_depth, data_dimension);
			return_node->left = gen_itree(curr_depth + 1, right_data, max_depth, data_dimension);
		}
		delete(X);
		return return_node;
	};


	//this method does replacement sampling, the paper doesn't
	std::vector<double*>* rnd_sample(int sub_sample_size, int data_dimension, double* instance, int num_points) {
		std::vector<double*>* sample = new std::vector<double*>();

		for (int i = 0; i < sub_sample_size; i++) {
			int offset = rnd_int(0, num_points - 1) * data_dimension;
			sample->push_back(instance + offset);
		}
		return sample;
	}

	ITree** tree_array;
};