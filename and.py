def and_relation(self, w1, w2, w3):

    if w1['pos_tag'] == 'NN' and w2['pos_tag'] == 'CC' and  w3['pos_tag'] == 'NN':
        return True
    elif w1['pos_tag'] == 'NNP' and w2['pos_tag'] == 'CC' and w3['pos_tag'] == 'NNP':
        return True
    elif w1['pos_tag'] == 'RB' and w2['pos_tag'] == 'CC' and w3['pos_tag'] == 'RB':
        return True
    elif w1['pos_tag'] == 'JJ' and w2['pos_tag'] == 'CC' and w3['pos_tag'] == 'JJ':
        return True
    else:
        return False
