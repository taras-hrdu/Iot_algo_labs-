class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.prev = None
        self.next = None

class Deque:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def add_head(self, new_data):
        if self.tail is None:
            self.head = Node(new_data)
            self.tail = self.head
        else:
            self.head.prev = Node(new_data)
            self.head.prev.next = self.head
            self.head = self.head.prev

    def add_tail(self, new_data):
        if self.tail is None:
            self.head = Node(new_data)
            self.tail = self.head
        else:
            self.tail.next = Node(new_data)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

    def delete_head(self):
        if self.head is None:
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return temp

    def delete_tail(self):
        if self.head is None:
            return None
        else:
            temp = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = None
            return temp
    
    def find_by_id(self, id):
        index = 0
        start_pos = self.head
        while index < id and start_pos is not None:
            start_pos = start_pos.next
            index += 1
        return start_pos.data

    def print_to_console(self):
        current_pos = self.head
        while current_pos is not None:
            print(current_pos.data)
            current_pos = current_pos.next
    
    def deque_to_list(self):
        empty_list = list()
        curr_pos = self.head
        while curr_pos is not None:
            empty_list.append(curr_pos.data)
            curr_pos = curr_pos.next
        return empty_list


if __name__ == '__main__':
    deque = Deque()
    print(f"My deque:")
    deque.add_head(5)
    deque.add_tail(10)
    deque.add_head(6)
    deque.add_head(11)
    deque.add_tail(14)
    deque.print_to_console()
    elem = deque.find_by_id(3)
    print(f"Found by id: {elem}")
    my_deque_list = deque.deque_to_list()
    print(f"My deque list: {my_deque_list}")
