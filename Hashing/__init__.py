from Hashing.Chainning import chaining
from Hashing.Double_hashing import Double_hashing
from Hashing.LinerProbing import Linear_Probing
from Hashing.QuadraticProbing import Quadratic_Probing


def introduction():
    print("\nHashing")
    print("-" * 120)
    print("This Module contains all the algorithm related to the Hasing")
    print("Example of Searching and inserting using LinerProbing")
    x = Linear_Probing()
    hash_table = x.insert([5, 25, 15, 35, 95])
    print(hash_table)
    print(x.search(35, hashtable=hash_table))
