"""
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend

"""


class Solution(object):
    result = {}
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n in self.result:
            return self.result[n]
        if n <= 3:
            return True


        self.his_turn(n - 1)  # I take 1
        self.his_turn(n - 2)  # I take 2
        self.his_turn(n - 3)  # I take 3
        self.result[n] = win
        return self.result[n]

    def his_turn(self, n):
        if n <= 3:
            return False
        self.canWinNim(n - 1)
        self.canWinNim(n - 2)
        self.canWinNim(n - 2)


sol = Solution()
print(sol.canWinNim(9))
