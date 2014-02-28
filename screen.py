def screen(mode="html",full="",start="",stop="",instance=1):
	if mode=="html":
		start,stop="<",">"
		while start in full:
			a=full.find(start)
			b=full.find(stop)
			full=full.replace(full[a:b+1],"")
		return full
