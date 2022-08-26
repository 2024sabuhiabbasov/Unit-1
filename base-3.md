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
    int i, n, s = arr.size();
    cin >> n;
    int cnt = 0;
    if(n == 0){
        cout << 0;
        exit;
    }
    while(n > 0){
        r = n % 3;
        arr.push_back(r);
        n /= 3;
    }
    /* for(i = 0; i < s; i++){
        cout << arr[i];
    } */
    cout << arr[3] << arr[2] << arr[1] << arr[0];
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
