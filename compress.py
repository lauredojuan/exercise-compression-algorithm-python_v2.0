# !/usr/bin/python
# coding=utf-8
import re
import csv

symbols = {}
# symbols = {
#     "implementation": "🤯",
#     "practicality": '🤩',
#     "better": '😅',
#     "than": '😘',
#     "Although": "🥺"
# }

def load_symbols():
  global symbols
  try:
    with open("symbols.csv", newline='') as myFile:
      reader = csv.reader(myFile)
      for rows in reader:
        symbols = rows
  except:
    open("symbols.csv", "w+")
    load_symbols()
    
    # estrategy: loop the string to check if a word is repeated more than one time. if so add that word as a key to the a dictionary inside symbols.csv and asign a new emogy as value:
    #Return the number of times the value "apple" appears in the string:
#     txt = "I love apples, apple are my favorite fruit"
#     x = txt.count("apple")
#     print(x)

def compress(content):
    load_symbols()
    compressed_content = content

    for x in symbols:
        compressed_local = compressed_content.replace(x, symbols[x])
        compressed_content = compressed_local

    return compressed_content


    
