D = [False,True, False, True, False,True,False,True,False,True,False,True, False, True, False, True]
C = [False, False, True, True, False, False, True,True,False,False, True,True,False, False, True,True]
B= [False,False,False,False,True,True,True,True,False,False,False,False,True,True,True,True]
A= [False,False,False,False,False,False,False,False, True,True,True,True,True,True,True,True]
print ("A B C D | A1 | A2 | F1 | F2 | F3")
for x in range(0,16):
    a = A[x]
    b = B[x]
    c = C[x]
    d = D[x]
    if (a == True):
        aa = 1
    else:
        aa = 0
    if (b == True):
        bb = 1
    else:
        bb = 0
    if (c == True):
        cc = 1
    else:
        cc = 0
    if (d == True):
        dd = 1
    else:
        dd = 0
    a1 = (not(a) and not(b) and (c) and (d)) or (not(a) and (b) and not(c) and (d)) or (not(a) and (b) and (c) and not(d)) or ((a) and not(b) and not(c) and (d)) or ((a) and not(b) and (c) and not(d)) or ((a) and (b) and not(c) and not(d))
    if (a1 == True):
        aa1 = 1
    else:
        aa1 = 0
    a2 = (not(a) and not(b)) and not(c) and (d) or (not(a) and not(b)) and (c) and not(d) or (not(a) and not(b)) and (c) and (d) or (not(a) and (b)) and not(c) and not(d) or (not(a) and (b)  and not(c) and (d)) or (not(a) and (b)) and (c) and not(d) or ((a) and not(b)) and not(c) and not(d) or ((a) and not(b)) and not(c) and (d) or ((a) and not(b)) and (c) and not(d) or ((a) and (b)) and not(c) and not(d)
    if (a2 == True):
        aa2 = 1
    else:
        aa2 = 0
    f1 = (not(b) and not(a ^ c)) or (b and (a ^ c ^ d))
    if (f1 == True):
        ff1 = 1
    else:
        ff1 = 0
    f2 = b and (a ^ c) or (not(a) and not(b) and (c^d)) or (not(c) and not(d) and(a^b)) or (a and c and ( b^d))
    if (f2 == True):
        ff2 = 1
    else:
        ff2 = 0
    f3= (not(b) and not(d) and not(a^c)) or (a ^ c ^ d)
    if (f3 == True):
        ff3 = 1
    else:
        ff3 = 0
    print(aa,bb,cc,dd,"|", aa1, " | ", aa2 ,"| ", ff1, "| " ,ff2, "| ",ff3)