class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.active = False

    def start(self):
        self.active = True
        print(f"Node {self.node_id} started")

if __name__ == "__main__":
    node = Node("ofn-node-001")
    node.start()