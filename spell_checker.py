from spellchecker import SpellChecker
word=input("write a word to check spelling : ")
corrector=SpellChecker()
if word in corrector:
    print("Correct")
else:
    corrected_word=corrector.correction(word)
    print(f"Correct Spelling is : {corrected_word}")
