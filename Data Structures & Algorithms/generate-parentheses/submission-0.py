class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        stack=[]
        def dfs(openn,closed):
            if openn==closed==n:
                res.append("".join(stack))
                return
            if openn<n:
                stack.append("(")
                dfs(openn+1,closed)
                stack.pop()
            if closed<openn:
                stack.append(")")
                dfs(openn,closed+1)
                stack.pop()
        dfs(0,0)
        return res