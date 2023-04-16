
class queue:
    internal_list : list
    def __init__(self) -> None:
        self.internal_list = []
    def push_back(self, object: str):
        self.internal_list.append(object)
    def pop(self) -> str:
        return self.internal_list.pop(0)
    def isempty(self) -> bool:
        return len(self.internal_list) == 0
    def emptyqueue(self):
        self.internal_list = []
