def hearts(seed:int):
    cards:list[dict] = []
    i:int = 0
    seed: int = 425
    players:list[list[dict]] = [[],[],[],[]]
    table: list[dict] = []

    for deck in ['H','C','D','S']:
        for num in range(2,11):
            cards.append({'deck':deck,'num':num,'value':num,'name':''.join([str(num), deck])})
        cards.append({'deck':deck,'num':'J','value':11,'name':"".join(['J',deck])})
        cards.append({'deck':deck,'num':'Q','value':12,'name':"".join(['Q',deck])})
        cards.append({'deck':deck,'num':'K','value':13,'name':"".join(['K',deck])})
        cards.append({'deck':deck,'num':'A','value':14,'name':"".join(['A',deck])})
    
    while len(cards) > 0:
        number = get_random_number(seed,cards)
        players[i].append(cards.pop(number))
        i = (i + 1) % len(players)

    for player in players:
        table.append(player[0])
    
    deck = table[0]['deck']
    winner_value = table[0]['value']
    winner = 0

    for player in range(1,4):
        if deck == table[player]['deck']:
            if winner_value < table[player]['value']:
                winner_value = table[player]['value']
                winner = player

    print("Cards played: ")
    for card in table:

def get_random_number(seed:int, cards:list) -> int:
    seed = (seed * 997) % 1000
    random = (seed * 503) % 1000 / 1000
    number = int(random * len(cards))
    return number

seed = int(input("Enter a random number: "))
hearts(seed)
