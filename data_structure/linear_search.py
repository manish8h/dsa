# linear search

test = {'input': {
    'cards': [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    'query': 8},
    'output': 5
}

tests = [test]

tests.append({'input': {
    'cards': [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    'query': 13},
    'output': 0
})

tests.append({'input': {
    'cards': [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    'query': 1},
    'output': 12
})

tests.append({'input': {
    'cards': [13, 12, 11, 10, 9, 8, 7],
    'query': 1},
    'output': -1
})
tests.append({'input': {
    'cards': [13, 12, 11, 10, 9, 9, 9, 8, 7],
    'query': 9},
    'output': 4
})

tests.append({'input': {
    'cards': [],
    'query': 1},
    'output': -1
})


def locate_card(cards, query):
    position = 0

    while position < len(cards):
        if cards[position] == query:
            return position

        position += 1

    return -1


v = locate_card(**test['input'])
print(v)


def test_inputcode():
    for test in tests:
        print(locate_card(**test['input']) == test['output'])


test_inputcode()

# =========================
# binary Search
# =========================







