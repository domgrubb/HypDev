#=====importing libraries===========
'''This is the section where you will import libraries'''
import os
import sys
import datetime
os.chdir(sys.path[0])

## Defining functions to be used ##
def reg_user():
    '''Prompts user for new username and password to register.
    Asks to confirm password given, if confirmation is incorrect loops until they match.'''

    new_user = input("Please input the new username to enter: ")
    ## Checking username is not already in database ##
    while new_user in usernames:
        new_user = input("This user already exists, please enter a new username: ")

    new_pass = input("Please enter the associated password: ")
    check_pass = input("Please confirm new password: ")
    while new_pass != check_pass:
        new_pass = input("Passwords did not match. Please enter the associated password: ")
        check_pass = input("Please confirm new password: ")
    with open("user.txt", "a") as f:
        f.write(f"\n{new_user}, {new_pass}")

def add_task():
    t_user = input("Please input the username to whom the task will be assigned: ")
    t_title = input("Please input the title of the task: ")
    t_desc = input("Please input the description of the task: ")
    t_due = input("Please input the date the task is due: ")
    curr_date = datetime.date.today().strftime("%d %b %Y")

    ## Adding information in correct format to tasks.txt file ##
    with open("tasks.txt", "a") as f:
        f.write(f'\n{t_user}, {t_title}, {t_desc}, {t_due}, {curr_date}, No')

def view_all():
    with open("tasks.txt", "r") as f:
        for line in f:
            sections = line.split(',')
            print('{:>6}, {:>6}, {:>6}, {:>6}, {:>6}, {:>6}'.format(*sections))
            ## Adding extra space for better formatting ## 
            print()

def view_mine():
    with open("tasks.txt", "r") as f:
        ## Initialising dictionary for ease of selecting a task ##
        task_dict = {}
        for count, line in enumerate(f):
            sections = line.split(',')
            if sections[0] == username:
                task_dict[str(count + 1)] = sections
        
        ## With dictionary formed, can call upon task by number easily ##
        task_req = input("Please enter the number for the task you wish to view. Enter \"-1\" to exit: ")
        if task_req in list(task_dict.keys()):
            print()
            print(f'''Task {task_req}: 
For user: {task_dict[task_req][0]} 
Title of task: {task_dict[task_req][1]} 
Description: {task_dict[task_req][2]} 
Current Date: {task_dict[task_req][3]} 
Due: {task_dict[task_req][4]} 
Completed? {task_dict[task_req][5]}''')
            ## Adding extra space for better formatting ## 
            print()

def gen_reports():
    '''Generates two reports, task_overview.txt and user_overview.txt.
    Task overview contains number of tasks generated and tracked, number of completed
    and uncompleted tasks, number of tasks that are overdue and percentage of incomplete/complete tasks.
    User overview contains number of users generated, percentage of tasks assigned to each user,
    percentage of tasks that are complete/incomplete and percentage that are overdue.'''
    ## Generating task_overview first, iterating over lines in file to obtain information ##
    today = datetime.datetime.today()
    n_complete = 0 
    n_incomplete = 0
    overdue = 0
    on_time = 0

        ## Opening file again to account for any newly added users ##
    f = open("user.txt", "r")
    user = f.read()
    f.close()

    ## Splitting the file means all odd indexed words will be users, all even will be passwords ##
    ## First removing whitespace, then splitting at comma ##
    user = user.replace(' ', '')
    user = user.replace('\n', ',')
    user = user.split(',')
    usernames = []
    for count, word in enumerate(user):
        if (count + 1) % 2 != 0:
            usernames.append(word)

    ## Initialising a dictionary to increment through tasks file to count tasks for each user ##
    users_tasks = dict.fromkeys(usernames, 0)
    users_incomplete = dict.fromkeys(usernames, 0)
    users_overdue = dict.fromkeys(usernames, 0)
    with open("tasks.txt", "r") as f:
        for count, line in enumerate(f):
            sections = line.split(',')
            
            ## Identifying completed tasks ##
            task_comp = sections[-1]
            if task_comp == "No":
                n_complete += 1
            else:
                users_incomplete[sections[0]] += 1
                n_incomplete += 1


            ## Identifying overdue tasks ##
            ## Can use mathematical operators with datetime objects, using this to assess if past due ##
            due_date = datetime.datetime.strptime(sections[-2]," %d %b %Y")
            if due_date > today and task_comp == "No":
                overdue += 1
                users_overdue[sections[0]] += 1
            else:
                on_time += 1
            
            ## Incrementing value in dict for username as tasks are found ## 
            users_tasks[sections[0]] += 1

    ## Writing obtained data to file ##
    with open("task_overview.txt", "w") as f:
        f.write(f'''Total tasks: {count + 1}
Total tasks added this session: {tasks_added}
Total completed tasks: {n_complete}
Total uncompleted tasks: {n_incomplete}
Total overdue: {overdue}
Percentage incomplete: {(n_incomplete / (n_incomplete + n_complete)) * 100}
Percentage overdue: {(overdue / (overdue + on_time)) * 100}''')

    ## Generating user overview ## 
    with open("user_overview.txt", "a") as f:
        f.write(f'''Total users registered this session: {users_added}
Total tasks added this session: {tasks_added}\n''')
        for user, tasks in users_tasks.items():
            f.write(f'''User {user} has {tasks} tasks assigned
User {user} has {(tasks / (count + 1)) * 100}% of total tasks
User {user} has {(users_incomplete[user] / tasks) * 100}% of their tasks currently incomplete
User {user} has completed {((tasks - users_incomplete[user]) / tasks) * 100}% of their tasks
User {user} has {(users_overdue[user] / tasks) * 100}% of their tasks overdue''')

def stats():
    gen_reports()
    print("Task statistics: ")
    with open("task_overview.txt", "r") as f:
        for line in f:
            print(line)
    print()
    print("Users statistics: ")
    with open("user_overview.txt", "r") as f:
        for line in f:
            print(line)
    print()
    
## Initialising counters to track how many users/tasks are created this session ##
tasks_added = 0
users_added = 0


## User and password separated by comma ##
f = open("user.txt", "r")
user = f.read()
f.close()

## Splitting the file means all odd indexed words will be users, all even will be passwords ##
## First removing whitespace, then splitting at comma ##
user = user.replace(' ', '')
user = user.replace('\n', ',')
user = user.split(',')
passwords = []
usernames = []
for count, word in enumerate(user):
    if (count + 1) % 2 == 0:
        passwords.append(word)
    else:
        usernames.append(word)

## Prompting user to log in, checking details ##
username = input("Please enter your username: ")
while username not in usernames:
    username = input("Invalid username entered, please try again: ")

password = input("Please enter your password: ")
while password not in passwords:
    password = input("Invalid password entered, please try again: ")

while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - Generate reports
s - View stats
e - Exit
: ''').lower()

    if menu == 'r' and username == 'admin':
        ## Calls previously defined function to prompt for new user and password and writes to file##
        reg_user()
        users_added +=1

    elif menu == 'a':
        add_task()
        tasks_added +=1

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()

    elif menu == 'gr':
        gen_reports()

    elif menu == 's' and username == 'admin':
        stats()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")