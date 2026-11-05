# You are given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of
# nested parentheses.

class Solution:
    def maxDepth(self, s: str) -> int:
        # brackets = [i for i in s if i=='(' or i==')']
        # stack=[]
        # depth=0
        # for b in brackets:
        #     if b==')':
        #         stack.pop(-1)
        #     else:
        #         stack.append('(')
        #         depth=max(len(stack),depth)
        # return depth
        depth=0
        max_depth=0
        for ch in s:
            if ch=='(':
                depth+=1
                max_depth=max(max_depth,depth)
            elif ch==')':
                depth-=1
        return max_depth

if __name__=='__main__':
    s = "(1+(2*3)+((8)/4))+1" #(()(()))
    print(Solution().maxDepth(s))