from __future__ import annotations
class Term:
    def __init__(self:Term,coff:int,exp:int) -> None:
        self.coff=coff
        self.exp=exp

    def __str__(self) -> str:
        return f"{self.coff} {self.exp}"
    
