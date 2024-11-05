#Ex 10 
nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
print("Before: ", nums)
       

def newlist():
    After=[]
    for items in nums:
        if items not in After:
            After.append(items)
            print("After: ", After)  #in loop to show step by step key values taken out.
newlist()
        
        
