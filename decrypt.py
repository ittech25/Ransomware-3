def decrypt_files(self) -> None:
    with open(self.get_files(), 'rb+') as f:
        cipher_text = f.read()
        plain_text = self.token.decrypt(cipher_text)
        f.seek(0); f.truncate()
        f.write(plain_text)
