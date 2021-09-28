# Чтение api key из файла
def GetApiKey():
    with open("api_key.txt", 'r') as file:
        return file.readline()
