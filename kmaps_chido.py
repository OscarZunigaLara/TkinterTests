for A in range(2):
    for B in range(2):
        for C in range(2):
            for D in range(2):
                not(A) ~A not A
                print("{}{}{}{}".format(A,B,C,D))