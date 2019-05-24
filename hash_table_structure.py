class HashItem(object):
    def __init__(self, key=None, value=None, hash_value=None):
        self.key = key
        self.value = value
        self.hash_value = hash_value

    def __repr__(self):
        return f"<DictionaryItem: key={self.key} value={self.value} hash_value={self.hash_value}>"


class HashTable(object):
    def __init__(self):
        self.used = 0
        self.min_size = 10
        self.hashed_items = []
        for i in range(self.min_size):
            self.hashed_items.append(HashItem())

    def __getitem__(self, key):
        hash_item = self.get_hashed_item(key)
        return hash_item.value if hash_item else None

    def __setitem__(self, key, value):
        self.add(key, value)

    def hash_function(self, hashed_value):
        return hashed_value % len(self.hashed_items)

    def add(self, key, value):
        hash_value = self.hash_function(hash(key))
        hashed_item = self.hashed_items[hash_value]

        if hashed_item.key is None:
            hashed_item.key = key
            hashed_item.value = value
            hashed_item.hash_value = hash_value
            self.used += 1
        else:
            if hashed_item.key == key:
                hashed_item.value = value
            else:
                next_slot = self.hash_function(hash_value + 1)
                next_hashed_item = self.hashed_items[next_slot]

                while next_hashed_item.key is not None and next_hashed_item.key != key:
                    next_slot = self.hash_function(next_slot + 1)
                    next_hashed_item = self.hashed_items[next_slot]

                if next_hashed_item.key is None:
                    next_hashed_item.key = key
                    next_hashed_item.value = value
                    next_hashed_item.hash_value = hash(key)
                    self.used += 1
                else:
                    next_hashed_item.value = value

        if self.used == (self.min_size - 1):
            self.resize()

    def get_hashed_item(self, key):
        hash_value = self.hash_function(hash(key))
        searched_item = None
        end_search = False
        initial_value = hash_value
        hashed_item = self.hashed_items[hash_value]

        while hashed_item.key is not None and not end_search:
            if hashed_item.key == key:
                searched_item = hashed_item
                end_search = True
            else:
                hash_value = self.hash_function(hash_value + 1)
                hashed_item = self.hashed_items[hash_value]
                if hash_value == initial_value:
                    return searched_item

        return searched_item

    def resize(self):
        for i in range(self.min_size):
            self.hashed_items.append(HashItem())

        self.min_size = self.min_size * 2

    def clear(self):
        self.used = 0
        self.hashed_items = []
        for i in range(self.min_size):
            self.hashed_items.append(HashItem())

        return self

    def remove(self, key):
        hashed_item = self.get_hashed_item(key)
        if hashed_item is not None:
            self.clear_item(hashed_item)

    def remove_last_index(self):
        hashed_items = [hashed_item for hashed_item in self.hashed_items if hashed_item.key is not None]
        if self.used > 0:
            self.clear_item(hashed_items[self.used - 1])

    def clear_item(self,hashed_item):
        hashed_item.key = None
        hashed_item.value = None
        hashed_item.hash_value = None
        self.used -= 1

    def insert(self, key, value):
        self.hashed_items.append(HashItem(key, value, hash(key)))

    def update(self, records):
        for record in records.items():
            hashed_item = self.get_hashed_item(record[0])
            if hashed_item is None:
                self.add(record[0], record[1])
            else:
                hashed_item.value = record[1]
    
    def items(self):
        return [hashed_item for hashed_item in self.hashed_items if hashed_item.value is not None]
