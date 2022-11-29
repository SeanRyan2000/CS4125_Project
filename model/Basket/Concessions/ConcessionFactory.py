from model.Basket.Concessions import Popcorn


class ConcessionFactory:

    def createPopcorn(self, request):
        regPop = None
        largePop = None
        if request == 'large':
            regPop = Popcorn.RegularPopcorn(request.re)
        if request == 'regular':
            return Popcorn.RegularPopcorn()