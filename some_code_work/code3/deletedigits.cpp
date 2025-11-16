#include <bits/stdc++.h>
using namespace std;

/**
 * 删数问题 - 删除s个数字使剩下的数字最小
 * 使用贪心算法，每次删除第一个比后面数字大的数字
 */
string deleteDigits(string n, int s) {
    string result = "";
    
    // 遍历每个数字
    for (char digit : n) {
        // 当还能删除数字，且结果字符串不为空，且当前数字比结果字符串的最后一个数字小时
        while (s > 0 && !result.empty() && digit < result.back()) {
            result.pop_back();  // 删除最后一个数字
            s--;  // 减少待删除数量
        }
        result.push_back(digit);  // 将当前数字加入结果
    }
    
    // 如果还有需要删除的数字（数字已经是非递减顺序），从末尾删除
    result.resize(result.length() - s);
    
    // 删除前导零
    int start = 0;
    while (start < result.length() && result[start] == '0') {
        start++;
    }
    
    // 如果所有数字都被删除了，返回"0"
    if (start == result.length()) {
        return "0";
    }
    
    return result.substr(start);
}

int main() {
    string n;
    int s;
    
    // 输入说明
    cout << "=== 删数问题 ===" << endl;
    cout << "问题描述：删除一个高精度正整数中的s个数字，使剩下的数字最小" << endl;
    cout << endl;
    cout << "输入格式：" << endl;
    cout << "第一行：高精度正整数 n (有效位数 ≤ 240)" << endl;
    cout << "第二行：要删除的数字个数 s" << endl;
    cout << endl;
    cout << "请输入数据：" << endl;
    
    // 读取输入
    cout << "n = ";
    cin >> n;
    cout << "s = ";
    cin >> s;
    
    // 输入验证
    if (s < 0 || s > n.length()) {
        cout << "错误：s 应该在 0 到 " << n.length() << " 之间" << endl;
        return 1;
    }
    
    // 计算并输出结果
    string result = deleteDigits(n, s);
    
    cout << endl;
    cout << "=== 计算结果 ===" << endl;
    cout << "原始数字: " << n << endl;
    cout << "删除个数: " << s << endl;
    cout << "最小结果: " << result << endl;
    
    return 0;
}