import csv

def write_into_csv(info_list):
    with open('student_info_csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact Number", "E-mail Id"])
            
        writer.writerow(info_list)
        
condition = True

while(condition):
    student_info = input("Enter student information in this format (Name, Age, Contact Number, E-mail Id): ")
    print("Entered Information: " + student_info)
    
    #split
    student_info_list = student_info.split(' ')
    print("Entered split up informaation is: " + str(student_info_list))
    
    write_into_csv(student_info_list)
    
    condition_check = input ("Enter (yes/no) for continue student details: ")
    if condition_check == "yes":
        condition = True
    elif condition_check == "no":
        condition = False
