class hashMap:
    def __init__(self):
        self.size = 6 #usually 64 or something larger than 6
        self.map = [None] * self.size

    def get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        key_hash = self.get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self.get_hash(key)
        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def print(self):
        print('-----Phone Book-----')
        for item in self.map:
            if item is not None:
                print(str(item))


def main():
    h = hashMap()

    h.add('Bob', '777-7777')
    h.add('Ming', '888-8888')
    h.add('Ming', '333-3333')
    h.add('Ankit', '111-1111')
    h.add('Aditya', '222-2222')
    h.add('Mike', '444-4444')
    h.add('Aditya', '555-5555')
    h.print()
    h.delete('Bob')
    h.print()

    print('Ming: ' + h.get('Ming'))

main()
