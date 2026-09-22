class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms=[[]]
        for n in nums:
            new_perms=[]
            for p in perms:
                for i in range(len(p)+1):
                    pcopy=p.copy()
                    pcopy.insert(i,n)
                    new_perms.append(pcopy)
            perms=new_perms
        return perms
        # if len(nums)==0:
        #     return [[]]

        # res=[]
        # perms=self.permute(nums[1:])
        # for p in perms:
        #     for i in range(len(p)+1):
        #         pcopy=p.copy()
        #         pcopy.insert(i,nums[0])
        #         res.append(pcopy)
        # return res
