class Linear_Probing:
    def __init__(self):
        self.hashfun = lambda a: a % 10
        self.Linear_fun = lambda a: a

    def insert(self, x: list[int]):

        hashtable = [0 for _ in range(0, 10)]
        for i in x:
            num = self.hashfun(i)
            if hashtable[self.hashfun(i)] == 0:
                hashtable[self.hashfun(i)] = i
            else:
                inc = 1
                temp: int = self.hashfun(num + inc)
                while hashtable[temp] != 0 and temp != num:
                    inc += 1
                    temp = self.hashfun(i + self.Linear_fun(inc))
                if temp == num:
                    print(i)
                    raise Exception("No free space")
                elif hashtable[temp] == 0:
                    hashtable[temp] = i

        return hashtable

    def search(self, ele: int, hashtable: list[int]):
        if hashtable[self.hashfun(ele)] == ele:
            return True
        inc = 1
        num = self.hashfun(ele)
        temp: int = self.hashfun(ele + inc)
        while hashtable[temp] != ele and temp != num:
            if hashtable[temp] == 0:
                return False
            temp = self.hashfun(temp + self.Linear_fun(inc))
        if hashtable[temp] == ele:
            return True
        else:
            return False


if __name__ == "__main__":
    x = Linear_Probing()
    hash_table = x.insert([5, 25, 15, 35, 95])
    print(hash_table)
    print(x.search(35, hashtable=hash_table))
