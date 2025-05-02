def NULL_not_found(object: any) -> int:
    object_type =  str(type(object))
    if isinstance(object, float):
        display = "Cheese: "+ str(object) + " " + object_type
    elif isinstance(object, bool):
        display = "Fake: " + str(object) + " " + object_type
    elif isinstance(object, int):
        display = "Zero: " + str(object) + " " + object_type
    elif object is None:
        display = "Nothing: " + str(object) + " " + object_type
    elif isinstance(object, str) and object == '':
        display = "Empty: " + object_type
    else:
        display = "Type not found"
        
    print(display)
    return 1