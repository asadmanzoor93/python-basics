from hash_table_structure import HashTable


class Dictionary(object):
    def __init__(self):
        self.hash_table = HashTable()

    def __getitem__(self, key):
        return self.hash_table[key]

    def __setitem__(self, key, value):
        self.hash_table[key] = value

    def __delitem__(self, key):
        self.hash_table.remove(key)

    def __repr__(self):
        return "Dictionary({" + ", ".join([f"{hash_item.key} : {hash_item.value}"
                                           for hash_item in self.hash_table.items()]) + "})"

    def fromkeys(self, keys, value=0):
        self.clear()
        for key in keys:
            self.hash_table[key] = value
        return self

    def clear(self):
        self.hash_table.clear()

    def keys(self):
        return [dict_item.key for dict_item in self.hash_table.items()]

    def values(self):
        return [dict_item.value for dict_item in self.hash_table.items()]

    def items(self):
        return [(dict_item.key, dict_item.value) for dict_item in self.hash_table.items()]

    def get(self, key, default=0):
        dict_item = self.hash_table[key]
        return dict_item.value if dict_item else default

    def update(self, records):
        self.hash_table.update(records)

    def pop(self, key):
        self.hash_table.remove(key)

    def popitem(self):
        self.hash_table.remove_last_index()

    def setdefault(self, key, value):
        dict_item = self.hash_table[key]
        if dict_item is not None:
            return dict_item.value
        else:
            self.hash_table[key] = value
            return value

    def copy(self):
        copy_obj = Dictionary()
        for dict_item in self.hash_table.items():
            copy_obj[dict_item.key] = dict_item.value

        return copy_obj
