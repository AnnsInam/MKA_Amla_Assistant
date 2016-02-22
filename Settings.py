import Labels

def LoadSettings():

    settings = []

    fopen = open('settings.ini', 'r')

    while(True):
        readline = fopen.readline()
        if 'Language' in readline:
            for i in range(len(Labels.Languages)):
                if Labels.Languages[i] in readline[10:]:
                    LangInd = i
                    break

        if 'Username' in readline:
            if 'None' in readline[10:]:
                Username = ''
                break
            else:
                Username = readline[11:]
            break

    settings.append(LangInd)
    settings.append(Username)

    return settings

def WriteSettings(SettingName, Setting):
    with open('settings.ini', 'r') as file:
        # read a list of lines into data
        data = file.readlines()

    Ind = 0
    while(True):
        if SettingName in data[Ind]:
            break
        else:
            Ind += 1

    # now change the 2nd line, note that you have to add a newline
    data[Ind] = '{} = {}\n'.format(SettingName, Setting)

    # and write everything back
    with open('settings.ini', 'w') as file:
        file.writelines( data )

