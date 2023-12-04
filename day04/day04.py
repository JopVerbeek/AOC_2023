with open('input4.txt') as f:
    games = f.read().splitlines()

def check_points(line):
    score = 0
    matches = 0    
    card = int(game.split(':')[0].split('Card')[1].strip())
    win_nums =  [int(num) for num in line.split('|')[0].split(':')[1].strip().split(' ') if num != '']
    pulled_nums = [int(num) for num in line.strip().split('|')[1].strip().split(' ') if num != '']
    for num in pulled_nums:
        if num in win_nums:
            matches += 1
            if score >= 1:
                score *= 2
            elif score == 0:            
                score = 1
    return score, matches, card

card_info = {}
total = 0
for game in games:
    score, matches, card = check_points(game)
    card_info[card] = {"amount": 1, "matches": matches}
    total += score

for k, v in card_info.items():
    for i in range(v['amount']):
        for j in range(k + 1, k + v['matches'] + 1):
            card_info[j]['amount'] += 1

score = sum([v['amount'] for v in card_info.values()])
print(score)
