import wikipedia

prompt = str(input('Enter title or search phrase: '))
while prompt != '':
    print(wikipedia.search(prompt))
    print(wikipedia.summary(prompt))
    print(wikipedia.page(prompt))
    prompt = str(input('Enter title or search phrase: '))



