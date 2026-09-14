class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st=[]
        maxarea=0
        for i,h in enumerate(heights):
            startindex=i
            while st and st[-1][1]>h:
                index,height=st.pop()
                maxarea=max(maxarea,(i-index)*height)
                startindex=index
            st.append((startindex,h))
        for i,h in st:
            maxarea=max(maxarea,(len(heights)-i)*h)
        return maxarea
