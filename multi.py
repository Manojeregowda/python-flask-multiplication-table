# multi.py

def multiplication_table(n):
    table = []
    for i in range(1, 11):
        table.append(f"{n} x {i} = {n*i}")
    return table
