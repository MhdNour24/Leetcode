from collections import Counter

class Solution:
    def getCoutOfElementsUsingDic(self,arr):
        return Counter(arr)

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        newArr=[]
        CountElements=self.getCoutOfElementsUsingDic(arr1)

        for el in arr2:
            newArr+=[el]*CountElements[el]
            del CountElements[el]
        CountElements = dict(sorted(CountElements.items(), key=lambda item: item[0]))
        for el in CountElements:
            newArr+=[el]*CountElements[el]
        return newArr