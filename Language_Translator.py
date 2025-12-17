#fasola omogbolahan
yoruba_dictionary  = {
    "hello": "Ẹ ǹlẹ́",
    "bye" : "Ó dàbọ̀",
    "good morning" : "e kaaro",
    "good evening" : "ka a ale",
    "welcome" : "kaabo",
    "thank you" : "e dupe",
    "food" : "Ounjẹ", 
    "well done" : "daradara ṣe",
    "how are you" : "Bawo ni",
    "come" : "wá",
    "go" : "lọ",
    "father" : "baba",
    "mother" : "iya",
    "boy" : "ọmọkunrin",
    "girl" : "omobirin",
    "money" : "owo",
    "what is your name" : "Kí ni orúkọ rẹ",
    "brother" : "arakunrin",
    "sister" : "arabinrin",
    "school" : "ile-iwe",

}

igbo_dictionary = {
    "hello": "kedu",  
    "Thank you": "Imena",
    "sorry": "Ndo",
    "water": "Mniri",
    "Goodbye": "Ka omesia",
    "food": "Nri",
    "House": "Ulo",
    "Please": "Biko",
    "Family": "Ezinuio",
    "Mother": "Nne",
    "Father": "Nna",
    "Child": "Nwa",
    "Friend": "Enyi",
    "Day": "Ubochi",
    "Night": "Abali",
    "One": "Otu",
    "Two": "Abuo",
    "Good": "Oma",
    "Yes": "Ee",
    "Love": "Ihunaya"
   
}

zulu_dictionary = {
    "good morning" : "sawubona",
    "come" : "woza",
    "enter" : "faka",
    "say" : "ukuthi",
    "go" : "hamba",
    "wash" : "ukuhlamba",
    "big" : "inkulu",
    "dog" : "inja",
    "food" : "ukudla",
    "short" : "okufutshane",
    "brother" : "mfowethu",
    "hear" : "zwa",
    "talk" : "inkulumo",
    "sister" : "dadewethu",
    "sing" : "hlabelelani",
    "run" : "gijima",
    "fan" : "umlandeli",
    "car" : "imoto",
    "chair" : "isihlalo",
    "eat" : "yidla",

}

hausa_dictionary = {
    "hello": "Sannu",
    "bye": "Sai anjima",
    "good morning": "Ina kwana",
    "good evening": "Barka da yamma",
    "welcome": "Maraba",
    "thank you": "Nagode",
    "food": "Abinci",
    "how are you": "Yaya kake?",
    "come": "Zo",
    "go": "Tafi",
    "father": "Uba",
    "mother": "Uwa",
    "boy": "Yaro",
    "girl": "Yarinya",
    "money": "Kudi",
    "what is your name": "Menene sunanka?",
    "brother": "Dan'uwa",
    "sister": "Yar'uwa",
    "school": "Makaranta",
}

igala_dictionary = {

}

print("LANGUAGE TRANSLATOR")
print()
print("select language you want to translate among : Yoruba, Igbo, Zulu, Hausa, Igala")
print() 
language = input("INPUT LANGUAGE HERE : ")
print()
if language == "Yoruba" or "YORUBA" or "yoruba":
   translation = input("Input yoruba word or phrase : ").lower() or upper()
   print(yoruba_dictionary[translation])

elif language == "Igbo" or "IGBO" or "igbo":
    translation = input("Input igbo word or phrase : ").lower() or upper()
    print(igbo_dictionary[translation])

elif language == "Zulu" or "ZULU" or "zulu":
    translation = input("Input zulu word or phrase :").lower() or upper()
    print(zulu_dictionary[translation])

elif language == "Hausa" or "HAUSA" or "hausa":
    translation = input("Input hausa word or phrase :").lower() or upper()
    print(hausa_dictionary[translation])

elif language == "Igala" or "IGALA" or "igala":
    translation = input("Input igala word or phrase :").lower() or upper()
    print(igala_dictionary[translation])

else:
    print( "THIS WORD NOT AVAILABLE")
    
