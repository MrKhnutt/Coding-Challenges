def twoSum(nums: list[int], target: int) -> list[int]:
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in map:
                if i != map[target-nums[i]]:
                    return [i, map[target-nums[i]]]

if __name__ == "__main__":
    assert twoSum([-1,-2,-3,-4,-5], 8) == [2,4]
    assert twoSum([3,5,4,2], 6) == [2,3]