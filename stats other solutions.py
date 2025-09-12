def count_words(text):
    count = 0
    splitted = text.split()
    for word in splitted:
        count+=1 
        #print(f"word:{word} | count:{count}")
    return count

#def count_characters(text):
    new_count = 0
    characters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ",".",","]
    ch_count = 0
    char_dict = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0," ":0,".":0,",":0} 
    lowered = text.lower()
    words = lowered.split()
    for word in words:
        #print(word)
        #print(f"character dictionary:{char_dict}")
        for i in range(0,len(characters)):
            new_count = word.count(characters[i])
            ch_count = char_dict.get(characters[i])
            char_dict[characters[i]] = ch_count + new_count
            #print(f"character: {characters[i]} counter: {new_count}")
    return char_dict

#def count_characters(text):
    new_count = 0
    characters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ",".",","]
    char_dict = {} 
    lowered = text.lower()
    print(f"length: {len(lowered)}")
    for i in range(0,len(characters)):
        new_count = lowered.count(characters[i])
        char_dict[characters[i]] = new_count
    return char_dict

def count_characters(text):
    new_count = 0
    characters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ",".",","]
    char_dict = {} 
    lowered = text.lower()
    print(f"length: {len(lowered)}")
    for i in range(0,len(characters)):
        for low in lowered:
            #print(f"low: {low}")  low is a character
            if characters[i] == low: 
                new_count += 1
        char_dict[characters[i]] = new_count
        new_count = 0
                
    return char_dict


