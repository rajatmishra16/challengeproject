def getObjectKeys(object, key) :

    keys = key.split('/')
    obj = object
  
    for ikey in keys: 
        for objKey,v in obj.items():
     #       print(objKey)
      #      print(v)
 
            if(ikey  in objKey) :
                     continue

        obj = v;


    return obj;

object = {"a":{"b":{"c":"d"}}}
key=str(input("Enter Key(in format,like a or a/b or a/b/c):"))
test=getObjectKeys(object,key)
print(test)