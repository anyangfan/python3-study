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
