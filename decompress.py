# !/usr/bin/python
# coding=utf-8
import re

def decompress(compressed_content):
    from compress import symbols
    decompressed_content = compressed_content
    for x in symbols:
        decompressed_local = decompressed_content.replace(symbols[x], x)
        decompressed_content = decompressed_local
    
    return decompressed_content
    