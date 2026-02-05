class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
            return

        cur = self.root
        while True:
            if val < cur.val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = Node(val)
                    return
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = Node(val)
                    return

    def path_to(self, val):
        path = []
        cur = self.root
        while cur:
            path.append(cur.val)
            if val == cur.val:
                return path
            elif val < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        return []

    def insert_number_and_print_path(self, number):
        digits = str(number)

        for d in digits:
            self.insert(int(d))

        start = int(digits[0])   # 4
        end = int(digits[-1])    # 1

        p1 = self.path_to(start)
        p2 = self.path_to(end)

        i = 0
        while i < len(p1) and i < len(p2) and p1[i] == p2[i]:
            i += 1

        path = p1[:i-1:-1] + p2[i-1:]
        print(path)

