import os

with open("books/frankenstein.txt", "r") as f:
    file_name = os.path.basename('books/frankenstein.txt')
    file_contents = f.read()
   # print(file_contents)



def get_char_dict(text):
    chars = {}
    chars_keys = []
    chars_vals = []
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    chars = chars
    
    for keys, vals in chars.items():
        key = keys 
        val = vals 
        chars_keys.append(key)
        chars_vals.append(val)
        print(f"The {keys} character was found {vals} times")
    #return chars_keys, chars_vals



def get_char_sum(text):
    words = text.split()
    return len(words)

print(f"---Begin report of {file_name}---")
print(get_char_sum(file_contents),"words found in the document")
print(get_char_dict(file_contents))
print("---End Report---")
#print(get_char_sum(file_contents))
#print(get_char_dict(file_contents))
