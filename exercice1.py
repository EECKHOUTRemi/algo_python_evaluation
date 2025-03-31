from collections import Counter
import string

alphabet = string.ascii_uppercase
text = "Against after outside and on against beside under from before amber from beyond before of in beyond outside with ivory outside without by inside between abbey after the on in during against against under from beside lagoon through under under on with without and harmony beside at by over the near between beside by outside cactus of under beside through in after in against with in cactus at against a a in under from before before bliss through without without near by falcon at through and outside at from dawn during before in on through the harmony inside beyond against before with from inside with by on koala beyond on and of under from jazz beyond over inside near outside the of over on ivory beyond under with beside at and garden with beside on beside from inside eagle after without over under of oasis beyond at of and of inside by a palm over from and before outside by ocean at against a a on during and beside serene and outside beside outside through between the during inside by jazz the outside after beyond against inside koala by between beside with outside through between abbey before at the on before jade beside inside under with over and beyond ivory outside before between near after with beside cactus on after a without by without without from under koala in by before during during without jade under after over after in after after outside jade by the between by during during during on between near eagle of outside in beyond between by inside inside inside feast and beyond outside near over after cactus and before without and outside inside marvel beside without of in against under beyond from beside cactus the by over at before and in and ivory during inside near near by bliss in near during from with of over on a during eagle a on and outside through inside of without through without bliss of under without a on cactus at near near after through during near during over."
cleanText = text.lower().replace('.', '').replace(',', '')
splittedText = cleanText.split(" ")

counter = sorted(list(Counter(splittedText)))
keysDict = {}

i = 0
for i in range(len(alphabet)):
    keysDict[alphabet[i]] = counter[i]
for j in range(len(counter)-26):
    keysDict[j] = counter[i+j]

print(keysDict)