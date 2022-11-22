from Movie.NewReleaseMovie import NewReleaseMovie
from Movie.StandardMovie import StandardMovie
from Movie.ChildrensMovie import ChildrensMovie
from Concessions.Popcorn import *
from Concessions.AddOns import *
from Ticket import *
from Basket import *

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
