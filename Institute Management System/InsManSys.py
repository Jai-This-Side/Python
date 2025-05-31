print("\t\t\t\t\t ~~~~ Imarticus Mega ~~~~")
print("\t\tPress 1 for Admission enquiry")
print("\t\tPress 2 for Employee details")
print("\t\tPress 3 for student details")

Choice_1 = int(input("\n\tEnter according to your choice :\t"))

if Choice_1 == 1 :

   New_name = str(input("Enter your name to continue :\t"))
   New_course = str(input("Enter the course name you are interested in :\t"))

   with open('C:\\Users\\MSI1\\OneDrive\\Documents\\python codes\\NewNames.txt', 'a') as file:
      file.write(New_name + '\n')

   with open('C:\\Users\\MSI1\\OneDrive\\Documents\\python codes\\lang.txt', 'r') as file:
      file_lang = file.read()

      course_list = file_lang.split('\n')

   if New_course in course_list:
      print("course available! contact us through our contact number 966766###4 or email us at imarticus@outlook.com")

   else:
      print("Sorry to say but the course is not available at this moment")

password = "aman01"

if Choice_1 == 2 :
   
   Emp_name = str(input("Enter your name :\t"))
   passw = str(input('Enter the password for access :\t'))

   with open('C:\\Users\\MSI1\\OneDrive\\Documents\\python codes\\EmployeeEntry.txt', 'a') as file:
      file.write(Emp_name + '\n')

   if passw == password:
      print("access granted")

   else :
      print("invalid password")

   print("What is the today's shedule of yours") 
   batch_2 = str(input("Which language would you be teaching to the first batch\n"))
   batch_3 = str(input("Which language would you be teaching to the second batch\n"))
   batch_4 = str(input("Which language would you be teaching to the third batch\n"))
   batch_5 = str(input("Which language would you be teaching to the fourth batch\n"))

   table = [
       ['Batch', 'Language'],
       ['1st Batch', batch_2],
       ['2nd Batch', batch_3],
       ['3rd Batch', batch_4],
       ['4th Batch', batch_5]
   ]
   for row in table:
       print('{:<10} {:<15}'.format(*row))
   
if Choice_1 == 3:
   name = str(input("Name of student you want to search for\t"))

   with open('StudentDetails.txt', 'r') as file:
      StudentDetails = file.read()

      StudentMatch = StudentDetails.split('\n')

   if name in StudentMatch:
      print("The student is from Imarticus Mega. What do you want to know about him?")

   else:
      print("Sorry the student with the name provided does not belong to Imarticus Mega")

   
