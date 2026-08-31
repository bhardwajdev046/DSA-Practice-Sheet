class Solution:
    def equalFrequency(self, word: str) -> bool:
        # hash={}
        # for i in word:
        #     hash[i]=hash.get(i,0)+1
        # temp = max(hash.values()) 
        # print(temp)
        # key = next((k for k, v in hash.items() if v == temp), None)
        # print(key)
        # hash[key] -=1
        # if hash[key]==0:
        #     del hash[key]
        # print(hash)
        # bin = max(hash.items())
        # print(bin)
        # for ele,freq in hash.items():
        #     if freq!=bin[1]:
        #         return False
        # return True
        
        hash = {}

        for ch in word:
            hash[ch] = hash.get(ch, 0) + 1

        # Try removing exactly one occurrence
        for key in list(hash.keys()):

            hash[key] -= 1

            # character completely remove ho gaya
            if hash[key] == 0:
                del hash[key]

            # remaining frequencies
            if len(set(hash.values())) == 1:
                return True

            # IMPORTANT: hashmap ko restore karo
            hash[key] = hash.get(key, 0) + 1

        return False