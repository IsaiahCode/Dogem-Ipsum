from random import randint

dog_words = [
    'pet', 'puppy', 'dog', 'poodle', 'dachshund', 'pooch',
    'corgi', 'good boy', 'doggie', 'beagle', 'canine', 'bone',
    'treat', 'doggy', 'pug', 'leash', 'pup', 'pupper dog', 'bark',
    'woof', 'howl', 'hungry', 'so hungry', 'food?', 'food now?',
    'treat', 'walk', 'wannagofora', 'sit', 'roll over', 'play dead',
    'bang!', 'wait', 'fido', 'doggo', 'doge', 'hound', 'bowwow', 'tail-wag',
    'sniff', 'lick', 'slobber', 'ruff', 'mutt', 'dawg', 'hound', 'fetch',
    'husky', 'whine', 'pooch'
]


def dogerize(word):
    random_pos = randint(0, len(dog_words) - 1)
    return f'{word} {dog_words[random_pos]}'


paragraphs = int(input('How many paragraphs of dogem ipsum?:'))

with open('resources/ipsum.txt') as ipsum_original:
    items = ipsum_original.read().split()

    for n in range(paragraphs):
        dog_text = list(map(dogerize, items))
        with open('output/dogem_ipsum.txt', 'a') as ipsum_dogem:
            ipsum_dogem.write(' '.join(dog_text) + '\n\n')
    print('Thank you. Please locate your Dogem Ipsum in the /output folder.')

input('Press ENTER to quit.')
