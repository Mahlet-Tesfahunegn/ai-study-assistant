def main():

    print("LearnCompass\n")

    print("Welcome to LearnCompass! \nYour AI-powered study companion.\n\n")

    # Asking the user to choose menu
    menu = "\n1.Add Note \n2.Summarize Text \n3.Generate Quiz \n4.Exit"

    # The invalid text input will be handled in future improvements
    userPreference = int(input(f"Choose your preference from this menu please\n\nLearnCompass menu \n {menu} \n\n Your preference:"))


    if userPreference == 1:
        addNote()
    elif userPreference == 2:
        summarize()
    elif userPreference == 3:
        generateQuiz()
    elif userPreference == 4:
        exitProgram()
    else :
        print(f"Please choose your preference again.")
        userPreference = int(input(f"Choose your preference from this menu please\n\nLearnCompass menu \n {menu} \n\n Your preference:"))



# Function for adding notes
def addNote():
    userNote = input("Please enter your note:")

    userNote = userNote.strip()

    # The code which will save the notes to the database will be added here in the future

    print("Your note has been saved.")



# Function for summarizing notes
def summarize():
    
    textToSummarise = input("Please add your input for summarization: ")

    # The code which will summarise the notes will be added here in the future
    summarisedNote = "Summarized Note"
    
    print(f"Here is your summarised note.\n{summarisedNote}")



# Function for generating quizes
def generateQuiz():

    quizNote = input("Please add your note to generate quiz: ")

    quizNote = quizNote.strip()

    # The code which will generate quizes will be added here in the future

    quiz = "Quiz"

    print(f"Here is your quiz try to focus and answer each questions. Good luck!!\n{quiz}")



# Exiting function
def exitProgram():
     print("Thanks for using LearnCompass.\nKeep learning!")





main()


