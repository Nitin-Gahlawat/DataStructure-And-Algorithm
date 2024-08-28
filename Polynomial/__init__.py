from __future__ import annotations
from .Term import Term

class Polynomial:
    def __init__(self:Polynomial,terms:list[Term]) -> None:
        self.n:int=len(terms)
        self.terms=terms

    @staticmethod
    def set_coff_exp(coff:list[int],exp:list[int])->Polynomial:
        terms:list[Term]=[]
        for i in range(len(coff)):
            terms.append(Term(coff[i],exp[i]))
        return Polynomial(terms=terms)
    
    def Evaluate(self:Polynomial,x:int):
        result:int=0
        for ct in range(len(self.terms)):
            result+=self.terms[ct].coff*pow(x,self.terms[ct].exp)
        return result
    
    def __str__(self:Polynomial) -> str:
        temp=""
        for i in range(len(self.terms)):
            if(self.terms[i].coff>=0):
                temp+=f" +{self.terms[i].coff}x^{self.terms[i].exp}"
            else:
                temp+=f" {self.terms[i].coff}x^{self.terms[i].exp}"
        return temp+" =0"
    
    def Addtion(self:Polynomial,poly2:Polynomial)->Polynomial:
        i,j=0,0
        c:list[Term]=[]
        while(i<self.n and j<poly2.n):
            if(self.terms[i].exp<poly2.terms[j].exp):
                c.append(self.terms[i])
                i=i+1
            elif(self.terms[i].exp>poly2.terms[j].exp):
                c.append(poly2.terms[j])
                j=j+1
            else:
                c.append(Term(self.terms[i].coff+poly2.terms[j].coff,self.terms[i].exp))
                i,j=i+1,j+1
        while(i<self.n):
            c.append(self.terms[i])
            i=i+1
        while(j<poly2.n):
            c.append(poly2.terms[j])
            j=j+1
        return Polynomial(c)
    

    def Substraction(self:Polynomial,poly2:Polynomial)->Polynomial:
        i,j=0,0
        c:list[Term]=[]
        while(i<self.n and j<poly2.n):
            if(self.terms[i].exp<poly2.terms[j].exp):
                c.append(self.terms[i])
                i=i+1
            elif(self.terms[i].exp>poly2.terms[j].exp):
                c.append(Term(-1*poly2.terms[j].coff,poly2.terms[j].exp))
                j=j+1
            else:
                c.append(Term(self.terms[i].coff-poly2.terms[j].coff,self.terms[i].exp))
                i,j=i+1,j+1
        while(i<self.n):
            c.append(self.terms[i])
            i=i+1
        while(j<poly2.n):
            c.append(Term(-1*poly2.terms[j].coff,poly2.terms[j].exp))
            j=j+1
        return Polynomial(c)
    



def introduction():
    print("\nPolynomial")
    print("-" * 120)
    print("This Module Contains all the algorithm related to the Polynomial datastructure")
    print("example of Polynomial algorithm")
    c:list[Term]=[Term(1,1),Term(-1,2),Term(1,3)]
    
    
    print("\nLet`s take 2 polynomial\n")
    x=Polynomial.set_coff_exp([1,-1,1],[1,2,3])
    y=Polynomial.set_coff_exp([1,2,3],[1,3,5])
    print(x)
    print(y)

    print("\nPerforming Addtion....")
    z=x.Addtion(y)
    print("\nThe Result of the Addtion is ")
    print(z)

    print("\nPerforming Substraction....")
    z=x.Substraction(y)
    print("\nThe Result of the substraction is ")
    print(z)

    print("\nEvaluating using variable value as 5 ...")
    z=x.Evaluate(x=5)
    print("\nThe Result of the Evaluate for x=5 is ")
    print(z)