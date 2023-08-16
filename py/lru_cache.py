class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.count = 0
        self.dict = {}
        self.head = {}
        self.tail = {}
        self.head['next'] = self.tail
        self.tail['prev'] = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dict:
            return -1
        else:
            node = self.dict[key]
            node['prev']['next'] = node['next']
            node['next']['prev'] = node['prev']
            self.insert_head(node)
            return node['value']

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dict:
            node = self.dict[key]
            node['prev']['next'] = node['next']
            node['next']['prev'] = node['prev']
            node['value'] = value
            self.insert_head(node)
        else:
            node = {}
            node['value'] = value
            node['key'] = key
            self.dict[key] = node
            self.insert_head(node)
            self.count += 1
            if self.count > self.capacity:
                last_node = self.tail['prev']
                last_node['prev']['next'] = self.tail
                self.tail['prev'] = last_node['prev']
                del self.dict[last_node['key']]
                self.count -= 1

    def insert_head(self, node):
        temp = self.head['next']
        self.head['next'] = node
        node['prev'] = self.head
        node['next'] = temp
        temp['prev'] = node
