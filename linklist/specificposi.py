def insert_at_pos(self, data, pos):
        new_node = Node(data)
        if pos == 0:
            self.insert_at_begin(data)
            return
        temp = self.head
        for _ in range(pos - 1):
            if temp is None:
                return
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
