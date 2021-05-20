# I used Thonny to run this code, it won't work on Jupyter.
# Once you download Thonny, go to Tools > Manage Packages... and look for thulac on the search bar
# Click on thulac and then click on the Install button

import thulac

thu1 = thulac.thulac(seg_only=True)
thu2 = thulac.thulac()
text1 = thu1.cut("我爱北京天安门", text=True)
text2 = thu2.cut("我爱北京天安门", text=True)
print("Tokenization without part-of-speech labeling: ", text1)
print("Tokenization with part-of-speech labeling: ", text2)
