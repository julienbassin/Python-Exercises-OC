class Queue:

    def __init__(self):
        self.queue = list()

    def enqueue(self, data):
        if data not in self.queue:
            self.queue.append(data)
            return self.queue
        return False

    def dequeue(self):
        if len(self.queue):
            self.queue.pop(0)
            return self.queue
        return ("Queue Empty !")
    
    def printQueue(self):
         print(self.queue)
    
q = Queue()
q.enqueue("toto")
q.enqueue("tata")
q.enqueue("titi")
q.printQueue()
q.dequeue()
q.printQueue()
            







