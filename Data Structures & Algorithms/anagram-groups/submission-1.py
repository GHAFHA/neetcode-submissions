class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # this is a dict whose type for the value is a list
        groups = defaultdict(list)

        for s in strs:
            # dicts need keys and values, and we already said that the value is going to be a list
            # so we need to build the key
            key = tuple(sorted(s)) #(a,c,t)
            # now we add the value to the dict at the key we just computed
            groups[key].append(s)
        
        # since the sorting takes car of adding to the appropriate key in the dict, we can just return the dict itself now as a list
        return list(groups.values())