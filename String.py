
""" 
#Uppgift 1a: Räkna vokaler
def count_vowels(text):
    #those are  vowel in swedish a e i o u å ä ö   A E I O U Å Ä Ö
    vowel = ["a", "e", "i", "o", "u", "å", "ä", "ö"]
    count_vowels = 0
    for char in text.lower():
        if(char in vowel):
            count_vowels += 1
    
    return count_vowels




print(count_vowels("Hej världen"))
"""

""" 
#Uppgift 1b: Tar bort vokaler

def remove_vowel(text):
    vowel = ["a", "e", "i", "o", "u", "å", "ä", "ö"]
    no_vowel = ""

    for char in text:
        if(char not in vowel):
            no_vowel += char
    
    return no_vowel


print(remove_vowel("Hej världen"))
"""

""" 
#Uppgift 2: Titelcase

def till_titel_case(text):
    words = text.split()
    result = []

    for word in words:
       result.append(word.capitalize())
      
    return  " ".join(result)


print(till_titel_case("hej världen"))

"""

""" 
#Uppgift 3: Antal ord

def rakna_ord(text):
    words = text.split()
    count_word = len(words)
    
    return count_word

print(rakna_ord("Detta är en mening"))

"""


