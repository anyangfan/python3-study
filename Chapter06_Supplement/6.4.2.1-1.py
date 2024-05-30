def init(data):
    data["first"]={}
    data["middle"]={}
    data["last"]={}

storage={}
init(storage)
print(storage)

my_sister="Anne Lie Heland"
storage["first"].setdefault('Anne',[]).append(my_sister)
storage["middle"].setdefault('Lie',[]).append(my_sister)
storage["last"].setdefault('Heland',[]).append(my_sister)
print(storage)

def lookup(data,label,name):
    return data[label].get(name)

print(lookup(storage,"first","Anne"))
print(lookup(storage,"middle","Lie"))
print(lookup(storage,"last","Heland"))
print("\n")
def store(data,full_name):
    names = full_name.split()
    print(names)
    if len(names) == 2:
        names.insert(1,'')
    labels = 'first','middle','last'
    for label,name in zip(labels,names):
        people = lookup(data,label,name)
        if people:
            print("名字已存在")
            people.append(full_name)
            print(people)
        else:
            print("名字不存在,存储名字")
            data[label][name] = [full_name]
            print(data)
    print("\n\n")

store(storage,"An Yang Fan")
store(storage,"Chen shou xiang")
store(storage,"An Yang Fan")



