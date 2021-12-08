
spam =['apples', 'oranges', 'buddy', 'Niall']

def commacode(given_list):

    for i in range(len(given_list)-1):
        print(given_list[i] + ', ', end ="")
spam =['apples', 'oranges', 'buddy', 'Niall']

commacode(spam)
print('and ' + spam[-1])




