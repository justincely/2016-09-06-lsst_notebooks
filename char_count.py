import sys

a = 4

def letter_counter(message):
           
    frequencies = {}
         
    letter_set = set(message)
                 
    for item in letter_set:        
        if item.isalpha():            
            frequencies[item] = message.count(item)        
                 
    return frequencies

if __name__ == "__main__":
    input_argument = sys.argv[1]

    print(letter_counter(input_argument))
