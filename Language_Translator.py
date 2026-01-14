
yoruba_dictionary  = { # FASOLA OMOGBOLAHAN BHU/25/04/05/0020 
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

igbo_dictionary = { #ANYANWU KELVIN
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

zulu_dictionary = { #CHUKWUBUIKEM EMERALD
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

hausa_dictionary = { #WILLIAM PANAM
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

igala_dictionary = { #EBIJE SHEKINAH PRINCESS
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

dictionaries = {
    "yoruba": yoruba_dictionary,
    "igbo": igbo_dictionary,
    "zulu": zulu_dictionary,
    "hausa": hausa_dictionary,
    "igala": igala_dictionary,
}

#FASOLA OMOGBOLAHAN BHU/25/04/05/0020
st.title("Language Translator")
st.markdown("## Welcome to the Language Translator App")

language = st.sidebar.selectbox(
    "Select language you want to translate among:", dictionaries.keys())

if language:
    selected_dictionary = dictionaries[language]
    word_to_translate = st.selectbox(
        f"Select a word to translate to {language.capitalize()}:", 
        options=[""] + list(selected_dictionary.keys()))
if st.button("Translate"):
    if word_to_translate:
        translation = selected_dictionary.get(word_to_translate, "Translation not found.")
        st.divider()
        st.subheader(f"The translation of '{word_to_translate}' in {language.capitalize()} is: {translation}")
        st.success(f"**{translation}**")
        st.balloons()
        st.write ("Thank you for using the Language Translator App!")
        st.feedback()
