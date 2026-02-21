def count_frequency(st):
    dict={}
    for ch in st:
       dict[ch]=dict.get(ch,0)+1
    return dict
print(count_frequency("aabada")