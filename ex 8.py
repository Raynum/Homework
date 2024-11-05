# ex 8
total = 0
letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
print(letters)

def count():
    global total
    for item in letters:
        if item == 'a':  
            total +=1
            print(total)

count()
print("Total: ", total)
