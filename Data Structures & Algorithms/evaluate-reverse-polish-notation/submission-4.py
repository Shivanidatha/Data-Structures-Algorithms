class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        r=0
        while r<len(tokens):
            if tokens[r] not in '+-*/':
                st.append(int(tokens[r]))
            else:
                num1=st.pop()
                num2=st.pop()
                if tokens[r]=='+':
                    st.append(num1+num2)
                elif tokens[r]=='-':
                    st.append(num2-num1)
                elif tokens[r]=='*':
                    st.append(num2*num1)
                elif tokens[r]=='/':
                    st.append(int(num2/num1))

            r+=1
        return st[0]
