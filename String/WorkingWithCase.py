# ## Working with case


class Working_with_case:

    @staticmethod
    def ToUpperCase(x : str):
        string=""
        for i in x:
            if(ord(i)>=ord('a') and ord(i)<=ord('z')):
                string+=(chr(ord(i)-32))
            else:
                string+=i
        return string
    
    @staticmethod
    def ToLowerCase(x : str):
        string=""
        for i in x:
            if(ord(i)>=ord('A') and ord(i)<=ord('Z')):
                string+=(chr(ord(i)+32))
            else:
                string+=i
        return string
    
    @staticmethod
    def ToggelCase(x : str):
        string=""
        for i in x:
            if(ord(i)>=ord('a') and ord(i)<=ord('z')):
                string+=(chr(ord(i)-32))
            elif(ord(i)>=ord('A') and ord(i)<=ord('Z')):
                string+=(chr(ord(i)+32))
            else:
                string+=i
        return string
    
if __name__=="__main__":
    print(Working_with_case.ToUpperCase("Hello world"))
    print(Working_with_case.ToLowerCase("Hello world"))
    print(Working_with_case.ToggelCase("Hello world"))


