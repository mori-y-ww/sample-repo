#strings
print('hello world')

#assignment
a='hello world'#object

print('konnnitiha'+'sekai')#ハードコーディング

#format
print('{} {}'.format(a , a))

name='john'
print('Hey, {}!!How are you doing?'.format(name))

#fstring
a='hello'
b='world'
print(f"{a} {b}")

#数値型:numeric=>integer,float,complex
#int 整数
print(type(-100))

#float(浮動小数)
print(type(0.1))
print(0.1+0.1+0.1)

#Boolean型 2つ
print(True)
print(False)

balance=1000
withdrawal=500

print(balance>withdrawal)
print(True+True)
print(1+True)

#比較演算子<, >, <=, >=, ==, !=

#is演算子同じデータ判別
a=1
b=1
print(a is b)

#論理演算子(logical operators)
a=1
b=1
c=10
d=100
print(a == b and c>d)
print(a==b or c>d)
print(not a == b)

#if文

