#pragma once
#include <random>
#include <iostream>


static double rnd_double(double min, double max) {
	std::random_device r;
	// std::seed_seq ssq{r()};
	// and then passing it to the engine does the same
	std::default_random_engine eng{ r() };
	std::uniform_real_distribution<double> urd(min, max);
	return urd(eng);
}



static int rnd_int(int min, int max) {
		std::random_device r;
		// std::seed_seq ssq{r()};
		// and then passing it to the engine does the same
		std::default_random_engine eng{ r() };
		std::uniform_int_distribution<int> urd(min, max);
		return urd(eng);
}

static double get_split_point(std::vector<double*>* X, int feature) {

	double min = DBL_MAX;
	double max = -DBL_MAX;

	for (int i = 0; i < X->size(); i++) {
		if (X->at(i)[feature] > max)  max = X->at(i)[feature];
		if (X->at(i)[feature] < min)  min = X->at(i)[feature];
	}

	std::cout << "";
	return rnd_double(min, max);
}