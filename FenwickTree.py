class FenwickTree():
    def __init__(self,lst):
        self.BIT = [0 for _ in range(len(lst)+1)]
        for i,num in enumerate(lst):
            print(i,num)
            self.update(i+1,num)
        
    def get_sum(self,idx):
        answer = 0
        while idx:
            answer += self.BIT[idx]
            idx_sub1 = idx-1
            idx = idx & idx_sub1
        return answer

    def update(self,idx,change_num):
        before_num = self.get_sum(idx) - self.get_sum(idx-1)
        while idx < len(self.BIT):
            self.BIT[idx] -= before_num
            self.BIT[idx] += change_num
            com_idx = ~ idx
            last_idx_bit = idx & (com_idx+1)
            idx += last_idx_bit
            pass

    def add(self,num):
        self.BIT.append(0)
        self.update(len(self.BIT)-1,num)
        return

    def __getitem__(self,idx):
        return self.get_sum(idx)-self.get_sum(idx-1)

class StrFenwickTree():
    def __init__(self,lst):
        self.lst = lst
        self.BIT = [{} for _ in range(len(lst)+1)]
        for i,l in enumerate(lst):
            self.init_update(i+1,l)
        
    def getsum(self,idx):           # return: {gem1:갯수, gem2:갯수, ...}
        answer = {}
        while idx:
            for k,v in self.BIT[idx].items():
                if k in answer:
                    answer[k] += v
                else:
                    answer[k] = v
            idx_sub1 = idx-1
            idx = idx & idx_sub1
        return answer
    
    def init_update(self,idx,l):
        while idx < len(self.BIT):
            if l in self.BIT[idx]:
                self.BIT[idx][l] += 1
            else:
                self.BIT[idx][l] = 1
            com_idx = ~ idx
            last_idx_bit = idx & (com_idx+1)
            idx += last_idx_bit

lst = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]

a = StrFenwickTree(lst)

print(a.BIT)
print(a.getsum(3))

print(a.getsum(5))