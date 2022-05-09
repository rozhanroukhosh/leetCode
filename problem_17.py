#17. Letter Combinations of a Phone Number
#https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # function that converts tuple to string
        def join_tuple_string(strings_tuple) -> str:
           return "".join(strings_tuple)
    
        dic={
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }
        
        if len(digits)==0:
            return []
        
        x = tuple(dic[d] for d in digits)
        cartesian_product = list(map(join_tuple_string,list(itertools.product(*x))))
        return cartesian_product
                
                
        