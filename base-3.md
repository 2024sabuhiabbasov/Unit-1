# Calculating in base 3

You can see the code I have written for calculating decimal numbers in base 3 in the C++ programming language. 

```.cpp
#include <bits/stdc++.h>

using namespace std;
vector <int> arr;
int r;
void ternary(int n){
    string s;
}

int main()
{
    int n, cnt = 0;
    cin >> n;
    if(n == 0){
        cout << 0;
        exit;
    }
    while(n > 0){
        r = n % 3;
        arr.push_back(r);
        n /= 3;
    }
    int s = arr.size();
    for(int i = s - 1; i >= 0; i--){
        cout << arr[i];
    }
    return 0;
}

```

**Test cases**
| **Input** | **Output** |
|-----------|------------|
| 42        | 1120       |
| 34        | 1021       |
| 25        | 0221       |
| 56        | 2022       |
