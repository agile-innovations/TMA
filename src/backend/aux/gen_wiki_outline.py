
titles =  ["Cablegate", "Muse", "NIH Map", "TMVE", "Topical Guide", "Twahpic"]
page = "related-projects" 
title_esc = []

for ttl in titles:    
    te = '-'.join(ttl.lower().split())
    title_esc.append(te)
    print """* <a href="%s#wiki-%s">%s</a>""" % (page, te, ttl)
           
print ""
print ""

for i, ttl in  enumerate(titles):
    print """<a name="%s" href="%s#wiki-%s">#</a> %s\n---""" % (title_esc[i], page, title_esc[i], ttl)
    print "" 
                    
                            

