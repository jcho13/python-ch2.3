print("----- global, local symbol table -----")

def f():
    l_a = 2
    l_b = "지역변수"
    print(locals())


class MyClass:
    x =10
    y =20


g_a = 100
g_b = "전역변수"

# table이 (표현만) dictionary 형태로 나타난다
print(globals())



print("----- 1. 정의된 함수 객체 -----")
f.k = "hello"
print(f.__dict__) # 밖에서 보는 방법



print("----- 2. 클래스 객체 -----")
print(MyClass.__dict__)
print(int.__dict__)



print("----- 3. 인스턴스 객체 -----")
o = MyClass()
o.x = 100
o.y = "asfd"
print(o.__dict__)


#  [ 내장함수(sort같은거) 또는 내장 클래스의 인스턴스 객체는 __dict__가 없다 ]
#  [ 즉, 심볼 테이블이 없으므로 확장이 불가능하다 ]
#  예)   print(g_a.__dict__)
#       print(print.__dict__)
