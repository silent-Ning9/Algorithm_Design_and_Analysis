 #include <bits/stdc++.h>
 using namespace std;

 // 桶结构体：用于存储每个桶的状态
struct Bucket {
    bool flag = false;
    double mn = 2e18;
    double mx = -2e18;
};

int main(int argc, char *argv[]) {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n;
    cin >> n;

    vector<double> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    // 处理边界情况：元素不足2个时直接返回0
    if (n < 2) {
        cout << fixed << setprecision(6) << 0.0 << endl;
        return 0;
    }

    // 计算全局最小值和最大值
    double mn = 2e18, mx = -2e18;
    for (int i = 0; i < n; i++) {
        mn = min(mn, a[i]);
        mx = max(mx, a[i]);
    }

    // 所有元素相等的特殊情况处理
    if (mn == mx) {
        cout << fixed << setprecision(6) << 0.0 << endl;
        return 0;
    }

    // 计算桶参数（基于鸽巢原理）
    double bucket_size = (mx - mn) / (n - 1); // 每个桶的区间长度
    int bucket_count = n - 1;                 // 桶的数量
    vector<Bucket> buckets(bucket_count);

    // 将元素分配到对应的桶中
    for (int i = 0; i < n; i++) {
        int bucket_idx;
        if (a[i] == mx) {
            // 最大值特殊处理到最后一个桶（防止计算索引越界）
            bucket_idx = bucket_count - 1;
        } else {
            // 计算元素应属的桶索引
            bucket_idx = floor((a[i] - mn) / bucket_size);
        }
        
        // 更新桶的极值信息
        buckets[bucket_idx].flag = true;
        buckets[bucket_idx].mn = min(buckets[bucket_idx].mn, a[i]);
        buckets[bucket_idx].mx = max(buckets[bucket_idx].mx, a[i]);
    }

     // 寻找最大间距
    double ans = 0;
    double prev = mn;

    for(int i = 0; i < bucket_count; i++) {
        if (buckets[i].flag) {
            prev = buckets[i].mx;
            break;
        }
    }

    // 遍历所有桶，计算相邻非空桶间距
    for (int i = 1; i < bucket_count; i++) {
        if (buckets[i].flag) {
            double res = buckets[i].mn - prev;
            ans = max(ans, res);
            prev = buckets[i].mx;
        }
    }

    // 输出结果
    cout << fixed << setprecision(6) << ans << endl;

    return 0;
}