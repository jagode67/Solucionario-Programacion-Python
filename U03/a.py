def criterio(a):
    return len(a)

s={"aaaa","bb","ccc"}
print(s)
lista=sorted(s,reverse=True,key=criterio)
print(lista)
