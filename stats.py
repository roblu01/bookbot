def count_words(text):
    count = 0
    splitted = text.split()
    for word in splitted:
        count+=1 
        #print(f"word:{word} | count:{count}")
    return count

def sort_on(dict_item):
    return dict_item["num"]

def convert_and_sort_char(dict):
    char_list=[]
    for di in dict:
        num = dict[di]
        temp_dict = {"char":di,"num":num}
        char_list.append(temp_dict)

    char_list.sort(reverse=True, key=sort_on)
    return char_list

def count_characters(text):
    char_dict = {} 
    lowered = text.lower()
    for low in lowered:
        if low in char_dict: 
            char_dict[low] += 1
        else:
            char_dict[low] = 1
                
    return char_dict
