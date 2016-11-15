class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        base_dirs = []
        cur_len = 0
        max_path_len = 0
        lines = input.split('\n')
        for line in lines:
            if not line:
                continue
            last_tab = line.rfind('\t')
            for i in range(len(base_dirs)-last_tab-1,0,-1):
                cur_len -= base_dirs[-1]
                base_dirs.pop()
            cur_len += len(line)-last_tab-1
            if '.' in line:
                if cur_len>max_path_len:
                    max_path_len = cur_len
            cur_len += 1 # add '/'
            base_dirs.append(len(line)-last_tab) # add '/'
        return max_path_len
