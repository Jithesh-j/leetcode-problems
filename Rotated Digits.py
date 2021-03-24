class Solution:
    def rotatedDigits(self, N: int) -> int:
        rel = []
        for i in range(1,N+1):
            temp = ''
            for j in str(i):
                if j == '0' or j == '1' or j == '8':
                    temp = temp + j
                elif j == '2':
                    temp = temp + '5'
                elif j =='5':
                    temp = temp + '2'
                elif j =='6':
                    temp= temp + '9'
                elif j == '9':
                    temp = temp + '6'
                else:
                    temp = temp + 'f'
            if temp != str(i) and 'f' not in temp:
                rel.append(i)
        return len(rel)
