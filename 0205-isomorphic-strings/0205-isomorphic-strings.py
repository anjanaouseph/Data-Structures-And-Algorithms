#can maintain mapping in LL and arry list also but for
#O(1) search complexity, we need hashMap
#we need s to t and t to s mapping to avoid breach of "No two characters may map to the same character". eg: egl and add , here g and l can map to d. To avoid this we need 2 hashmaps
#we can't have a single map for s->t and t->s mapping because we won't know from which string the chars are coming from. Else we have to maintain a flag (in a tuple with key) with keys to show distinction but its as good as having two hashmaps. space complexity will be 2 * no. of keys, if we use 2 hashmaps or two keys within a single hashmap. 


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for cs, ct in zip(s, t):
            if cs in s_to_t and s_to_t[cs] != ct:
                return False
            if ct in t_to_s and t_to_s[ct] != cs:
                return False

            s_to_t[cs] = ct
            t_to_s[ct] = cs

        return True