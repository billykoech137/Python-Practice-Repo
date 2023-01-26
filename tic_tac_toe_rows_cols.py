
def get_row_col(s):
    row = {"1": 0, "2": 1, "3": 2}
    col = {"A": 0, "B": 1, "C": 2}
    
    lc = []
    for i in s:
        if i in row.keys():
            lc.append(row[i])
    
    for i in s:
        if i in col.keys():
            lc.append(col[i])
    
    tc = tuple(lc)

    return tc

print(get_row_col("C1"))