class Double_hashing:
    def __init__(self):
        h1 = lambda x: x % 10
        h2 = lambda x: 7 - (x % 7)
        self.hashfun = lambda a, i=0: (h1(a) + i * h2(a)) % 10

    def insert(self, x: list[int]):

        hashtable = [0 for _ in range(0, 10)]
        for i in x:
            num = self.hashfun(i)
            if hashtable[self.hashfun(i)] == 0:
                hashtable[self.hashfun(i)] = i
            else:
                inc = 1
                temp: int = self.hashfun(i, inc)
                while hashtable[temp] != 0 and temp != num:
                    inc += 1
                    temp = self.hashfun(i, inc)
                if temp == num:
                    raise Exception("No free space  ")
                elif hashtable[temp] == 0:
                    hashtable[temp] = i

        return hashtable

    def search(self, ele: int, hashtable: list[int]):
        if hashtable[self.hashfun(ele)] == ele:
            return True
        inc = 1
        num = self.hashfun(ele)
        temp: int = self.hashfun(ele, inc)
        while hashtable[temp] != ele and temp != num:
            if hashtable[temp] == 0:
                return False
            inc += 1
            temp = self.hashfun(ele, inc)
        if hashtable[temp] == ele:
            return True
        else:
            return False


if __name__ == "__main__":
    x = Double_hashing()
    hash_table = x.insert([5, 25, 15, 35, 95])
    print(hash_table)
    print(x.search(35, hashtable=hash_table))
