class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity):
            running_sum = 0
            total_days = 1
            for weight in weights:
                if weight + running_sum > capacity:
                    running_sum = 0
                    total_days += 1
                running_sum += weight
            return total_days
        
        l, r = max(weights), sum(weights)

        while l <= r:
            mid = (l + r) // 2
            if can_ship(mid) <= days:
                r = mid - 1
            else:
                l = mid + 1

        return l


            