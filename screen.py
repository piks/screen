def screen(mode="html",full="",start="",stop="",instance=0):
	if mode=="html":
		start,stop="<",">"
		while start in full:
			a=full.find(start)
			b=full.find(stop)
			full=full.replace(full[a:b+1],"")
		return full
	elif mode=="strip":
		print(instance)
		if instance=="all":
			while start in full:
				a=full.find(start)
				b=full.find(stop)
				full=full.replace(full[a:b+1],"")	
				print(full)
