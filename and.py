def and_relation(self, w1, w2):

    if w1['pos_tag'] == 'NN' and w2['pos_tag'] == 'NN':
        return True
    elif w1['pos_tag'] == 'NNP' and w2['pos_tag'] == 'NNP':
        return True
    elif w1['pos_tag'] == 'RB' and w2['pos_tag'] == 'RB':
        return True
    elif w1['pos_tag'] == 'JJ' and w2['pos_tag'] == 'JJ':
        return True
    else:
        return False
