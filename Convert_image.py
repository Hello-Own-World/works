import random
class Image :
    def __init__(self,size):
        self.size = size
        self.colors = ["red", "blue" , "green" , "yellow" , "pink"]
        self.image = [[random.choice(self.colors)[0] for j in range(self.size)] for i in range(self.size) ]

    def zip_image (self):
        self.zipped = {}
        for line in range (self.size):
            for el in range (self.size):
                if self.image[line][el] not in self.zipped:
                    self.zipped[self.image[line][el]] = [(line,el)]
                else:
                    self.zipped[self.image[line][el]].append((line,el))
        self.image = self.zipped

    def unzip_image (self):
        self.unzipped = [[None for j in range(self.size)]for i in range(self.size)]
        for color in self.image :
            for coords in range(len(self.image[color])):
                self.unzipped[self.image[color][coords][0]][self.image[color][coords][1]] = color
        self.image= self.unzipped

photo = Image(10)
for i in range (photo.size):
    print(photo.image[i])
photo.zip_image()
print(photo.image)
photo.unzip_image()
for i in range (photo.size):
    print(photo.image[i])

