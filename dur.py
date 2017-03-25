def duration(w1,w2):
    if w1['pos_tag']=='VBD' and w2['pos_tag']=='CD':
        return True
    elif w1['pos_tag']=='VBD' and w2['pos_tag']=='JJ':
        return True
    elif w1['pos_tag']=='VBD' and w2['pos_tag']=='CD':
        return True
    elif w1['pos_tag']=='VBG' and w2['pos_tag']=='VBG':
        return True  
    elif w1['pos_tag']=='VBD' and w2['pos_tag'] = 'NNS':
	return True	
    else:
        return False
    
