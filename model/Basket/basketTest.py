import os
import sys

from CS4125_Project.model.Basket.Basket import Basket, BasketEmpty

currDir = os.path.dirname(os.path.realpath(__file__))
rootDir = os.path.abspath(os.path.join(currDir, '..'))
if rootDir not in sys.path: # add parent dir to paths
    sys.path.append(rootDir)

from CS4125_Project.model.Movie.NewReleaseMovie import NewReleaseMovie
from CS4125_Project.model.Movie.StandardMovie import StandardMovie
from CS4125_Project.model.Movie.ChildrensMovie import ChildrensMovie
from CS4125_Project.model.Basket.Concessions.Popcorn import *
from CS4125_Project.model.Basket.Concessions.AddOns import *
# from CS4125_Project.model.Basket.Ticket import Ticket as tick
import CS4125_Project.model.Basket.Ticket as tick
import CS4125_Project.model.Basket.Basket as bask
from CS4125_Project.model.Basket import *

##Movies##
movie1 = NewReleaseMovie("Where the Crawdads Sing", 123, 20)
movie2 = ChildrensMovie("Cars 2", 131, 20)
movie3 = StandardMovie("Shawshank Redemption", 141, 20)

##Tickets##
ticket1 = tick.Ticket('movieName1', "kids", 'new', 120, 1, 'Adult')
ticket2 = tick.Ticket('movieName2', "student", 'new', 120, 1, 'Adult')
ticket3 = tick.Ticket('movieName3', "adult", 'new', 120, 1, 'Adult')

##Concessions##
popcorn1 = RegularPopcorn()
popcorn2 = LargePopcorn()
popcorn1 = AddIceCream(AddDrink(popcorn1))
popcorn2 = AddHotDog(AddSweets(popcorn2))

##Basket##
myBasket = bask.Basket(BasketEmpty())

##Add Items##
myBasket.addItem(ticket1, 1)
myBasket.addItem(ticket2, 2)
myBasket.addItem(ticket3, 1)
myBasket.addItem(popcorn1, 2)
myBasket.addItem(popcorn2)

##View Baseket##
myBasket.viewBasket()
myBasket.recordPurchase(69124)
