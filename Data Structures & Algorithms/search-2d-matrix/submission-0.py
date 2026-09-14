class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        cols=len(matrix[0])
        l=0
        r=len(matrix)*cols-1
        while l<=r:
            mid=(l+r)//2
            if target==matrix[mid//cols][mid%cols]:
                return True
            elif target>matrix[mid//cols][mid%cols]:
                l=mid+1
            else:
                r=mid-1
        return False
