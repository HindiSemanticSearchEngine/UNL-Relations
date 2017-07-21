def qua(w1,w2):
	if w1['pos_tag']=='NN' and w2['pos_tag']=='QNUM':
		return True

	elif w1['pos_tag']=='QNUM' and w2['pos_tag']=='NN':
		return True

	else:
		return False
