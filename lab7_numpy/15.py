fp = open('input.txt', 'r')
fp.seek(0)

positive = 0
negative = 0
zero = 0

for number in fp.read().split():
    if int(number) == 0:
        zero += 1
    elif int(number) > 0:
        positive += 1
    elif int(number) < 0:
        negative += 1

outputFile = open('output.txt', 'w')
outputFile.write(f'1 {positive} -1 {negative} 0 {zero}')
