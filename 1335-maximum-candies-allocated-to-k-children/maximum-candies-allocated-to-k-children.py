class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0 

        left, right = 1, max(candies) 
        best = 0

        def canDistribute(mid: int) -> bool:
            count = sum(c // mid for c in candies)
            return count >= k

        while left <= right:
            mid = (left + right) // 2
            if canDistribute(mid):
                best = mid  # Try to maximize
                left = mid + 1
            else:
                right = mid - 1

        return best

                    

                
        