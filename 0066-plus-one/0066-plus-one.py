class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new = int("".join(map(str,(digits))))
        new += 1 
        return list(map(int,str(new)))