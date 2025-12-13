class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        n = len(code)
        valid = []
        order = ["restaurant", "grocery", "pharmacy", "electronics"]
        
        for i in range(n):
            if not code[i]:
                continue
            if not isActive[i]:
                continue

            if businessLine[i] not in order:
                continue
            if not (code[i].replace("_", "").isalnum() or code[i] == "_"):
                continue

            valid.append((businessLine[i], code[i]))
        valid.sort()
                
        return [c for _ , c in valid]
