class Stack:
    def __init__(self):
        self.stack: list = []

    def is_empty(self) -> bool:
        """
        проверка стека на пустоту. Метод возвращает True или False
        """
        return not self.stack or False

    def push(self, item) -> None:
        """
        добавляет новый элемент на вершину стека. Метод ничего не возвращает.
        """
        self.stack.append(item)

    def pop(self):
        """
        удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека.
        """
        return None if self.is_empty() else self.stack.pop()

    def peek(self):
        """
        возвращает верхний элемент стека, но не удаляет его. Стек не меняется;
        """
        return None if self.is_empty() else self.stack[-1]

    def size(self):
        """
        возвращает количество элементов в стеке
        """
        return len(self.stack)