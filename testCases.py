import sys
sys.path.insert(1, 'model')
import Basket
import pytest

from Basket.Ticket import Ticket


from Movie import NewReleaseMovie, ChildrensMovie, StandardMovie
# from model.movie.NewReleaseMovie import NewReleaseMovie
# from model.movie.StandardMovie import StandardMovie
# from model.movie.ChildrensMovie import ChildrensMovie


# import movie.NewReleaseMovie, ChildrensMovie, StandardMovie

class TestCases():
    def test1(self):
        self.assertEqual(1, 1)

    def test2(self):
        self.assertEqual(1, 2)

    def addToMovieTest(self):
        ##Movies##
        # movie1 = NewReleaseMovie("Where the Crawdads Sing", 123)
        # movie2 = ChildrensMovie("Cars 2", 131)
        movie3 = StandardMovie("Shawshank Redemption", 141)

        ##Tickets##
        # ticket1 = Ticket(movie1, "kids")
        # ticket2 = Ticket(movie2, "student")
        ticket3 = Ticket(movie3, "adult")

        ##Concessions##
        popcorn1 = RegularPopcorn()
        popcorn2 = LargePopcorn()
        popcorn1 = AddIceCream(AddDrink(popcorn1))
        popcorn2 = AddHotDog(AddSweets(popcorn2))

        ##Basket##
        myBasket = Basket(BasketEmpty())

        ##Add Items##
        myBasket.addItem(ticket1, 1)
        myBasket.addItem(ticket2, 2)
        myBasket.addItem(ticket3, 1)
        myBasket.addItem(popcorn1, 2)
        myBasket.addItem(popcorn2)

        ##View Baseket##
        myBasket.viewBasket()
        myBasket.recordPurchase(69124)



if __name__ == '__main__':
    pytest.main()