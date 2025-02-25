#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

int factorial(int n) {
    long long result = 1;
    for (int i = 2; i <= n; ++i) {
        result = (result * i) % MOD;
    }
    return result;
}

int main() {
    int N;
    cin >> N;

    vector<int> C(2 * N);
    for (int i = 0; i < 2 * N; ++i) {
        cin >> C[i];
    }

    vector<int> R(N);
    for (int i = 0; i < N; ++i) {
        cin >> R[i];
    }

    vector<int> B(N);
    for (int i = 0; i < N; ++i) {
        cin >> B[i];
    }

    // Step 1: Identify the used numbers from C and B
    set<int> used;
    for (int i = 0; i < 2 * N; ++i) {
        if (C[i] != -1) {
            used.insert(C[i]);
        }
    }
    for (int i = 0; i < N; ++i) {
        used.insert(B[i]);
    }

    // Step 2: Identify missing numbers
    vector<int> missing;
    for (int i = 1; i <= 2 * N; ++i) {
        if (used.find(i) == used.end()) {
            missing.push_back(i);
        }
    }

    // Step 3: Check the relationships based on R and B
    bool valid = true;
    vector<pair<int, int>> unknownPairs; // To store pairs of unknowns
    for (int i = 0; i < N; ++i) {
        int a1 = C[2 * i], a2 = C[2 * i + 1];

        // If both are unknown, we add them to unknownPairs
        if (a1 == -1 && a2 == -1) {
            unknownPairs.push_back({i, i}); // Mark this index
            continue;
        }

        // Assign known values if one is unknown
        if (a1 == -1) {
            a1 = (R[i] == 0) ? B[i] : -1; // Min case
        } else if (a2 == -1) {
            a2 = (R[i] == 0) ? B[i] : -1; // Min case
        }

        // Now check if the known values satisfy the conditions
        if (R[i] == 0) { // min case
            if (min(a1, a2) != B[i]) {
                valid = false;
                break;
            }
        } else { // max case
            if (max(a1, a2) != B[i]) {
                valid = false;
                break;
            }
        }
    }

    // Handle unknown pairs separately
    if (valid) {
        int numMissing = missing.size();
        int count = 1;

        for (const auto& pair : unknownPairs) {
            int index = pair.first;
            if (R[index] == 0) {
                // Min case: both must be the same value
                if (numMissing < 1) {
                    valid = false; // No missing numbers to fill
                    break;
                } else {
                    // Choose one missing number for both unknowns
                    count = (count * numMissing) % MOD;
                    numMissing--; // Reduce the count of missing for the next pair
                }
            } else {
                // Max case: they must be different
                if (numMissing < 2) {
                    valid = false; // Not enough missing numbers
                    break;
                } else {
                    count = (count * numMissing * (numMissing - 1)) % MOD; // Choose two distinct numbers
                    numMissing -= 2; // Reduce for the next pair
                }
            }
        }

        // Step 4: If valid, output the count
        if (valid) {
            cout << count << endl;
        } else {
            cout << 0 << endl;
        }
    } else {
        cout << 0 << endl;
    }

    return 0;
}
