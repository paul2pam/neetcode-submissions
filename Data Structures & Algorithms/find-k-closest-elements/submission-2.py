class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        l, r = 0, len(arr) - 1
        split = (l + r) // 2
        closest = abs(x - arr[split])

        while l <= r:
            mid = (l + r) // 2
            if abs(x - arr[mid]) < closest:
                closest = abs(x - arr[mid])
                split = mid

            if arr[mid] == x:
                split = mid
                break
            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        
        
        l, r = split - 1, split + 1
        #print(arr[split])
        res = [arr[split]]

        for i in range(k - 1):
            if l < 0:
                res.append(arr[r])
                r += 1
            elif r >= len(arr):
                res.append(arr[l])
                l -= 1
            elif abs(arr[l] - x) <= abs(arr[r] - x):
                res.append(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1
        
        return sorted(res)

                
