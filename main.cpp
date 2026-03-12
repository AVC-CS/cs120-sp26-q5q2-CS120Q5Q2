#include <iostream>
using namespace std;

int main()
{
    int N, M;

    cout << "Enter your base number: ";
    cin >> N;
    cout << "Enter your exponent: ";
    cin >> M;

    cout << N << " to power number: ";

    // TODO
    int result = 1;
    for (int i = 0; i <= M; i++) {
        if (i > 0) cout << ", ";
        cout << result;
        result *= N;
    }
    // END TODO

    cout << endl;

    return 0;
}
