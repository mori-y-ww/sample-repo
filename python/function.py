#function
def print_dict(input_dict):
    for k,v in input_dict.items():
        print(f'key:{k},value:{v}')
#returnがなければnanを返している
        
a={'one':1,'two':2}
print(a)
print_dict(a)
return_value=print_dict(a)
print(return_value)

def get_first_last_word(text):
    text=text.replace(',','')
    words=text.split()
    return words[0],words[-1]
#複数返す場合tupleで帰ってくる

text = 'Hello, My name is Mike'
first,last=get_first_last_word(text)
print(f'first:{first},last:{last}')