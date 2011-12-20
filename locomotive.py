import track,math,plot

class locomotive:
    """Navigating locomotive that will follow tracks"""
    def __init__(self,plot):
        self.pos = plot

    def navigate(self,plot,incr):
        """Calculate X, Y, and Z movements"""
        
        # 3D Usage of Pythagorean Theorem:
        # length^2 = x^2 + y^2 + z^2
        #
        # sf = d/length (sf: scale factor; d: desired length)
        #
        # Movement:
        # x += 1*sf
        # y += y*sf
        # z += z*sf

        # convert variables to type float
        x1,y1,z1 = map(float,self.pos)
        x2,y2,z2 = map(float,plot)
        incr = float(incr)
        
        x = 1
        y = (y2-y1)/(x2-x1)
        z = (z2-z1)/(x2-x1)
        length = math.sqrt((x**2)+(y**2)+(z**2))
        sf = incr/length

        x3,y3,z3 = sf,(y*sf),(z*sf)
        return x3,y3,z3

    def move(self,dest):
        """Move to coordinates dest"""
        pos = []
        pos.extend(self.pos) # localize
        pos[0]+=dest[0]
        pos[1]+=dest[1]
        pos[2]+=dest[2]
        self.pos = pos[0],pos[1],pos[2]
        
if __name__ == "__main__":
    humpty = locomotive((3,1,2))
    lenny = humpty.navigate((6,5,3),1)
    print lenny
    print math.sqrt((lenny[0]**2)+(lenny[1]**2)+(lenny[2]**2))
    humpty.move(lenny)
    print humpty.pos
