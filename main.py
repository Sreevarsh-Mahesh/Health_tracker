# app to track food and excercise routines of people
# the routines can be retrived bt user

#fns required

# creating profile
def create(name,activity):
    '''this fn creates a new document for the user to access'''
    file = open(f"{name}-{activity}.txt", 'w')
    file.write(f'{name} {activity} log :\n')
    file.close()

#acess profile
def access(name,activity):
    '''this fn allows user to access a particular profile'''
    file=open(f'{name}-{activity}.txt','r')
    log = file.readlines()
    for i in log:
        if i[-1]=='\n':
            log[log.index(i)]=i[-len(i):-1]
    return log


#time finder
def finddatetime():
    '''finds time and date of updation'''
    import datetime as dt
    date=dt.datetime.now()
    time=date.strftime('%H : %M')
    return f'[{dt.date.today()} - {time}]'



#update profile
def update(name,activity,addition):
    '''this fn adds new info to the document'''
    file = open(f'{name}-{activity}.txt','a')
    file.write(f'\n {finddatetime()} : {addition}')

#Useful info for the user
def help():
    print('Guide : ')
    print('c = create')
    print('a = access')
    print('u = update')
    print('h = help')
    print('t = terminate')

#giving intro to user
help()


#the app has to run till the user terminates
while True:
    start = input("What would you like to do ? (c,a,u,h,t) : ").lower()
    if start=='c':
        name=input('Enter name of profile : ').lower()
        activity = input('Enter the activity to be tracked (diet,exercise,both) : ').lower()
        try:
            if activity=='both':
                create(name,'diet')
                create(name,'exercise')
                print('Profiles Created ! :) ')
                print(f'Profile names : {name}-diet , {name}-exercise')
            else:
                create(name,activity)
                print('Profile created ! :)')
                print(f'Profile names : {name}-{activity}')
        except Exception as E:
            print(E)
            print('Please try again')
    elif start=='a' :
        name = input('Enter name of profile : ').lower()
        activity = input('Enter the activity to be accessed (diet,exercise) : ').lower()
        try:
            log = access(name,activity)
            print('In order of updation : ')
            for i in log:
                print(i)
        except:
            print(f'Error : no such file {name}-{activity}.txt')
            print('Please try again')
    elif start=='u':
        try:
            name = input('Enter name of profile : ').lower()
            activity = input('Enter the activity to be updated (diet,exercise) : ').lower()
            if activity=='diet':
                n_food = int(input('How many dellicacies in your meal : '))
                food=[]
                for i in range(1,n_food+1):
                    item=input(f'Enter delicacy {i} : ')
                    food.append(item)
                update(name,activity,food)
            elif activity=='exercise':
                n_exercises = int(input('How many exercises did you perform : '))
                exercises = []
                for i in range(1,n_exercises+1):
                    item = input(f'Enter exercise {i} : ')
                    exercises.append(item)
                update(name, activity, exercises)
            else:
                print('Invalid input')

        except Exception as E:
            print(E)
            print('Please try again')
    
    elif start=='h':
        help()
    
    elif start=='t':
        print('Thank you for using the program!!')
        break

    else:
        print('invalid input try again')
