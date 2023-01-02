//	Isolation Forest
//	Ben Schneider
//	https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/icdm08b.pdf?q=isolation-forest
#include "Loader.h"
#include "IForest.h"
#include "Rnd.h"
int main() {

	//Data parameters
	const char* data_file = "column.csv";
	int data_dimension = 1;
	int num_data_points = 378;

	//model hyperparameter
	int sub_sample_size = 256;
	int num_trees = 100;

	double* instance = loader(data_file, data_dimension, num_data_points);
	IForest iforest(num_trees, sub_sample_size,data_dimension,num_data_points,instance);
}