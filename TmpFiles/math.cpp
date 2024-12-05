#include <bits/stdc++.h>
#include <cmath>
using namespace std;

double a(int n) {
    if (n % 2 == 0) return -1/sqrt(n+1);
    else return 1/sqrt(n+1);
}

int main(int argc, char *argv[]) {
    double P = 1;
    int N = stoi(argv[1]);
    for (int n = 1; n < N; n++) {
        P *= a(n);
    }
    cout << P << endl;
    return 0;
}
