def count_a_letter(sentence, letter):
    if not letter.isalpha():
        return None
    if not sentence:
        return None
    
    count = 0
    for char in sentence:
        if char is letter or char == letter:
            count +=1
    
    return count
