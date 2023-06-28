#!/usr/bin/env/python3

def insert(self, data):
    if self.data:
        if data < self.data:
            if self.left is None:
                self.left = Node(data)


def PrintTree(self):
    if self.left:
        self.left.PrintTree()
    print(self.data),
    if self.right:
        self.right.PrintTree()
def main():
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.PrintTree()


if __name__ == '__main__':
    main()
