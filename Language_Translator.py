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
   
}

igala_dictionary = {
"hello": "àgba",
"bye" : "chegbà tó bà",
"good morning" : "olodu",
"good evening" : "olane",
"welcome" : "olale",
"thank you" : "Nagó",
"food" : "Ujewu",
"well done" : "Olacolo",
"Water" : "Omi",
"come" : "wá",
"go to bed" : "na dachi",
"father" : "attah",
"mother" : "iye",
"boy" : "Ikolobia",
"girl" : "Ibele",
"money" : "okó",
"what is your name" : "Kí ni orukó ẹ",
"plate" : "uchibu",
"good afternoon" : "óroka",
"school" : "chubulu",

}

print("LANGUAGE TRANSLATOR")
print()
print("select language you want to translate among : Yoruba, Igbo, Zulu, Hausa, Igala")
print() 
language = input("INPUT LANGUAGE HERE : ")
print()
if language == "Yoruba".lower().upper():
   translation = input("Input yoruba word or phrase : ").lower().upper()
   print(yoruba_dictionary[translation])

elif language == "Igbo".lower().upper():
    translation = input("Input igbo word or phrase : ").lower().upper()
    print(igbo_dictionary[translation])

elif language == "Zulu".lower().upper():
    translation = input("Input zulu word or phrase :").lower().upper()
    print(zulu_dictionary[translation])

elif language == "Hausa".lower().upper():
    translation = input("Input hausa word or phrase :").lower().upper()
    print(hausa_dictionary[translation])

elif language == "Igala".lower().upper():
    translation = input("Input igala word or phrase :").lower().upper()
    print(igala_dictionary[translation])

else:
    print()
    
