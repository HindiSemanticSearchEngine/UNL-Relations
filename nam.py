def qua(w1,w2):
	if w1['pos_tag']=='NN' and w2['pos_tag']=='NNS':
		return True

	elif w1['pos_tag']=='NNS' and w2['pos_tag']=='NN':
		return True

	elif w1['pos_tag']=='NN' and w2['pos_tag']=='NNP':
		return True

	elif w1['pos_tag']=='NNP' and w2['pos_tag']=='NN':
		return True

	elif w1['pos_tag']=='NN' and w2['pos_tag']=='NNPS':
		return True

	elif w1['pos_tag']=='NNPS' and w2['pos_tag']=='NN':
		return True

	elif w1['pos_tag']=='NNS' and w2['pos_tag']=='NNP':
		return True

	elif w1['pos_tag']=='NNP' and w2['pos_tag']=='NNS':
		return True

	elif w1['pos_tag']=='NNS' and w2['pos_tag']=='NNPS':
		return True

	elif w1['pos_tag']=='NNPS' and w2['pos_tag']=='NNS':
		return True

	elif w1['pos_tag']=='NNP' and w2['pos_tag']=='NNPS':
		return True

	elif w1['pos_tag']=='NNPS' and w2['pos_tag']=='NNP':
		return True

	else:
		return False