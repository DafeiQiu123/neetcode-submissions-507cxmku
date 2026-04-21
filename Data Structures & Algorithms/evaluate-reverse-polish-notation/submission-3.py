class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        sn = []
        for i in tokens:
            if i not in ("+","-","*","/"):
                sn.append(int(i))
            else:
                a = sn.pop()
                b = sn.pop()
                if i == "+":
                    sn.append(a+b)
                elif i == "-":
                    sn.append(b-a)
                elif i == "*":
                    sn.append(b*a)
                else:
                    sn.append(int(b/a))
        return sn[0]
                