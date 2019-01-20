"""
How to use it is visible https://github.com/qianduanXIAOHAOZI/WebGraph/blob/master/README.md
"""

class webpage:
    def __init__(self, url, weight = 0.001, links = []):
        self.__url = url # you can't change it, but you can get it
        self.weight = weight # you can change and get it, because the value of this needs to be recalculated frequently
        self.links = links # you can change and get it, because the value of this also needs to add elements and get their values often.

    def url(self): # This is the way to get url
        return self.__url


# To calculat the weight according to links
def weight(links): # links is of a webpage object
    # The initial state is 0
    # Then add the weight of all the pages that point to it
    w = 0
    for i in links:
        w += i.weight
    return w
