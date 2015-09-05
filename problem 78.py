class Solution(object):
    def subsets(self, nums):
        nums.sort()
        result = []
        for i in xrange(len(nums)):
            result.append([i])
        toreturn = result
        for cnt in xrange(2,len(nums)):
            temp = []
            for i in xrange(len(result)):
                for j in xrange(result[i][-1]+1,len(nums)):
                    temp.append(result[i]+[j])
            result = temp
            toreturn += result
        for i in xrange(len(toreturn)):
            for j in xrange(len(toreturn[i])):
                toreturn[i][j] = nums[toreturn[i][j]]
        toreturn.append([])
        if len(nums) > 1:
            toreturn.append(nums)
        return toreturn

a = Solution()
print a.subsets([0])
