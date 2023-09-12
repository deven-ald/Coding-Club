class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sCount1 = 0
        sCount2 = 0
        counter = 1
        newList = []
        answer = 0

        for x in nums:
            sCount2 = counter
            while counter < len(nums):
                y = nums[counter]
                answer = y + x
                if answer == target:
                    break
                counter = counter + 1
            if answer == target:
                    newList.append(sCount1)
                    newList.append(counter)
                    break
            sCount1 = sCount1 + 1
            counter = sCount2 + 1
            
        return newList