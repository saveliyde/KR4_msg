class security():
    def __init__(self, public_key1, public_key2, private_key):
        self.public_key1 = public_key1
        self.public_key2 = public_key2
        self.private_key = private_key
        self.full_key = None

    def generate_partial_key(self):
        partial_key = self.public_key1 ** self.private_key
        partial_key = partial_key % self.public_key2
        return partial_key

    def generate_full_key(self, partial_key_r):
        full_key = partial_key_r ** self.private_key
        full_key = full_key % self.public_key2
        self.full_key = full_key
        return full_key

    def encrypt_msg(self, msg):
        encrypted_msg = ""
        key = self.full_key
        for c in msg:
            encrypted_msg += chr(ord(c) + key)
        return encrypted_msg

    def decrypt_msg(self, encrypted_msg):
        decrypted_msg = ""
        key = self.full_key
        for c in encrypted_msg:
            decrypted_msg += chr(ord(c) - key)
        return decrypted_msg