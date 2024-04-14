import sys
def encrypt(inputfilename,outputfilename):
    encrypt={
    "A":100,"a":101,"B":110,"b":111,"C":120,"c":121,"D":130,"d":132,"E":148,
    "e":200,"F":218,"f":219,"G":220,"g":221,"H":230,"h":229,"I":240,"i":247,
    "J":300,"j":301,"K":310,"k":311,"L":320,"l":321,"M":330,"m":331,"N":340,
    "n":401,"O":410,"o":411,"P":434,"p":464,"Q":430,"q":431,"R":440,"r":441,
    "S":412,"s":501,"T":519,"t":511,"U":520,"u":521,"V":530,"v":531,"W":540,
    "w":582,"X":601,"x":610,"Y":611,"y":620,"Z":636,"z":660,".":1100,"?":1084}
    def split_file_into_characters(inputfilename):
            with open(inputfilename, 'r') as file:
                content = file.read()
                character = [char for char in content]
                characters=character[::-1]
                return characters
    def replace_characters_with_numbers(characters):
        replaced_characters = []
        for char in characters:
            if char in encrypt:
                replaced_characters.append(encrypt[char])
            else:
                replaced_characters.append(char)
        return replaced_characters
    def perform_modulo(numbers, divisor, divisor2):
        modulo_results = []
        for num in numbers:
            if num < 1000:
                modulo_results.append(num % divisor)
            else:
                modulo_results.append(num % divisor2)
        return modulo_results
    def write_characters_to_file(modulo_results, outputfilename):
            with open(outputfilename, 'w') as file:
                for num in modulo_results:
                    digits = [int(digit) for digit in str(num)]
                    digits1= digits[::-1]
                    file.write(''.join(map(str, digits1)))
    characters = split_file_into_characters(inputfilename)
    replaced_characters = replace_characters_with_numbers(characters)
    numbers = [int(char) for char in replaced_characters if str(char).isdigit()]
    divisor = 69 
    divisor2 = 143
    modulo_results = perform_modulo(numbers, divisor,divisor2)
    write_characters_to_file(modulo_results, outputfilename)

def decrypt(inputfilename):
    decrypt = {
        100: "A", 101: "a", 110: "B", 111: "b", 120: "C", 121: "c", 130: "D", 132: "d", 148: "E",
        200: "e", 218: "F", 219: "f", 220: "G", 221: "g", 230: "H", 229: "h", 240: "I", 247: "i",
        300: "J", 301: "j", 310: "K", 311: "k", 320: "L", 321: "l", 330: "M", 331: "m", 340: "N",
        401: "n", 410: "O", 411: "o", 434: "P", 464: "p", 430: "Q", 431: "q", 440: "R", 441: "r",
        412: "S", 501: "s", 519: "T", 511: "t", 520: "U", 521: "u", 530: "V", 531: "v", 540: "W",
        582: "w", 601: "X", 610: "x", 611: "Y", 620: "y", 636: "Z", 660: "z", 1100: ".", 1084: "?"}
    def split_file_into_characters(inputfilename):
            with open(inputfilename, 'r') as file:
                content = file.read()
                encryptedtext = [char for char in content]
                return encryptedtext
    def fliptext(encryptedtext):
        pairs = [encryptedtext[i:i+2] for i in range(0, len(encryptedtext), 2)]
        flippedencryptedtexts = [[int(char) for char in pair[::-1]] for pair in pairs]
        flippedencryptedtext=flippedencryptedtexts[::-1]
        return flippedencryptedtext
    def unmodelo(flippedencryptedtext):
        with open(outputfilename, 'w') as file:
            for pair in flippedencryptedtext:
                pair_str = ''.join(map(str, pair)) 
                pair_int = int(pair_str)
                if pair_int == 99 or pair_int == 83:
                    while pair_int not in decrypt:
                        pair_int=pair_int+143
                else:
                    while pair_int not in decrypt:
                        pair_int=pair_int+69
                key=pair_int
                value = decrypt.get(key)
                file.write(value)

    encryptedtext = split_file_into_characters(inputfilename)
    flippedencryptedtext = fliptext(encryptedtext)
    unmodelo(flippedencryptedtext)

inputfilename = input("Type in your file name for input: ")
outputfilename =input("Type in your file name for output: ")  
y=input("Do you want to encrypt of decrypt: ")
if y == "encrypt":
    encrypt(inputfilename,outputfilename)
elif y=="decrypt":
    decrypt(inputfilename)
     


