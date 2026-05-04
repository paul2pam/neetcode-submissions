class Solution {
public:
    bool isPalindrome(string s) {
        string str;
        for (char c : s) {
            if (isalpha(c)) str += tolower(c);
            if (isdigit(c)) str += c;
        }
        int i = 0, n = str.length() - 1;
        while (i < str.length() / 2) {
            if (str[i] != str[n]) return false;
            i++;
            n--;
        }
        return true;
    }
};
