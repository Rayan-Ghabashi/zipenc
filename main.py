import zipenc
key = "0123456789abcdef"
encrypted_text = zipenc.encrypt_text("hello world", key)
print(encrypted_text)

decrypted_text = zipenc.decrypt_text(encrypted_text, key)

print(decrypted_text)

default_patterns = {"metadata": "[![METADATA]!]",
                    "eometadata": "[![EOMETADATA]]",
                    "eof": "[![EOF]!]"}
list_of_txts = ["hello world", "this is rayan"]
list_of_metadata = ["meta 1","meta2"]
metadata_eof_text = zipenc.insert_metadata_eof(list_of_txts, list_of_metadata)
print(metadata_eof_text)
print(zipenc.extract_metadata(metadata_eof_text[0]))
