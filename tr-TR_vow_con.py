sesli_harfler="aeıioöuüAEIİOÖUÜ"
sessiz_harfler="bcçdfgğhjklmnprsştvyzBCÇDFGĞHJKLMNPRSŞTVYZ"

sesliler=""
sessizler=""

kelime=input("Bir kelime girin: ")

for x in kelime:
	if x in sesli_harfler:
		sesliler+=x
	else:
		sessizler+=x

print("Sesli harfler: ",sesliler)
print("Sessiz harfler: ",sessizler)