from typing import Self


class NestedInteger:
    def isInteger(self) -> bool:
        pass

    def getInteger(self) -> int:
        pass

    def getList(self) -> list[Self]:
        pass

class NestedIterator:
    def __init__(self, nestedList: list[NestedInteger]):
        self.flatten = []
        self.index = 0
        def flatten(nested):
            if not nested.isInteger():
                for child in nested.getList():
                    flatten(child)
            else:
                self.flatten.append(nested.getInteger())

        for n in nestedList:
            flatten(n)
        
        print(self.flatten)
    
    def next(self) -> int:
        self.index += 1
        return self.flatten[self.index - 1]
    
    def hasNext(self) -> bool:
        return self.index < len(self.flatten)