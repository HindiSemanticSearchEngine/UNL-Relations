def duration(w1,w2):
    if w1['pos_tag']=='RB' and w2['pos_tag']=='INTF':
        return True
    elif w1['pos_tag']=='VAUX' and w2['pos_tag']=='QNUM':
        return True
    elif w1['pos_tag']=='RB' and w2['pos_tag']=='QNUM':
        return True
    elif w1['pos_tag']=='NNPC' and w2['pos_tag']=='INTF':
        return True  
    elif w1['pos_tag']=='NN' and w2['pos_tag'] == 'QF':
	return True
    elif w1['pos_tag']=='NNP' and w2['pos_tag'] == 'QF':
    else:
        return False
    
