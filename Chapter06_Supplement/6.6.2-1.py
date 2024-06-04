def search(sequence,number,lower,upper):
    if upper==None:
        upper=len(sequence)-1
    if lower==upper:
        assert number==sequence[upper]
        return upper
    else:
        middle=(lower+upper)//2
        if number==sequence[middle]:
            return middle
        elif number<sequence[middle]:
            if lower==middle:
                return None
            else:
                return search(sequence,number,lower,middle-1)
        else:
            if upper==middle:
                return None
            else:
                return search(sequence,number,middle+1,upper)

sequence=[1,2,3,4,5,6,7,8,9,10]
print(search(sequence,11,0,None))