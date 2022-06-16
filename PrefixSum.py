class StrPrefixSum():
    def __init__(self,lst):
        self.prefix = [{}]
        for l in lst:
            new_dic = self.prefix[-1].copy()
            if l in new_dic:
                new_dic[l] += 1
            else:
                new_dic[l] = 1
            self.prefix.append(new_dic)

    def getrangesum(self,idx1,idx2):
        new_dic =self.prefix[idx2].copy()
        for k,v in self.prefix[idx1-1].items():
            new_dic[k] -= v
            if new_dic[k] == 0:
                new_dic.pop(k)
        return new_dic


lst = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
prefix = StrPrefixSum(lst)
print(prefix.prefix)
print(prefix.getrangesum(4,6))