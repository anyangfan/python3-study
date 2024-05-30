def print_params_4(x,y,z=3,*pospar,**keypar):
    print(x,y,z)
    print(pospar)
    print(keypar)

print_params_4(1,2,2,5,5,5,foo=1,bar=2)
print("\n")
print_params_4(1,2)
print("\n")

def init(data):
    data["first"]={}
    data["middle"]={}
    data["last"]={}

def lookup(data,label,name):
    return data[label].get(name)

def store(data,*full_names):
    for full_name in full_names:
        names = full_name.split()
        print(names)
        if len(names) == 2:
            names.insert(1,'')
        labels = 'first','middle','last'
        for label,name in zip(labels,names):
            people = lookup(data,label,name)
            if people:
                print("名字已存在")
                if full_name not in people:
                    people.append(full_name)
                #print(people)
            else:
                print("名字不存在,存储名字")
                data[label][name] = [full_name]
                #print(data)
        
        print("people:")
        print(people)
        print("data:")
        print(data)
        print("\n")

storage={}
init(storage)
print(storage)

store(storage,"An Yang Fan")
store(storage,"Chen shou xiang")
store(storage,"An Yang Fan")

print(storage)