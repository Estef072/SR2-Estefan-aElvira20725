def glFill(self, polygon):
    for y in range(self.height):
        for x in range(self.width): 
            i = 0
            j = len(polygon) - 1
            result = False

            for i in range(len(polygon)):
                if (polygon[i][1] < y and polygon[j][1] >= y) or (polygon[j][1] < y and polygon[i][1] >= y):
                    if polygon[i][0] + (y - polygon[i][1]) / (polygon[j][1] - polygon[i][1]) * (polygon[j][0] - polygon[i][0]) < x:
                        result = not result
                        j = i

                        if result == True:
                            self.glPoint((float(x)/(float(self.width)/2))-1,(float(y)/(float(self.height)/2))-1,self.vertexColor)
                    else:
                        pass