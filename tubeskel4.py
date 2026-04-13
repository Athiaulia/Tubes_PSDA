class Node:
    def __init__(self, id_member, nama, paket, sisa_durasi):
        self.id_member = id_member
        self.nama = nama
        self.paket = paket
        self.sisa_durasi = sisa_durasi
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, id_member, nama, paket, sisa_durasi):
        if self._find_node(id_member):
            raise ValueError(f"ID {id_member} sudah ada!")
        
        new_node = Node(id_member, nama, paket, sisa_durasi)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def delete(self, id_member):
        curr = self._find_node(id_member)
        if not curr: return False
        if curr.prev: curr.prev.next = curr.next
        else: self.head = curr.next
        if curr.next: curr.next.prev = curr.prev
        else: self.tail = curr.prev
        self.size -= 1
        return True

    def _find_node(self, id_member):
        curr = self.head
        while curr:
            if curr.id_member == id_member: return curr
            curr = curr.next
        return None

    def sort_by_sisa_durasi(self):
        if not self.head or not self.head.next: return
        swapped = True
        while swapped:
            swapped = False
            curr = self.head
            while curr.next:
                if curr.sisa_durasi > curr.next.sisa_durasi:
                    curr.id_member, curr.next.id_member = curr.next.id_member, curr.id_member
                    curr.nama, curr.next.nama = curr.next.nama, curr.nama
                    curr.paket, curr.next.paket = curr.next.paket, curr.paket
                    curr.sisa_durasi, curr.next.sisa_durasi = curr.next.sisa_durasi, curr.sisa_durasi
                    swapped = True
                curr = curr.next

    def display(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(curr)
            curr = curr.next
        return nodes