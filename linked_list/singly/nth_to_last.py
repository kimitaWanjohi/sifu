class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def len_iterative(self):
        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def print_nth_from_last(self, n):
        total_len = self.len_iterative()

        curr = self.head
        while curr:
            if total_len == n:
                print(curr.data)
                return curr
            total_len -= 1
            curr = curr.next

        if curr is None:
            return

    def print_nth_from_last2(self, n):
        p = self.head
        q = self.head

        count = 0
        while q and count < n:
            q = q.next
            count += 1

        if not q:
            print(str(n) + " is greater than the number of nodes in list.")
            return

        while p and q:
            p = p.next
            q = q.next

        return p.data


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

print(llist.print_nth_from_last(2))
