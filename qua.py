def qua(w1,w2):
	if w1['pos_tag']=='noun' and w2['pos_tag']=='num':
		return True

	elif w1['pos_tag']=='num' and w2['pos_tag']=='noun':
		return True

	else:
		return False
