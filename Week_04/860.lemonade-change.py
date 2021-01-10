class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cnt_5, cnt_10 = 0, 0

        for bill in bills:
            if bill == 5: 
                cnt_5 += 1
            elif bill == 10: 
                cnt_5 -= 1
                cnt_10 += 1
            else:
                cnt_5 -= 1
                if cnt_10 > 0:
                    cnt_10 -= 1  
                else:
                    cnt_5 -= 2
            
            if cnt_5 < 0 or cnt_10 < 0: return False
        
        return True