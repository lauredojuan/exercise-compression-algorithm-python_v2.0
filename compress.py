# !/usr/bin/python
# coding=utf-8
import re

symbols = {
    "implementation": "🤯",
    "practicality": '🤩',
    "better": '😅',
    "than": '😘',
    "Although": "🥺"
}

def compress(content):
    compressed_content = content
    for x in symbols:
        compressed_local = compressed_content.replace(x, symbols[x])
        compressed_content = compressed_local

    return compressed_content
    