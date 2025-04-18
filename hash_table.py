class HashTable:
    DELETED = "<DELETED>"

    def __init__(self, initial_size, load_factor, resize_strategy):
        """
        Initialize the hash table.
        :param initial_size: Initial size of the hash table.
        :param load_factor: Maximum load factor before resizing.
        :param resize_strategy: Strategy for resizing (1 = double size, 2 = add 10000).
        """
        self.size = initial_size
        self.load_factor = load_factor
        self.resize_strategy = resize_strategy
        self.table = [None] * self.size
        self.count = 0

    def _hash(self, string):
        """
        Compute the hash value for a string.
        :param string: The string to hash.
        :return: The hash value mod the table size.
        """
        return hash(string) % self.size

    def _resize(self):
        """
        Resize the hash table based on the resize strategy.
        """
        old_table = self.table
        if self.resize_strategy == 1:
            self.size *= 2
        elif self.resize_strategy == 2:
            self.size += 10000
        else:
            raise ValueError("Invalid resize strategy. Use 1 (double size) or 2 (add 10000).")

        self.table = [None] * self.size
        self.count = 0

        for item in old_table:
            if item is not None:
                self.insert(item)

    def insert(self, string_to_insert):
        """
        Insert a string into the hash table.
        """
        # Check load factor BEFORE insertion
        current_load = (self.count + 1) / self.size
        if current_load >= self.load_factor:
            self._resize()

        index = self._hash(string_to_insert)
        first_deleted_index = None

        while self.table[index] is not None:
            if self.table[index] == string_to_insert:
                return  # String already exists
            if self.table[index] == self.DELETED and first_deleted_index is None:
                first_deleted_index = index
            index = (index + 1) % self.size

        insert_index = first_deleted_index if first_deleted_index is not None else index
        self.table[insert_index] = string_to_insert
        self.count += 1

    def find(self, string_to_find):
        """
        Find a string in the hash table.
        :param string_to_find: The string to find.
        :return: True if the string is found, False otherwise.
        """
        index = self._hash(string_to_find)
        steps = 0
        while self.table[index] is not None and steps < self.size:
            if self.table[index] == string_to_find:
                return True
            index = (index + 1) % self.size
            steps += 1
        return False

    def delete(self, string_to_delete):
        index = self._hash(string_to_delete)
        steps = 0
        while self.table[index] is not None and steps < self.size:
            if self.table[index] == string_to_delete:
                self.table[index] = self.DELETED
                self.count -= 1
                return True
            index = (index + 1) % self.size
            steps += 1
        return False

    def contains(self, string):
        return self.find(string)

    def __str__(self):
        return str([item for item in self.table])