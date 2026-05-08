for i in l:
    if var <= 100:
        temp[var] += str[i]
    else:
        chunks[idx] = temp
        idx += 1
        i -= 1
        var = 0
        
print(chunks)