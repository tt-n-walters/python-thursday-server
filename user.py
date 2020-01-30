
class User:
    def __init__(self, name, password_hash, hash_used):
        self.name = name
        self.password_hash = password_hash
        self.hash_used = hash_used
    
    password = property(lambda self: self.password_hash)

    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        return hash(self) == hash(other)
