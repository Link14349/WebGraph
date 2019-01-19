class webpage:
    def __init__(self, url, weight = 0.001, links = []):
        self.__url = url
        self.weight = weight
        self.links = links

    def url(self):
        return self.__url


def weight(links):
    w = 0
    for i in links:
        w += i.weight
    return w
