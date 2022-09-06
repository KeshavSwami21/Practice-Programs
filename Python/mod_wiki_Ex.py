#==============Imports Starts======================

import wikipedia

#==============Imports Starts======================


#===========Wikipedia Search Engine Starts=====================

class Wiki:

    #Decalring global variable to use them throughout the class
    global txt, txt1, subject2, subject1

    #Text for replying via mails.
    txt = "Thanks for using my program, hopping to see your again."
    txt1 = "Soory for inconvenience."

#Getting the search results by initialing wikipedia Starts

    def __init__(self, word):
        self.word = word
        
        global X
        #Stroing the results in list form to variable X
        X = wikipedia.search(self.word, results=5)

#Getting the search results by initialing wikipedia Ends

#Showing the search results in output

    def show(self):

        #If the search result cann't be found then the if condition will be executed
        if(len(X) == 0):

            print("Oops! I can't Find anything regarding that.")

        #If the list contain only 1 result the the elif condition will be executed
        elif(len(X) == 1):

            print(wikipedia.summary(X, sentences=5), "\n") #This will print the search result output

            
        #If the list contain more than 1 result the the else condition will be executed
        else:

            a = len(X) #Stroing the length of the list to variable a

            print("I found to many results.\n")

            #Loop to print the list items in different lines
            for i in range(0, a):
                print(f"{i+1}. {X[i]}.")

            #Asking user to select sub-search-item option
            sel = int(input("\nPlease an option to search: "))
            print()
            
            
            #If program dosen't generate any error then the try statement will be executed
            try:
                #Printing the result and Passing the result to 'Speak' method.
                print(wikipedia.summary(X[sel-1], sentences=5), "\n")
            #If program generate any error then the except statement will be executed       
            except:
                print("\nOops! I can't Find anything regarding that.")

#===========Wikipedia Search Engine Ends=====================

#===========Main Program Starts=========================
#Asking user to enter a word for searching 
word = input("Enter a word to search: ")

#Passing 'Word' variable to 'Wiki' class
obj = Wiki(word)
obj.show() #Using the show methon in 'Wiki' Class

#Printing thanks
print("\nThanks for using me:), Hoppping to see you again.")

#===========Main Program Ends=========================