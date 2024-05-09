class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]  # Ініціалізуйте порожні списки

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value  # Оновлюємо значення, якщо ключ уже існує
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is None:
            return False  # Ключ не знайдено
        for i, pair in enumerate(self.table[key_hash]):
            if pair[0] == key:
                del self.table[key_hash][i]  # Видаляємо пару клю-значення
                return True
        return False  # Ключ не знайдено
# Тестування хєш-ьаблиці
H = HashTable(5)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)

print(H.get("apple"))  # Output: 10
print(H.delete("apple"))  # Output: True
print(H.get("apple"))  # Output: None (apple is deleted)
print(H.get("orange"))  # Output: 20
print(H.get("banana"))  # Output: 30
