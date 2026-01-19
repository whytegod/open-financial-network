class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.active = False
        self.peers = []

    def start(self):
        self.active = True
        print(f"Node {self.node_id} started")

    def connect_peer(self, peer_id):
        self.peers.append(peer_id)
        print(f"Node {self.node_id} connected to peer {peer_id}")

    def send_message(self, peer_id, message):
        if peer_id in self.peers:
            print(f"{self.node_id} -> {peer_id}: {message}")
        else:
            print(f"Peer {peer_id} not connected")

    def receive_message(self, peer_id, message):
        print(f"{self.node_id} received from {peer_id}: {message}")


if __name__ == "__main__":
    node = Node("ofn-node-001")
    node.start()

    node.connect_peer("ofn-node-002")
    node.send_message("ofn-node-002", "Hello peer")
    node.receive_message("ofn-node-002", "Hello back")