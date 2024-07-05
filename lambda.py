# a와 b를 받아서 더하는 함수 만들기

def plus(a,b) :
    result  = a + b
    return result

print(plus(1,6))


plus_lambda = lambda a, b: a + b
print(plus_lambda(1,6))

def plus(a,b) :
    result  = a + b
    return result

print(plus(1,6))


plus_lambda = lambda a, b: a + b
print(plus_lambda(1,6))

def word_len(w):
    print(len(w))

word_len("Hello World")

word_len = lambda w: len(w)
print(word_len("Hello World"))

def squ(x):
    print(x*x)

squ(3)

squ = lambda x : x*x
print(squ(3))

max_num = lambda x , y  :print(x) if x>y else print(y)
max_num(3,2)


my_list = [x*x for x in range(4)]
print(my_list)

my_list_x = list(map(lambda x : x*x, my_list))

print(my_list_x)


list1 = list(map(lambda x : x, range(11)))
print(list1)

list2 = [x for x in range(11) if x %2 ==0]
print(list2)

list3 = list(filter(lambda x : x % 2 ==0, range(11)))                #     filter 로 조건을 다는것
print(list3)

list4 = list(map(lambda x , y :x + y, list2, list3))                 #     map는 전체에 하느 것
print(list4) 