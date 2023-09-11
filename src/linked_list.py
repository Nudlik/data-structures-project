class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""

        if self.head is None:
            self.head = Node(data, None)
            self.tail = self.head
        else:
            self.head = Node(data, self.head)

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""

        if self.head is None:
            self.head = Node(data, None)
            self.tail = self.head
        else:
            self.tail.next_node = Node(data, None)
            self.tail = self.tail.next_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""

        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string.lstrip()

    def to_list(self) -> list:
        """Возвращает список с данными, содержащимися в односвязном списке"""

        node = self.head
        if node is None:
            return []

        lst = []
        while node:
            lst.append(node.data)
            node = node.next_node

        return lst

    def get_data_by_id(self, id: int) -> dict | None:
        """Возвращает словарь с ключом 'id', значение которого равно переданному в метод значению"""

        for elem in self.to_list():
            try:
                if elem['id'] == id:
                    return elem
            except TypeError:
                print('Данные не являются словарем или в словаре нет id')
