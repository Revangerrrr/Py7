def reverse():
    fp = open('input.dat', 'rb')
    outputFile = open('output.dat', 'wb')
    fp.seek(0)
    outputFile.write(fp.read()[::-1])


reverse()
