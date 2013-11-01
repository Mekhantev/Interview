def merge(la: list, lb: list):
    lb_i = 0
    la_i = 0
    la_end = len(la) - 1
    while la_i <= la_end:
        while lb[lb_i] < la[la_i]:
            la.insert(la_i, lb[lb_i])
            lb_i += 1
            la_i += 1
            la_end += 1
        la_i += 1
    lb_end = len(lb)
    while lb_i < lb_end:
        la.append(lb[lb_i])
        lb_i += 1