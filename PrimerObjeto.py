class Hotel:
    def __init__(self, max_huespedes, estacionamiento):
        self.max=max_huespedes
        self.estacionamiento=estacionamiento
        self.huespedes=0
    def huesped_nuevo(self,cant_huespedes):
        self.max-=cant_huespedes
        self.huespedes+=cant_huespedes
    def checkout(self,cant_huespedes):
        self.max+=cant_huespedes
        self.huespedes-=cant_huespedes  
    def ocupacion(self):
        print(self.max,self.huespedes)          
hotel= Hotel(50,20)
