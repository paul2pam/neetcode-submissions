class Solution {
public:

    string encode(vector<string>& strs) {
        string to_return;
        for (string str : strs) {
            to_return += to_string(str.length());
            to_return += '#';
            to_return += str;
        }
        return to_return;
    }

    vector<string> decode(string s) {
        vector<string> to_return;
        int i = 0;
        while (i < s.size()) {
            int j = i;
            while (s[j] != '#') {
                j++;
            }
            int len = stoi(s.substr(i, j - i));
            i = j + 1;
            j = i + len;
            to_return.push_back(s.substr(i, len));
            i = j;
        }

        return to_return;
    }
};
