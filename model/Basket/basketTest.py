from Movies.NewReleaseMovie import NewReleaseMovie
from Movies.StandardMovie import StandardMovie
from Movies.ChildrensMovie import ChildrensMovie
from Concessions.Popcorn import RegularPopcorn, LargePopcorn
from Concessions.AddOns import AddDrink, AddSweets, AddIceCream, AddHotDog
from Ticket import Ticket
from Basket import Basket
from Basket import BasketEmpty

movie1 = NewReleaseMovie("Where the Crawdads Sing", 123, 20)
movie2 = ChildrensMovie("Cars 2", 131, 20)
movie3 = StandardMovie("Shawshank Redemption", 141, 20)

ticket1 = Ticket(movie1, "student")
ticket2 = Ticket(movie2, "kids")
ticket3 = Ticket(movie3, "student")

popcorn1 = RegularPopcorn()
popcorn2 = LargePopcorn()
popcorn1 = AddIceCream(AddDrink(popcorn1))
popcorn2 = AddHotDog(AddSweets(popcorn2))

myBasket = Basket(BasketEmpty())

myBasket.addItem(ticket1, 1)
myBasket.addItem(ticket2, 2)
myBasket.addItem(ticket3, 1)
myBasket.addItem(popcorn1, 2)
myBasket.addItem(popcorn2)

myBasket.viewBasket()