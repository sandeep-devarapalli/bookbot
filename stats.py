def get_num_words(text):
    words = text.split()
    return len(words)

def charater_counts(text):
    lower_text = text.lower()
    character_dict = {}
    
    for char in lower_text:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1

    return character_dict

def print_dict_sorted_by_value(d):
    # Sort the dictionary items by value in descending order
    sorted_items = sorted(d.items(), key=lambda item: item[1], reverse=True)
    
    # Print each key-value pair
    for key, value in sorted_items:
        if key.isalpha():
            print(f"{key}: {value}")