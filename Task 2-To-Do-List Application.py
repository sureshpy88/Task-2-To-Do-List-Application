#import os module for directory and file methods
import os

# Creating a blank list to store the processed values

processed_lines=[]

#The algorithm has 2 main branches.
#1. A flow when the os.file.exists() method returns True
#2. A flow when the os.file.exists() method returns False

#As a beggining step determining if the file exists or not in the current directory
filepath="C:/Users/Suresh/Desktop/Python-Workspace/tasklist.txt"

if os.path.exists(filepath):
    user_file_flag=True
    print("The file tasklist.txt exists in the current directory\n")
else:
    user_file_flag=False
    print("The file tasklist.txt doesn't exist in the current directory\n")

    
# Code branch 1:If file exists, as a first step, import the contents to a list. Remove any newline \n character using the strip method

if user_file_flag == True:
   #Opening the file tasklist.txt and reading the numberoflines. Storing the initial values in a variable.
    with open("tasklist.txt","r") as file1:
        init_list_numberoflines = len(file1.readlines())
        print("\nThe initial number of lines in the file are:",init_list_numberoflines)
        
    #If the number of values in the file tasklist.txt are >0 opening the file in read mode.
    #Reading the lines into a list and then processing each line by removing the existing "\n" character for each line.
    if init_list_numberoflines > 0:
            with open("tasklist.txt","r") as file2:
              lines = file2.readlines()
              
            for snum,line in enumerate(lines):
              processed_line=line.strip()
              #Adding the processed line to the processed_lines list
              processed_lines.append(processed_line)
                
    #If the number of lines in the initial file are 0, displaying it to the user.
    else:
            print("\nThere are no tasks to be displayed currently.")
        
                
#Code branch 2:If the file doesn't exist, creating it.

if user_file_flag == False:
  with open("tasklist.txt","x") as file:
      pass
  print("\nThe new file tasklist.txt has been created.")
  print("\nThere are no tasks to be displayed currently.\n")

             
# Welcoming the user to the application and displaying the existing task items in a vertical view, in the application

print("\nWelcome to the To-Do list app!"+"\n")
#print (processed_lines)
if len(processed_lines)!=0:
 print("These are your current To-Do tasks list:"+"\n")
 for i in range(len(processed_lines)):
  print(processed_lines[i])

# Starting a while loop for displaying user selection options, and taking the user input into a list

while True:
#Display the options of selection to the user
 print()
 print("What would you like to do next?"+"\n")
 print("1. Add a task, 2. Remove a task, 3. View the task list, 4. Exit the application\n")
 user_selection_number=int(input("Please enter your selection number from 1,2,3,4:"))

 #Working with the list processed_lines after user input is entered from the console from 1,2,3,4
 #1 for Adding a task to the list
 #2 for Removing a task from the list
 #3 for Viewing a task from the list
 #4 for Exiting the application

# Adding the task to processed_lines list and display vertically the updated list    
 if user_selection_number == 1:
  new_task_entry = input("Please enter the new task:")
  processed_lines.append(new_task_entry)
  print("The new task has been added to your To-Do list.The updated list is:"+"\n")
  for i in range(len(processed_lines)):
   print(processed_lines[i])

#Removing a task from the list after user has entered a value from console that matches the list values               
 if user_selection_number == 2:
 
  print("Which task would you like to remove?"+"\n")
  for i in range(len(processed_lines)):
   print(processed_lines[i]) 
  taskvalue_to_be_removed = input("\nPlease Enter the exact value to be removed from the list:")
  processed_lines.remove(taskvalue_to_be_removed)
  print("\nThe updated task list after removal of the task is:"+"\n")
  for i in range(len(processed_lines)):
   print(processed_lines[i])  

#Viewing the current task list at any point of time during additions or removals

 if user_selection_number == 3:
  print("\nThe current total list of tasks:")
  print()
  for i in range(len(processed_lines)):
   print(processed_lines[i])

#Exiting the application at any point of time
     
 if user_selection_number == 4:
  
  break 

#Finalizing and saving the task list to the tasklist.txt after add/remove modifications from the user
final_task_list=processed_lines

with open("tasklist.txt","w") as file3:
    for item in final_task_list:
        file3.write(item+"\n")
   
#Thanking the user before exiting the application
print("All your changes have been saved to the file tasklist.txt.")
print("Thank you for using the application, have a nice day!")