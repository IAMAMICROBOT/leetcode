class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        memo = {}
        result = self.findCheapestPriceHelper(n, flights, src, dst, k, memo)
        return result if result != float('inf') else -1

    def findCheapestPriceHelper(self, n: int, flights: List[List[int]], src: int, dst: int, k: int, memo: dict) -> int:
        if src == dst:
            return 0
        if k < 0:
            return float('inf')

        key = (src, dst, k)
        if key in memo:
            return memo[key]

        minCost = float('inf')
        for fr, to, pr in flights:
            if fr == src:
                price_to_dst = self.findCheapestPriceHelper(n, flights, to, dst, k - 1, memo)
                if price_to_dst != float('inf'):
                    minCost = min(minCost, pr + price_to_dst)

        memo[key] = minCost
        return minCost
