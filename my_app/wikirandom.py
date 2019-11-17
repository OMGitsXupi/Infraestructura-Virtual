import random

class RandomImage:

	def __init__(self):
		self.links = ['https://pbs.twimg.com/media/EIxOE3pWwAEGvCl?format=jpg&name=360x360','https://pbs.twimg.com/media/EIkQnbdXkAAhMl9?format=jpg&name=900x900','https://pbs.twimg.com/media/EH6OUtEXkAAFEcK?format=jpg&name=small']

	def getLinks(self):
		return self.links

	def getRandomImage(self):
		i=random.randint(0, self.getSize()-1)
		return self.links[i]

	def pushImage(self,link):
		self.links.append(link)
		return 0

	def getImage(self,i):
		return self.links[i]

	def getSize(self):
		return len(self.links)
