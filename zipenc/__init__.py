import logging
from .files import (insert_metadata_eof, encrypt_text, decrypt_text,
                    join_texts, seperate_text_on_patterns,
                    extract_metadata, default_patterns, aes_encrypt, aes_decrypt, find_pattern_positions)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Package mypackage initialized.")
__all__ = [
    "insert_metadata_eof",
    "encrypt_text",
    "decrypt_text",
    "join_texts",
    "seperate_text_on_patterns",
    "extract_metadata",
    "default_patterns",
    "aes_encrypt",
    "aes_decrypt",
    "find_pattern_positions"
]
