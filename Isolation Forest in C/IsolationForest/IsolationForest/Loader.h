#pragma once
#include <iostream>
#include <sstream>
#include <string>
#include <fstream> 
#include <stdlib.h>

//IO Streams are the stupidest fucking thing
double* loader(const char* filename, int dim, int numPoints) {
		double *instance = new double[dim * numPoints];
		std::ifstream infile;
		std::string str = std::string(filename);

		infile.open(str, std::ifstream::in);
		std::string token;
		int datapoint = 0;
		
		while (std::getline(infile, token))
		{
			int feature = 0;
			std::stringstream ss(token);
			std::string temp_str;

			while (getline(ss, temp_str, ',')) {
				instance[datapoint * dim + feature] = std::stod(temp_str);
				feature++;
			}
			datapoint++;
		}
		return instance;
};