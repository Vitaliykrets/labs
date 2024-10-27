def capitalize_custom(string, indexes):
    result = ""  
    alphabet = "abcdefghijklmnopqrstuvwxyz" 
    uppercase_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for x in range(len(string)):  
        if x in indexes:  
          
            letter_index = -1
            for y in range(len(alphabet)):
                if string[x] == alphabet[y]:
                    letter_index = y
                    break
            
            if letter_index != -1:  
                result += uppercase_alphabet[letter_index]  
            else:
                result += string[x]  
        else:
            result += string[x]  
    
    return result 

input_string = "i am learning to program to python"
indixes = [0, 2, 5, 14, 17, 25, 28]  
result = capitalize_custom(input_string, indixes)
print(result)

