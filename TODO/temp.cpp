#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

const int N = 100010;
struct Range {
    int l,r;
    bool operator < (const Range& W) const {
        return l<W.l;
    }
}range[N];

int main() {
    int n;
    cin>>n;
    for(int i=0; i<n; ++i) {
        int a,b;
        cin>>a>>b;
        range[i] = {a, b};
    }
    sort(range, range+n);
    // 这里使用小根堆保存当前每个分组中的最大右端点
    priority_queue<int, vector<int>, greater<int>> q;
    int res = 0;
    for(int i=0; i<n; ++i) {
        if(q.empty() || range[i].l <= q.top()) {
            q.push(range[i].r);
            res++;

        }
        else if(range[i].l > q.top()) {
            q.pop();
            q.push(range[i].r);
        }
    }
    cout<<res;
    return 0;
}