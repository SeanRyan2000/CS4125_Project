from model.Basket.Concessions import Popcorn


class ConcessionFactory:

    def createPopcorn(self, request):

        if request == 'large':
            return Popcorn.LargePopcorn()
        if request == 'regular':
            return Popcorn.RegularPopcorn()