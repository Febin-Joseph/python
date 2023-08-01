#You are working on a project for a bookstore and need to implement a system 
#to calculate the total price of a customer's order. The bookstore offers a
#discount based on the total quantity of books purchased. The discount tiers 
#are as follows:
#If the total quantity is less than 10, no discount is applied.
#If the total quantity is between 10 and 20 (inclusive), a 10% discount is applied.
#If the total quantity is greater than 20, a 20% discount is applied

try:
   num_of_books = int(input(" enter the number of books you have purchased "))
   
   one_book_price = 10
   discount = 0
   
   if num_of_books <= 10 and num_of_books >= 0:
       print ("You are not eligible for a a discount. total price = ",one_book_price * num_of_books)
   elif num_of_books > 10 and num_of_books < 20:
       books_price = num_of_books * one_book_price
       discount += 10
       total_claculation = books_price - (books_price / discount)
   
       print(f"Price: {books_price}, Discount: {discount}%, Total RS. : {total_claculation}")
   elif num_of_books >= 20 :
       books_price = num_of_books * one_book_price
       discount += 20
       total_claculation = books_price - (num_of_books * one_book_price / discount)
   
       print(f"Price: {books_price}, Discount: {discount} %, Total RS. : {total_claculation}")
   elif num_of_books < 0:
       print("please by a book")
   
except ValueError:
   print("please enter a valid number")