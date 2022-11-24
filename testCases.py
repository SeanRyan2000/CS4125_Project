import model.Basket
import pyTest
from model.Movie.NewReleaseMovie import NewReleaseMovie
from model.Movie.StandardMovie import StandardMovie
from model.Movie.ChildrensMovie import ChildrensMovie
from model.Basket.Concessions.Popcorn import *
from model.Basket.Concessions.AddOns import *
from model.Basket.Ticket import *
from model.Basket.Basket import *

class TestCases(pyTest.TestCase):
    def test1(self):
        self.assertEqual(1, 1)

    def test2(self):
        self.assertEqual(1, 2)

    def addToMovieTest(self):
        ##Movies##
        movie1 = NewReleaseMovie("Where the Crawdads Sing", 123, 20)
        movie2 = ChildrensMovie("Cars 2", 131, 20)
        movie3 = StandardMovie("Shawshank Redemption", 141, 20)

        ##Tickets##
        ticket1 = Ticket(movie1, "kids")
        ticket2 = Ticket(movie2, "student")
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
    pyTest.main()
