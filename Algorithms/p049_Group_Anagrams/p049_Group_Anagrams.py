class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_table = collections.defaultdict(list)
        for s in strs:
            hash_table[''.join(sorted(s))].append(s)
        res = []
        for key in hash_table:
            res.append(hash_table[key])
        return res
