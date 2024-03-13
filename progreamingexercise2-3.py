# Variable to hold the size of the tract and number of scres .
tractSize = 0.0
acres = 0.0

#constant for the number of square feet in an acre .
SQ_FEET_PER_ACRE = 4360

#Get the square feet in the tract .
tractSize = float (input("Enter the number of square feet in tract."))

# calculate the acreage.
arces = tractSize/ SQ_FEET_PER_ACRE  

#print the number of acres.print.
("The size of that tract is" , format(acres, '.2f'), "acres.")
