class HW_250619():


    def namer(self, name):
        self.name = name
        return name


    def avg_sum(self,*args):
        return sum(args)/len(args)


a = HW_250619()

print a.namer('Garick')
print a.avg_sum(2,1,1,1,20)
