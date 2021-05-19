import thulac

thu1 = thulac.thulac(seg_only=True)
text = thu1.cut("我爱北京天安门", text=True)
print(text)