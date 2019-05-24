from dictionary_structure import Dictionary


def main():

    record = Dictionary()
    print(record.fromkeys(('key1', 'key2', 'key3'), 0))
    record.clear()
    
    record['year'] = 2018
    record[23] = 'numeric value'
    record['month'] = 'Dec'
    record['day'] = 'Monday'
    record['brand'] = '_Ford'
    record['model'] = '_Mustang'
    record.pop("day")

    record_update = Dictionary()
    record_update['year'] = 2019
    record_update['color'] = '_White'

    record.update(record_update)
    record.popitem()
    record.setdefault('DOB', '1993')

    record_copy = record.copy()
    print(record_copy)


if __name__ == "__main__":
    main()
