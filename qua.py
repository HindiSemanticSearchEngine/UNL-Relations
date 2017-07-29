def qua(w1,w2):
	if w1['pos_tag']=='NN' and w2['pos_tag']=='QF':
		return True

	elif w1['pos_tag']=='QF' and w2['pos_tag']=='NN':
		return True

	else:
		return False
