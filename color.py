class Jacket:
	def getColor(self):
		colors = {
		'#ffffff' : 'white',
		'#000000': 'black'
		}
		return colors[self.__color]

	def setcolor(self, val):
		self.__color = val

obj = Jacket()
obj.setcolor('#ffffff')
print(obj.getColor())
