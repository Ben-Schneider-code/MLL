#pragma once
#include <iostream>
#include <sstream>
#include <string>
#include <fstream> 
class InstanceLoader
{
public:
	InstanceLoader(char* filename, int dim) {

		std::ifstream infile;
		std::string str = std::string(filename);

		infile.open(str, std::ifstream::in);
		std::string token;

		//IO Streams are the stupidest fucking thing
		while (std::getline(infile, token))
		{
			std::cout << token;
			//std::stringstream stream(token);
			//std::string subtoken;
			//std::getline(stream, subtoken, ' ');
		}


	}

};