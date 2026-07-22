class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        l = 0
        res = []
        def generate(s, l, r):
            
            if r == n:
                res.append(s)
                #print(s, l, r)
                return

            if l < n:
                sl = s + "("
                #print(f"generating {s, l +1, r}")
                generate(sl, l + 1, r)
                
            if r < l: 
                sr = s + ")"
                generate(sr, l, r + 1)
        
        generate("", 0, 0)
        return res