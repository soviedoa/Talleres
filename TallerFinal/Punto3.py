def postorden(pre, ino):
    if pre == "":
        return ""
    if len(pre)==1:
        return pre
    postOrden = ""
    inoIzq = ""
    inoDer = ""
    preIzq = ""
    preDer = ""
    aux = 0
    while ino[aux] != pre[0]:
        inoIzq = inoIzq + ino[aux]
        aux+=1
    aux=0

    while aux<len(ino):
        inoDer = inoDer + ino[aux]
        aux+=1
    aux=0
    for i in pre:
        if i in inoIzq:
            preIzq = preIzq + i
        if i in inoDer:
            preDer = preDer + i
    postOrden = postOrden+postorden(preIzq, inoIzq)+postorden(preDer, inoDer)+pre[0]
    return postOrden
print(postorden("GEAIBMCLDFKJH", "IABEGLDCFMKHJ"))