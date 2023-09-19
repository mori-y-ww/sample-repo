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
age =121
age_alcohol =20
if age >=age_alcohol:
    print('You can drink beer!')
else:
    print('You are too young to drink beer')

age_drive=18
if age>=age_alcohol:
    print('You can drink beer!')
elif age <age_drive:
    print('You are not allowed to drink beer only if you can drive car')

if not 0<age<120:
    print('The value is invalid')

balance=5000
withdraw=2000000000
withdraw_limit=1000000
if withdraw<=withdraw_limit:
    if balance>=withdraw:
        balance-=withdraw
        print('残高:'+str(balance))
    else:
        print('残高が足りません')
else:
    print('引出しの上限が超えています')

#if 文のnone
a=None
if a is None:
    print('a is none')
else:
    print('a is value')

if a:
    print('a has value')
else:
    print('a is None')

if not a:#aがnoneだったら値を入れる処理。
    a=10
    print(a)

#input(): ユーザの入力を文字列で取得

# age=int(input('何歳ですか？'))

# #print('あなたは{}歳です'.format(age))
# border_age=18
# game_menus={1:'ルーレット',2:'ブラックジャック',3:'ポーカー'}
# if age>=border_age:
#     print('カジノへようこそ')
#     print(game_menus)
#     game_number=int(input('どのゲームを選びますか？数字で答えてください:'))
#     if 1<=game_number<=3:
#         game_name=game_menus[game_number]
#         print('あなたは{}を選びました'.format(game_name))
#     else:
#         print('正しい数字をお選びください')
# else:
#     print('カジノへ入れません')

#リスト複数のオブジェクトを順序付けて保存するデータ型
#[]でくくって、カンマで各オブジェクトを区切る
fruits=['apple','peach','melon','grapes']

hetro_list=['string',1,3.4,True,fruits]
print(hetro_list)
print('hello world'[3:5])

# .append:新しいobjectの追加
fruits.append('banana')
print(fruits)
# .insert:指定したindexに指定したobejectの追加
fruits.insert(3,'lemon')
print(fruits)
# .remove:マッチした最初のobjectを除く
fruits.remove('peach')
print(fruits)
# .sort:昇順に並べる
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
# len():リストの要素数の獲得
print(len(fruits))
print(len('hello'))

#slicing
even=[2,4,6,8,10,12]
#基本は[開始:未満]
print(even[1:4])

print(even[:4])

print(even[3:-1])

print(even[3:])

print(even[:])

text='hello world'
print(text[3:])

#[開始:未満:step]
print(text[2:10:2])

print(text[::-1])

#+でリストの結合をする
print([1,2,3]+[4,5,6])

a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)
a.append(b)
print(a)

#join
text="**".join(["Hi","My",'name','is','John'])
print(text)
#split 
print('Hi My name is John'.split(" "))

filename ='sample.py'
print(filename.split('.')[-1])

#in演算子
fruits=['apple','peach','grapes','banana']
# print('apple' in fruits)
# print('lemon' in fruits)
# print('h' in 'hello world')

# favorite_fruit=input('好きなフルーツを選んでください')
# if favorite_fruit in fruits:
#     fruits.remove(favorite_fruit)
#     print(fruits)
# else:
#     fruits.append(favorite_fruit)
#     print(fruits)

#forループ
#ループで回すことをiterationするという。できるものをiterableという。
# for fruit in fruits:
#     print(f'I love {fruit}!')

# for char in 'hello world!':
#     print(f'char: {char}')

# for fruit in fruits:
#     favorite=input(f'{fruit}は好きですか？')
#     print(f'{fruit}は{favorite}です')


# favorite_fruit=[]
# nomal_fruit=[]
# for fruit in fruits:
#     favorite=input(f'{fruit}は好きですか？y/n')
#     if favorite=='y':
#         favorite_fruit.append(fruit)
#         print(favorite_fruit)
#     else:
#         nomal_fruit.append(fruit)
#         print(nomal_fruit)

#range(start,stop,step)


for _ in range(10):
    print('hello')

for i in range(1,51):
    if i%15==0:
        print('FizzBuzz')

    elif i%3==0:
        print('Fizz')
    
    elif i%5==0:
        print('Buzz')
    
    else:
        print(i)

