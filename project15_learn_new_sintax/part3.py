f = open('text.txt', 'w')

f.write('''Hello
how
are
you
brouh?!''')
f.close()

f = open('text.txt', 'r')
for i in f:
    print(i)
f.close()
