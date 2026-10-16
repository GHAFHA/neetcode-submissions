class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups=defaultdict(list) #this creates a new dict where any new key starts with an empty list
        for s in strs:
            # act
            # sort the characters of s to get a canonical key
            # key = a, c, t
            key = tuple(sorted(s))   # tuple so it's hashable
            # {a,c,t = [act]}
            groups[key].append(s)
        # return a list of just the values
        return list(groups.values())