#whileループ条件を設定、条件がtrueならループ<->forループlistをループ
# count=0
# while count<10:
#     count+=1
#     print(count)

# while True:
#     age=int(input('あなたは何歳ですか？'))
#     if not 0<=age<=120:
#         print('入力された値は正しくありません')
#         continue
#     else:
#         print(f'あなたは{age}歳です')
#         break
# casino_age=18
# game_list={'1':'ルーレット','2':'ブラックジャック','3':'ポーカー'}
# while True:
#     age=int(input('あなたは何歳ですか？'))
#     if not 0<=age<=120:
#         print('正しい数字を入力してください')
#         continue
#     else:
#         if casino_age<=age:
#             print('カジノへようこそ')
#             game=input(f'{game_list}から好きな数字を選んでください')
#             if game=='1':
#                 print(f'あなたは{game_list[game]}を選びました')
#                 break
#             elif game=='2':
#                 print(f'あなたは{game_list[game]}を選びました')
#                 break
#             elif game=='3':
#                 print(f'あなたは{game_list[game]}を選びました')
#                 break
#             else:
#                 print('数字が正しくありません')
#                 continue
#         else:
#             print('あなたはカジノへ入れません')
#             continue

#for else
# fruits=['apple','peach','grapes','banana']
# for fruit in fruits:
#     choice=input(f'あなたが探しているフルーツは{fruit}ですか？y/n:')
#     if choice =='y':
#         print('見つかってよかったね')
#         break
#     else:
#         print('そうですか。。。')
# else:
#     print('お探しのフルーツはありませんでした。')


#while else
# count=0
# while count<10:
#     print(count)
#     count+=1
# else:
#     print('countは20未満で無くなりました')

# balance =1000
# game_price=200

# while balance>=game_price:
#     choice =input(f'1回{game_price}円のゲームに参加しますか？(残高:{balance}円(y/n))')
#     if choice=='y':
#         balance-=game_price
#         print(balance)
#         continue
#     elif choice=='n':
#         print('また遊ぼう')
#         break
#     else:
#         print('yかnで答えてください')
#         continue
# else:
#     print('残高不足です。')

# fruits=['apple','peach','grapes','banana']

# for idx,value in enumerate(fruits):
#     print(idx)
#     print(value)

for x in enumerate(fruits):
    print(x)

#リスト内方表記(list comprehension)

square_list=[]#0,1,4,9,16,25...
for i in range(10):
    square_list.append(i**2)

print(square_list)

square_list=[i**2 for i in range(10)]
print(square_list)

even_square_list=[i**2 for i in range(10) if i%2==0]
print(even_square_list)

#tuple(タプル)：変更できないリスト
date_of_birth=(1999,2,3)
# date_of_birth=[1999,2,3]
# date_of_birth[0]=1990
print(date_of_birth[0])

year,month,date=date_of_birth
print(year)
print(month)
print(date)

#dictionary:キーと値の組み合わせを複数保存するデータ
fruits_colors={'apple':'red','lemon':'yellow','grapes':'purple'}
print(fruits_colors['apple'])
fruits_colors['peach']='pink'
print(fruits_colors)
dict_sample={1:'one','two':2,'three':[1,2,3],'four':{'inner':'dict'}}
print(dict_sample)
print(dict_sample['four']['inner'])

colors={}
colors[1]='blue'
colors[2]='red'
colors[0]='grapes'
print(colors)

#.keys() .values()
for x in fruits_colors:
    print(x)

#.items()
for fruit,color in fruits_colors.items():
    print(f'{fruit}は{color}色です')
            
fruits_color = {'apple':'red','lemon':'yellow','grapes':'purple'}
print(fruits_color['apple'])

if 'peach' in fruits_color:
    print(fruits_color['peach'])
else:
    print('the key is not found')

#.get()
# fruit=input('フルーツの名前を選択してください')
# print(fruits_color.get(fruit,'Nothing'))

#.update()
fruits_color2={'peach':'pink','kiwi':'green'}
fruits_color.update(fruits_color2)
print(fruits_color)

#セット(sets):重複しないリスト指定できない
fruits={'apple','peach','lemon','grapes','apple'}
print(fruits)

#キャスティング(casting):データの型変換
#str,float,int,list,bool,set

#mutable変更可能な list,dict,set

#imutable int,float,str,bool,tuple






