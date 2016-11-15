class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        operands = []
        operators = []
        while True:
            i = 0
            while i<len(input) and not input[i] in "+-*":
                i += 1
            operands.append(int(input[0:i]))
            input = input[i:]
            if not input:
                break
            operators.append(input[0])
            input = input[1:]
        return self.subExpressionResults(operands,operators,0,len(operands)-1)
        
    # i,j: subrange of operands
    def subExpressionResults(self, operands, operators, i, j):
        results = []
        if i<j:
            for k in range(i,j):
                results_l = self.subExpressionResults(operands,operators,i,k)
                results_r = self.subExpressionResults(operands,operators,k+1,j)
                for v1 in results_l:
                    for v2 in results_r:
                        if operators[k]=='+':
                            v = v1+v2
                        elif operators[k]=='-':
                            v = v1-v2
                        else:
                            v = v1*v2
                        results.append(v)
        else:
            results.append(operands[i])
        return results
