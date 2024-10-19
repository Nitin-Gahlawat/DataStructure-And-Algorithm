from Stack.stack import Stack
from Stack.balanced_parentheses import balanced, Matching
from Stack.Evaluation_postfix import eval
from Stack.stack_linkedlist import stack_ll
from Stack.postfix import infix_postfix


def introduction():
    print("\nStack")
    print("-" * 120)
    print("This Module contains all the algorithm related to the Stack datastructure")
    print("example of stack algorithm")

    x = "(A+B)*C+D/E+M"
    print(f"\nConsider The infix expression {x}")

    post = infix_postfix(x)
    print(f"The postfix of this expression is {post}")
