// Name : Day 21: Generics
// Link : https://www.hackerrank.com/challenges/30-generics/problem
// Difficulty : Easy
// Programming Language : C++

#include <iostream>
#include <vector>
#include <string>

using namespace std;

void printArray(vector<auto> a){for(auto i:a)cout<<i<<endl;}

int main() {
	int n;
	
	cin >> n;
	vector<int> int_vector(n);
	for (int i = 0; i < n; i++) {
		int value;
		cin >> value;
		int_vector[i] = value;
	}
	
	cin >> n;
	vector<string> string_vector(n);
	for (int i = 0; i < n; i++) {
		string value;
		cin >> value;
		string_vector[i] = value;
	}

	printArray<int>(int_vector);
	printArray<string>(string_vector);

	return 0;
}