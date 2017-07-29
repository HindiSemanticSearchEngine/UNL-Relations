def obj(w1,w2):
	if w1['pos_tag']=='NN' and w2['pos_tag']=='VM:
		return True

	elif w1['pos_tag']=='VM' and w2['pos_tag']=='NN':
		return True

	elif w1['pos_tag']=='NNP' and w2['pos_tag']=='VM':
                return True

        elif w1['pos_tag']=='VM' and w2['pos_tag']=='NNP':
                return True

        elif w1['pos_tag']=='VAUX' and w2['pos_tag']=='NNP':
                return True

        elif w1['pos_tag']=='NNP' and w2['pos_tag']=='VAUX':
		return True
            
	else:
		return False
