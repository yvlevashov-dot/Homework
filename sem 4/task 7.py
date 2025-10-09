import string
def find_max(start_dict):
    max_val = max(start_dict.values())
    final_dict = {k: v for k, v in start_dict.items() if v == max_val}
    return final_dict
with open( "license.txt", "r") as f:
    lines = f.readlines()
nmb = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9","3104"]
dic = dict()
for i in lines:
    i=i.replace('\n', ' ').replace('\r', '')
    cleaned_text = "".join(char for char in i if char not in string.punctuation)
    cleaned_text = cleaned_text.lower()
    for k in cleaned_text.split(" "):
        if k != "\n":
            if k not in nmb:
                if k in dic:
                    dic[k]+=1
                else:
                    dic[k] = 1
del dic[""]
for i in range(10):
    print(find_max(dic))
    dic = {key: val for key, val in dic.items() if val != max(dic.values())}