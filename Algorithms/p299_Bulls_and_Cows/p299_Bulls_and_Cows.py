class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        secret_cnt = [0]*10
        guess_cnt = [0]*10
        a_cnt = 0
        b_cnt = 0
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                a_cnt += 1
            else:
                secret_cnt[int(secret[i])] += 1
                guess_cnt[int(guess[i])] += 1
        for i in range(10):
            b_cnt += min(secret_cnt[i],guess_cnt[i])
        return str(a_cnt)+'A'+str(b_cnt)+'B'
