def ant_relation(self,sentence):
    l = list(sentence.split())
    if 'नहीं'  not in l:
        return False

    for i in l:
        for j in l:
            if i!=j:
                if i['pos_tag']=='NN' and j['pos_tag']=='NN':
                    return True
                elif i['pos_tag']=='PRP' and j['pos_tag']=='PRP':
                    return True
                elif (i['pos_tag']=='JJ' and j['pos_tag']=='JJ'):
                    return True
                else:
                    return False


