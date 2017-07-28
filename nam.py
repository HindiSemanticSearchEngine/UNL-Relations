def nam_relation(self, w1, w2):

    if w1['pos_tag'] == 'NN' and  w2['pos_tag'] == 'NNP':
        return True
    elif w1['pos_tag'] == 'NNP' and w2['pos_tag'] == 'NN':
        return True
    elif w1['pos_tag'] == 'PRP' and w2['pos_tag'] == 'NNP':
        return True
    elif w1['pos_tag'] == 'NNP' and w2['pos_tag'] == 'PRP':
        return True
    else:
        return False
