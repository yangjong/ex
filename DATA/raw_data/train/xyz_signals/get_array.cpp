#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

void load_train_file(const char *data_file)
{
	vector< vector<float> > data;
	ifstream file;
	file.open(data_file);

	while (!file.eof()) {
		for (int i = 0; i < 70; i++) {
			for (int j = 0; j < 30; j++) {
				file >> data[i][j];
			}
		}
	}

	for (int i = 0; i < 70; i++) {
		for (int j = 0; j < 30; j++) {
			 cout << data[i][j]  << endl;
		}
		cout << "\n" << endl;
	}



}

int main() {
	load_train_file("sensor_xacc1_train1.txt");
	return 0;


}

/*
float load_train_file(char * data) {
	int i, j, n;
	float train_data[MAX_R][MAX_C];
	FILE *fp = NULL;
	fp = fopen(data, "r");
	if (fp == NULL) { printf("file access failed \n"); return 0; }
	for (i = 0; i < MAX_R; i++)
		for (j = 0; j < MAX_C; j++)
			fscanf(fp, "%d,", &train_data[i][j]);
	for (i = 0; i < MAX_R; i++) {
		for (j = 0; j < MAX_C; j++)
			printf("%d ", train_data[i][j]);
		printf("\n");
	}
	return 
}
*/