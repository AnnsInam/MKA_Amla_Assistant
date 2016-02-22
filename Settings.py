import Labels

def LoadSettings():

    settings = []

    fopen = open('settings.ini', 'r')

    Language = fopen.readline()

    for i in range(len(Labels.Languages)):
        if Labels.Languages[i] in Language[10:]:
            LangInd = i
            break
        else:
            LangInd = 0

    settings.append(LangInd)

    return settings

def WriteSettings(Ind, Language):

    with open('settings.ini', 'r') as file:
        # read a list of lines into data
        data = file.readlines()

    # now change the 2nd line, note that you have to add a newline
    data[Ind] = 'Language = {}\n'.format(Language)

    # and write everything back
    with open('settings.ini', 'w') as file:
        file.writelines( data )

