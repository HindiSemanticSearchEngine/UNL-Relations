def and(w1, w2):

    if w1['pos_tag'] == 'noun' and w2['pos_tag'] == 'noun':
        return True
    elif w1['pos_tag'] == 'num' and w2['pos_tag'] == 'num':
        return True
    elif w1['pos_tag'] == 'RB' and w2['pos_tag'] == 'RB':
        return True
    elif w1['pos_tag'] == 'JJ' and w2['pos_tag'] == 'JJ':
        return True
    elif w1['pos_tag'] == 'IN' and w2['pos_tag'] == 'IN':
        return True
    else:
        return False
