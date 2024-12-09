from functools import reduce
from encrept import aes_encrypt, aes_decrypt
from .utils import find_pattern_positions

# Todo abstract the hardcoded texts to the main file

default_patterns = {"metadata": "<<METADATA>>",
                    "eometadata": "<<EOMETADATA>>",
                    "eof": "<<EOF>>"}


def insert_metadata_eof(list_of_texts,
                        list_of_metadata,
                        patterns=default_patterns):
    mapped_list = map(lambda text, metadata: patterns["metadata"]+metadata +
                      patterns["eometadata"]+text + patterns["eof"], list_of_texts, list_of_metadata)
    return list(mapped_list)


def encrypt_text(text, key):
    return aes_encrypt(text, key)


def join_texts(list_of_texts):
    return reduce(lambda x, y: x + y, list_of_texts)


def decrypt_text(text: str, key: str):
    return aes_decrypt(text, key)


def seperate_text_on_patterns(text: str,
                              patterns=default_patterns):
    extracted_texts = []

    patterns_matches = find_pattern_positions(text, patterns.values())

    num_eof = len(patterns_matches[patterns["eof"]])
    for i in range(num_eof):
        meta = patterns_matches[patterns["metadata"]][i].start
        eof = patterns_matches[patterns["eof"]][i].start
        extracted_texts.append(text[meta:eof])
    return extracted_texts


def extract_metadata(text, patterns=default_patterns):
    extracted_texts = []
    
    patterns_matches = find_pattern_positions(text, patterns.values())
    num_eof = len(patterns_matches[patterns["eof"]])
    for i in range(num_eof):
        meta = patterns_matches[patterns["metadata"]][i]["end"]
        eometa = patterns_matches[patterns["eometadata"]][i]["start"]
        extracted_texts.append(text[meta:eometa])
    return extracted_texts
