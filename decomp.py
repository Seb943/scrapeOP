def getFromTxt():
    result = []
    with open('file.txt', 'r') as f:
        for line in f.readlines():
            quote = 0
            element = ''
            elements = []
            for letter in line:
                if letter == "'":
                    if quote == 1:
                        elements += [element]
                        element = ''
                    quote = 1 - quote
                    continue
                if quote == 1:
                    element += letter
            result += [elements]
    return result

def getScore(result):
    score = dict()
    for elements in result:
        score[elements[0]] = dict()
        scores = elements[-1]
        if 'retired' in scores:
            print('ok')
            score[elements[0]]['setP1'] = scores.split(' (')[0]
            score[elements[0]]['setP2'] = ''
        else:
            score[elements[0]]['setP1'] = scores[scores.find(':') - 1]
            score[elements[0]]['setP2'] = scores[scores.find(':') + 1]
        jeux = scores.split('(')[1][: -1]
        listJeux = jeux.split(', ')
        score[elements[0]]['jeux'] = dict()
        for i in range(len(listJeux)):
            score[elements[0]]['jeux']['set' + str(i + 1) + 'P1'] = listJeux[i].split(':')[0][0]
            score[elements[0]]['jeux']['set' + str(i + 1) + 'P2'] = listJeux[i].split(':')[1][0]
        for i in range(len(listJeux), 5):
            score[elements[0]]['jeux']['set' + str(i + 1) + 'P1'] = 'NA'
            score[elements[0]]['jeux']['set' + str(i + 1) + 'P2'] = 'NA'
    #print(score['Gasquet R. - Pospisil V.'])
    return score