import sys

x = object()
print(type(x))
print(sys.getrefcount(x)) # 2

y = x
print(sys.getrefcount(x)) # 3 (함수 내부에서 일해서 1증가?!)


print("----- 레퍼런스 값 줄이기 -----")
del x
print(sys.getrefcount(y))
# symbol x 가 심볼테이블(네임스페이스)에서 삭제


print("-----  -----")



print("-----  -----")


