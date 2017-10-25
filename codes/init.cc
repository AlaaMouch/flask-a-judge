#include <iostream>

using namespace std;

int main(){
	int n, sum = 0, t;
	cin >> n;
	for (int i = 0; i < n; ++i){
		if (i) cout << " + ";
		cin >> t;
		cout << t;
		sum += t;
	}
	cout << " = " << sum << endl;
	return 0;
}
