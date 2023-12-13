"""Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets poisoned for a exactly duration seconds.
 More formally, an attack at second t will mean Ashe is poisoned during the inclusive time interval [t, t + duration - 1].
 If Teemo attacks again before the poison effect ends, the timer for it is reset, and the poison effect will end duration seconds after the new attack.

You are given a non-decreasing integer array timeSeries, where timeSeries[i] denotes that Teemo attacks Ashe at second timeSeries[i], 
and an integer duration.

Return the total number of seconds that Ashe is poisoned.
"""
class Solution: # non decreasing order
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        if not timeSeries:
            return 0    
        totalDuration = 0

        for i in range(1, len(timeSeries)):
            totalDuration += min(duration, timeSeries[i] - timeSeries[i - 1])

        totalDuration += duration
        return totalDuration
    

timeSeries = [1,4]
duration = 2
print(Solution().findPoisonedDuration(timeSeries, duration))
print("\n")

timeSeries = [1,2]
duration = 2
print(Solution().findPoisonedDuration(timeSeries, duration))