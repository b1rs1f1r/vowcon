vowel="aeıioöuüAEIİOÖUÜ"
consonant="bcçdfgğhjklmnprsştvyzBCÇDFGĞHJKLMNPRSŞTVYZ"

vowels=""
consonants=""

word=input("Enter a text: ")

for x in word:
	if x in vowel:
		vowels+=x
	else:
		consonants+=x

print("Vowels: ",vowels)
print("Consonants: ",consonants)