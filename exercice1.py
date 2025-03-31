# Imports
from collections import Counter
from string import ascii_uppercase as alphabet # Récupération de l'alphabet en majuscules via string.ascii_uppercase
from pathlib import Path

def oldMessage():
    old_message = "Strawberry quince olive fig bliss peach ximenia victoria grape kiwi cherry feijoa cloud fig nectarine guava blackberry papaya kumquat eggplant watermelon blackberry strawberry rhubarb lime feijoa eggplant ice apricot nutmeg tamarillo ugni victoria victoria huckleberry yellow zest elderflower zucchini nebula apricot ugly jackfruit ugli raspberry zinfandel feijoa vanilla ivory ugli quandary ximenia blackberry tamarind quince kale avocado oasis eggplant jujube elderberry mulberry raspberry elderberry feijoa nut abbey kiwi jackfruit ugli yuzu blackberry mulberry orange waxberry quince vine marvel jackfruit strawberry kale guava mandarin ugli mulberry nutmeg serene zest dragonfruit jujube victoria zest kumquat hawthorn waxberry ocean xerophyte lime fig cantaloupe nutmeg feijoa apple tamarillo lychee hawthorn vine tamarillo palm kumquat elderflower kale ugni nut kiwi wildberry fennel garden gooseberry mandarin hawthorn kiwi date xerophyte elderflower raspberry elderberry pearl onion kale ugni strawberry zucchini banana hawthorn mulberry feast tangerine jackfruit vanilla indian ugni olive satsuma ugly papaya guava eagle nectarine wildberry wildberry lemon dragonfruit saffron haven blackberry strawberry grape jujube tamarind watermelon quandong hawthorn persimmon lemon harmony kale elderflower vine date persimmon quandong dragonfruit quartz mulberry quince zinfandel kale cranberry lychee jade tamarillo papaya gooseberry ugly eggplant elderberry jackfruit cranberry elderberry cactus honeydew vine kale tangerine persimmon rasp zest dragonfruit jujube blackberry ximenia daisy cantaloupe papaya hawthorn nut nectarine apricot durian hawthorn mango meadow orange indian zinfandel lychee tamarillo ugni zest fennel satsuma ugli jackfruit elderberry jazz durian jujube grape mulberry xerophyte yam kumquat apple cranberry quest watermelon dragonfruit apricot jujube papaya orange mandarin rhubarb watermelon banana falcon apple yuzu kumquat elderberry nectarine apple yuzu satsuma dragonfruit elderflower xerophyte cantaloupe hawthorn luna jujube elderflower jackfruit zest yam dragonfruit banana rasp date rain kale tamarillo tamarillo lime ximenia raspberry strawberry fennel ximenia lime lagoon satsuma grape strawberry zest ugly nut indian cherry kale zinfandel huckleberry tamarillo zinfandel dawn quandong blueberry blueberry raspberry banana papaya satsuma ximenia watermelon glow dragonfruit zucchini durian guava olive yam papaya nest eggplant strawberry cranberry indian strawberry rasp watermelon koala nut cantaloupe feijoa xerophyte quince apricot river tamarillo orange ugly zest jujube lychee kiwi mandarin mandarin breeze avocado wildberry zucchini jackfruit gooseberry durian waxberry wildberry echo nut cherry quandong lychee blackberry huckleberry amber mandarin xigua quandong banana mango"
    filling_words_old_message = {'rhubarb', 'quince', 'watermelon', 'ximenia', 'nut', 'zucchini','blackberry', 'vine', 'cranberry', 'durian', 'papaya', 'huckleberry', 'jujube', 'xerophyte', 'elderberry','tangerine', 'satsuma', 'kiwi', 'victoria', 'lime', 'saffron', 'ugni', 'rasp', 'kale', 'avocado','xigua', 'ugly', 'waxberry', 'eggplant', 'honeydew', 'lychee', 'dragonfruit', 'zinfandel','raspberry', 'guava', 'indian', 'fig', 'orange', 'yuzu', 'date', 'tamarind', 'yam', 'strawberry','hawthorn', 'apple', 'nectarine', 'cherry', 'fennel', 'elderflower', 'quandary', 'blueberry','quandong', 'zest', 'wildberry', 'yellow', 'apricot', 'onion', 'cantaloupe', 'nutmeg','persimmon', 'mandarin', 'olive', 'lemon', 'tamarillo', 'ugli', 'mango', 'grape', 'banana', 'jackfruit','gooseberry', 'vanilla', 'mulberry', 'kumquat', 'peach', 'feijoa'}

    cleanText = old_message.lower().replace('.', '').replace(',', '')  # Suppression des points et virgules
    splittedText = cleanText.split(" ")
    sortedText = sorted(Counter(splittedText))                  # Tri par ordre alphabétique et suppression de doublons

# Supprime les mots de remplissage dans le texte trié
for filling_word in filling_words_old_message:
    if filling_word in sortedText:
        sortedText.remove(filling_word)

    keysDict = {} # Initialisation du dictionnaire qui contiendra les clefs pour décoder le message

    # Assignation des mots à des clefs
    for i in range(len(alphabet)):              # Les 26 premières clefs seront assignées aux lettres de l'alphabet précédemments importées
        keysDict[alphabet[i]] = sortedText[i]
    for j in range(10):                         # Les autres clefs seront assignées à des numéros
        keysDict[j] = sortedText[i+j]
                
    return(keysDict)    


def myMessage(keysDict):
    # Récupération du message codé
    file = Path("message_code.txt") # Récupération du fichier
    text = file.read_text()         # Récupération du contenu du fichier

    # Traitement du texte du message codé
    cleanText = text.lower().replace('.', '').replace(',', '')  # Suppression des points et virgules
    splittedText = cleanText.split(" ")                         # Récupération des différents mots dans une liste
    sortedText = sorted(Counter(splittedText))                  # Tri par ordre alphabétique et suppression de doublons

    decryptedText = ""


    for cryptedWord in splittedText:
        for value, key in keysDict.items():
            if cryptedWord == key:
                decryptedText += str(value)     

    print(decryptedText)

# myMessage(oldMessage())

print(oldMessage())