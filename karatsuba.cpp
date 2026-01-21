#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string>
#include <vector>
#include <utility>
using namespace std; 
   
string strip(string s) {
    while (s.size() > 1 && s[0] == '0')
        s.erase(0, 1);
    return s;
}

string add(string a, string b) {
    string res = "";
    int carry = 0;
    int i = a.size() - 1, j = b.size() - 1;

    while (i >= 0 || j >= 0 || carry) {
        int sum = carry;
        if (i >= 0) sum += a[i--] - '0';
        if (j >= 0) sum += b[j--] - '0';
        res = char(sum % 10 + '0') + res;
        carry = sum / 10;
    }
    return strip(res);
}

string subtract(string a, string b) { // a >= b
    string res = "";
    int borrow = 0;
    int i = a.size() - 1, j = b.size() - 1;

    while (i >= 0) {
        int diff = (a[i] - '0') - borrow;
        if (j >= 0) diff -= (b[j] - '0');

        if (diff < 0) {
            diff += 10;
            borrow = 1;
        } else borrow = 0;

        res = char(diff + '0') + res;
        i--; j--;
    }
    return strip(res);
}

string shift(string s, int zeros) {
    return s + string(zeros, '0');
}

string karatsuba(string x, string y){
    x = strip(x);
    y = strip(y);
    if (x.size() == 1 || y.size() == 1){
        return to_string(stoll(x)*stoll(y));
    }
    int n = max(x.size(), y.size());
    if (n % 2 != 0){
        n++;
    }
    while (x.size() < n){
        x = "0" + x;
    }
    while (y.size() < n){
        y = "0" + y;
    }
    int m = n/2;
    string a = x.substr(0,m);
    string b = x.substr(m);
    string c = y.substr(0,m);
    string d = y.substr(m);
    string ac = karatsuba(a,c);
    string bd = karatsuba(b,d);
    string abcd = karatsuba(add(a,b), add(c,d));
    string ad_plus_bc = subtract(subtract(abcd, ac), bd);
    return strip(add(add(shift(ac, 2*m), shift(ad_plus_bc, m)), bd));
}
int main(){
    string x ;
    string y ;
    cout << "Enter x:\n";
    cin >> x;
    cout << "Enter y:\n";
    cin >> y;
    string ans = karatsuba(x,y);
    cout << ans << "\n";

}