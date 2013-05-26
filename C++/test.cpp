#include <iostream>
#include <vector>
#include <string>

using std::cout;

int main(int argc, char *argv[])
{
	cout << "test C" << std::endl;
	std::vector<std::string> *vec = new std::vector<std::string>();
	if (!vec->empty()) {
		cout << "vec" << std::endl;
	} else {
		cout << "no vec" << std::endl;
	}
	return 0;
}
