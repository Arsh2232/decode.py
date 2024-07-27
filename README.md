# decode.py
this program allows you to enter the numbers in another text file and decode or create an encrypted message
#for better reading, view README in 
the program starts by defining a fucntion def decode that takes in two attributes, numbers and message file which is the attached letters.txt file. 
This fucntion has an empty dictionary that holds the numbers 
then with open, we open the letters file and itertae through each line and seperate it into number and word by using strip and split
then convert the num into int and add it to the dictionary 
Then we intialize another empty dictionary to store the values of the numbers 
then a conditional checks that if the number entered is in the first  num dictiionary, only then the value gets added to the new dictionary we just created 
then .join is used to join the words decoded words added to the dictionary based on what numbers the user enters and decoded message is returned
The end of the program asks the user for input and used strip and split method to remomve leading ro trailing white spaces and split is used to split it at the white spaces between the numbers.
Now, the split method alredy return a list but since this list contains strings as items, we need to create another list that iterated through this list and converts the items to int.
then a final  print statement displays the message.
