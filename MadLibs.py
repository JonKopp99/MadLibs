import random #So we can use random int!
import os #to clear terminal!

CVI = '\33[105m' #ANSI Violet!
CRED    = '\33[31m' #ANSI RED!
ENDC = '\033[0m' #ANSI End Color Code!


'''
    user_input Used to get the input to see if user wants to continue or exit the program!
    @param prompt = what we are asking to the user!
    @return return the user input!!! ;)
'''
def user_input(prompt):
    thein = str(raw_input(prompt))
    return thein


'''
    repalceThemBrackets = First gets user input asking them a word based on whats inside the bracket start and end
                          point. Then puts their response in a dictionary!
    @param c = What to ask user for(Adj,Noun,Verb,etc...)
    @param dictionary = suer input pair insdie the dictself.
    @postcondition add the cue to the dict and set it euqal to what user picks

'''
def replaceThemBrackets(c, dictionary):
    p = "Enter a word that is a "+CRED+"{name}"+ENDC+": "
    theprompt = p.format(name=c)
    resp= raw_input(theprompt) # use raw input so user doesnt have to put input in ""!
    dictionary[c] = resp


'''
getTheBrackets = Searches through the madlib and Returns a list of bracket locations.
@Param bracketFinder = The MadLib with {} used as place holders for words
@Return returns set(blist) set removes duplicates and blist contains the points of start
 and end of the brackets.
'''
def getTheBrackets(bracketFinder):
    bList = list()
    end = 0
    dupes = bracketFinder.count('{')
    for k in range(dupes):
        start = bracketFinder.find('{', end) + 1
        end = bracketFinder.find('}', start)
        theBrack = bracketFinder[start : end]
        bList.append(theBrack)

    return set(bList)


'''
    getUserInp = Loops through the cue and then gets the input from user and Returns
                   the dictionary containing them
    @param bLoc = Where the brackets are stored! Need to be replaced with userinputs!
    @return return dictionary contating the user choices where the brackets were before!

'''
def getUserInp(bLoc):
    userInps = dict()
    for c in bLoc:
        replaceThemBrackets(c, userInps)
    return userInps


'''
    printTheStory = Puts the full story together getting user input and replacing {}
                with the inputs.
    @param theStory = the story that needs to be formatted with userInputs!
    @postcondition get bracket locations of story, get user input for the grammar that needs to be replaced
                   then print out the new formatted story!
'''
def printTheStory(thestory):
    unused_variable = os.system("clear")
    c = getTheBrackets(thestory)
    userInp = getUserInp(c)
    story = thestory.format(**userInp)
    print(story)


'''
    main = Picks a random story everytime to tell user,
    @postcondition = Does its magic to put the whole madlibs together!
'''
def main():
    rannum = random.randint(0,3)
    if(rannum==1):
        Story= '''
        Once upon a time at MakeSchool, ''' + CVI + '''{instructor}'''+ ENDC + ''' told me that I needed to
        ''' + CVI + '''{activity}'''+ ENDC + '''. At first this was ''' + CVI + '''{verb}'''+ ENDC + ''' to do. But soon I feel in love with
        ''' + CVI + '''{activity}'''+ ENDC + '''.

        The End
        '''

    elif(rannum==2):
        Story = '''
        My name is ''' + CVI + '''{your name}'''+ ENDC + '''. My best friends name is ''' + CVI + '''{friend}'''+ ENDC + '''. Today we ate ''' + CVI + '''{food}'''+ ENDC + '''.
        ''' + CVI + '''{friend}'''+ ENDC + ''' got super duper sick from eating ''' + CVI + '''{food}'''+ ENDC + '''. He told me "''' + CVI + '''{your name}'''+ ENDC + ''', Why did you
        make me eat this trash?". This is the day ''' + CVI + '''{friend}'''+ ENDC + ''' and I stopped being homies.


        The End
        '''
    else:
        Story = '''
        Today I went to the pound and adopted a ''' + CVI + '''{animal}'''+ ENDC +'''. I named it ''' + CVI + '''{name}'''+ ENDC +'''.
        ''' + CVI + '''{name}'''+ ENDC +''' and I did everything together, I had never been so in ''' + CVI + '''{feeling}'''+ ENDC +'''
        before. But one day ''' + CVI + '''{name}'''+ ENDC +''' got hit by a ''' + CVI + '''{object}'''+ ENDC +'''. I was so in ''' + CVI + '''{feeling}'''+ ENDC +'''.

        The End
        '''

    printTheStory(Story)
    tempin=user_input("Would you like to go again!?!? "+CRED+"Y/N"+ENDC+": ")
    while(tempin.lower() != 'n' and tempin.lower() != 'y'):
        print(tempin)
        tempin=user_input("Sorry I missheard you. Would you like to go again!?!? "+CRED+"Y/N"+ENDC+": ")
    if(tempin.lower()=='y'):
        main()
    else:
        print("EXITING...")
        unused_variable = os.system("clear")
        exit()
        

main()

'''
def test():
    testInp = user_input("Test: ")
    print(testInp)

    print(getTheBrackets("TEST {TEST} TEST {TEST}"))
test()
'''
