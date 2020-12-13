import sys
To_Do_List = []
def daily_task():
    name = input('Enter Your Name: ')
    print("Hello,",name,"I'm Your Personal Assistant, What Plans Do You Have For Today?\nPress Enter To Finish.")
    while True:
        task = input('Task: ')
        if task == '':
            print("Here are your tasks for today,",name)
            for goal in To_Do_List:
                print('---',goal)
            print("Are there any tasks that you completed yet?\nPress 'Enter' To End Program.")
            while True:
                completed_task = input('Completed Task: ')
                if completed_task == '':
                    if len(To_Do_List) == 0:
                        print('Your list of tasks is complete, have a good day',name)
                        sys.exit()
                    else:
                        print('Here is your list of uncompleted task(s). Good luck',name)
                        for goal in To_Do_List:
                            print('---',goal)
                        sys.exit()                    
                elif completed_task not in To_Do_List:
                    print('Task is not found inside of daily log')
                    continue
                else:
                    To_Do_List.remove(completed_task)
                    for goal in To_Do_List:
                        print('---',goal)
                    print('Task Has Been Completed.')
                    continue
        else:
            print('I will add your task to your to do list.')
            To_Do_List.append(task)
            continue
daily_task()
