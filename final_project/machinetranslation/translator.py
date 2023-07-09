from deep_translator import MyMemoryTranslator 

def englishToFrench(englishText):

    frenchText = MyMemoryTranslator(source='english',\
                         target='french').translate(englishText)

    # print(f'Translating {englishText} to French: {frenchText}')
    return frenchText


def frenchToEnglish(frenchText):

    englishsText = MyMemoryTranslator(source='french', \
                         target='english').translate(frenchText)

    return englishsText