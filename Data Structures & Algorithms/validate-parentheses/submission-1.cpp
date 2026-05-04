class Solution {
public:
    

    bool isValid(string s) {
        map<char, char> m = {
        {'(' , ')'},
        {'{' , '}'},
        {'[' , ']'}
    };
        deque<char> dq;
        for (char c : s) {
            if (c == '(' || c == '{' || c == '[') {
                dq.push_front(c);
            } else if (c == m[dq.front()]) {
                dq.pop_front();
            } else return false;
        }
        return dq.empty();
    }
};
