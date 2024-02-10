def address_redirector(request):
    info_list = request.split()
    address = []

    if is_foreigner_address(info_list):
        address = foreigner_address(info_list)
    elif len(info_list) == 2:
        address = info_list
    else:
        address = bigger_address(info_list)

    return address

def bigger_address(info_list):
    name = number = ""
    list = []

    for word in info_list:
        if has_number(word):
            break
        name += word + " "

    name = name.strip() 
    list_without_name = info_list[len(name.split()):]
    for vector in list_without_name:
        number += vector + " " 
    number = number.strip()
    list.append(name)
    list.append(number)

    return list

def foreigner_address(info_list):
    name = number = ""
    list = []
    isNoAddress = False
    c = 0
    
    for vector in info_list:
        if vector == "No":
            isNoAddress = True
        else:
            c += 1

    if has_number(info_list[0]) and ',' in info_list[0]:
        number = info_list[0].replace(',', "")
        number_lenght = info_list[len(number.split()):]
        for vector in number_lenght:
            name += vector + " "
        name = name.strip()
        list.append(name)
        list.append(number) 
        return list
    
    elif info_list[0].isdigit():
        number = info_list[0]
        list_without_number = info_list[len(number.split()):]
        for vector in list_without_number:
            name += vector + " "
        name = name.strip()
        list.append(name)
        list.append(number) 
        return list
    
    elif isNoAddress:
        number_list = info_list[c-1:len(info_list)]
        for vector in number_list:
            number += vector + " "
        number = number.strip()
        list_without_number = info_list[:len(number.split())]
        for vector in list_without_number:
            name += vector + " "
        name = name.strip()
        list.append(name)
        list.append(number) 
        return list
    
    else:
        i = 0
        for vector in info_list:
            if ',' in vector:
                break
            else:
                i += 1
        name_list = info_list[:i+1]
        for vector in name_list:
            name += vector + " "
        name = name.strip()
        list_without_name = info_list[len(name.split()):]
        for vector in list_without_name:
            number += vector + " "
        name = name.replace(',', '')
        number = number.strip()
        list.append(name)
        list.append(number) 
        return list
    
def is_foreigner_address(info_list):
    for vector in info_list:
        if vector == ',' or ',' in vector:
            return True
        elif vector == 'No':
            return True
        elif vector.isdigit() and info_list[0] == vector:
            return True

def has_number(word):
    return any(char.isdigit() for char in word)
        
    
address = address_redirector("Calle 44 No 1991")

# {“Miritiba”, “339”}
# { “Babaçu”, “500”}
# {“Cambuí”, “123B”}
# {“Rio Branco”, “23”}
# {“Quirino dos Santos”, ”23 b”}
# {"Rue de la République", "4"}
# {"Broadway Av", "100"}
# {“Calle Sagasta”, “26”}
# {“Calle 44”, “No 1991”}
