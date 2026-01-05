from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        n = len(digits)
        res = []
        
        def backtrack(index, path):
            if index == n:
                res.append(path)
                return
            # 只处理当前 index 对应的数字
            for char in phone_map[digits[index]]:
                backtrack(index + 1, path + char)
        
        backtrack(0, "")
        return res
    
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl',
                   '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = ['']
        for d in digits:
            res = [s + c for s in res for c in mapping[d]]
        return res
