class Solution(object):
    def carPooling(self, trips, capacity):
        slots = [0] * 1000
        for trip in trips:
            num = trip[0]
            frm = trip[1]
            to = trip[2]
            for i in range(frm,to):
                slots[i] += num
            # slots[frm:to] += num
        if max(slots) > capacity:
            return False
        return True

solution = Solution()
print(solution.carPooling(trips = [[2,1,5],[3,3,7]], capacity = 4))
print(solution.carPooling(trips = [[2,1,5],[3,3,7]], capacity = 5))