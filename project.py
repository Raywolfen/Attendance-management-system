from random import random
from math import ceil
import names


#####################################################################################################
########################### CLASSES #################################################################
#####################################################################################################






class Student:
    def __init__(self, id, name, sect_id):
        self.id = id
        self.name = name
        self.sect_id = sect_id
        self.attendence = []

    def disp_stud(self):
        print(self.id, self.name)

    def add_attendence(self, aten_bool):
        self.attendence.append(aten_bool)

    def get_weekly_aten(self):
        i = 0
        c = 0
        try:
            while i < 5:
                if self.attendence[i]:
                    c += 1
                i += 1
        except IndexError:
            print("Sorry there was an index error")
        return (c / 5)

    def get_monthly_aten(self):
        i = 0
        c = 0
        try:
            while i < 22:
                if self.attendence[i]:
                    c += 1
                i += 1
        except IndexError:
            print("Sorry there was an index error")
        return (c / 22)

    def get_yearly_aten(self):
        i = 0
        c = 0
        try:
            while i < 198:
                if self.attendence[i]:
                    c += 1
                i += 1
        except IndexError:
            print("Sorry there was an index error")
        return (c / 198)


class Section:
    def __init__(self, sect_id, max_students):
        self.sect_id = sect_id
        self.stud_list = []
        self.max_students = max_students
        # think about it

    def set_teacher(self, teacher_id):
        self.teacher_id = teacher_id

    def get_student(self, stud_id):
        for x in self.stud_list:
            if x.id == stud_id:
                return x

    def disp_sect(self):
        print(self.sect_id)
        for x in self.stud_list:
            x.disp_stud()


class Year:
    def __init__(self, year_id, max_per_sect):
        self.year_id = year_id
        self.max_per_sect = max_per_sect
        self.sect_list = []

    def __init__(self, max_per_sect):
        global year_count
        self.year_id = year_count
        year_count += 1
        self.max_per_sect = max_per_sect
        self.sect_list = []

    def disp_year(self):
        #print(self.year_id)
        #print(self.max_per_sect)
        #print(self.num_students)
        for x in self.sect_list:
            x.disp_sect()

    def newest_sect(self):
        i = len(self.sect_list)
        if len(self.sect_list[len(self.sect_list)-1].stud_list) == self.max_per_sect:
            self.sect_list.append(Section(chr(65 + i), self.max_per_sect))
            return i
        else:
            return i-1

    def getYear(self):
        return self.year_id

    #def checkSection(self):
        # Returns the next free section (Will create one if not available)



#####################################################################################################
########################### FUNCTIONS ###############################################################
#####################################################################################################


def charToInt(c):
    if c == 'a' or c == 'A':
        return 0
    elif c == 'b' or c == 'B':
        return 1
    elif c == 'c' or c == 'C':
        return 2
    elif c == 'd' or c == 'D':
        return 3
    elif c == 'e' or c == 'E':
        return 4
    elif c == 'f' or c == 'F':
        return 5
    elif c == 'g' or c == 'G':
        return 6
    elif c == 'h' or c == 'H':
        return 7
    elif c == 'i' or c == 'I':
        return 8
    elif c == 'j' or c == 'J':
        return 9
    elif c == 'k' or c == 'K':
        return 10
    elif c == 'l' or c == 'L':
        return 11
    elif c == 'm' or c == 'M':
        return 12
    elif c == 'n' or c == 'N':
        return 13
    elif c == 'o' or c == 'O':
        return 14
    elif c == 'p' or c == 'P':
        return 15
    elif c == 'q' or c == 'Q':
        return 16
    elif c == 'r' or c == 'R':
        return 17
    elif c == 's' or c == 'S':
        return 18
    elif c == 't' or c == 'T':
        return 19
    elif c == 'u' or c == 'U':
        return 20
    elif c == 'v' or c == 'V':
        return 21
    elif c == 'w' or c == 'W':
        return 22
    elif c == 'x' or c == 'X':
        return 23
    elif c == 'y' or c == 'Y':
        return 24
    elif c == 'z' or c == 'Z':
        return 25


def intToChar(c):
    if c == 0:
        return 'A'
    elif c == 1:
        return 'B'
    elif c == 2:
        return 'C'
    elif c == 3:
        return 'D'
    elif c == 4:
        return 'E'
    elif c == 5:
        return 'F'
    elif c == 6:
        return 'G'
    elif c == 7:
        return 'H'
    elif c == 8:
        return 'I'
    elif c == 9:
        return 'J'
    elif c == 10:
        return 'K'
    elif c == 11:
        return 'L'
    elif c == 12:
        return 'M'
    elif c == 13:
        return 'N'
    elif c == 14:
        return 'O'
    elif c == 15:
        return 'P'
    elif c == 16:
        return 'Q'
    elif c == 17:
        return 'R'
    elif c == 18:
        return 'S'
    elif c == 19:
        return 'T'
    elif c == 20:
        return 'U'
    elif c == 21:
        return 'V'
    elif c == 22:
        return 'W'
    elif c == 23:
        return 'X'
    elif c == 24:
        return 'Y'
    elif c == 25:
        return 'Z'


def adminMenu():
    inp = 0
    while inp != 7:
        print("Welcome to the Admin Menu!")

        print("1) Add Class")
        print("2) Add Section")
        print("3) Add Student to a class")
        print("4) Allocate Staff to a section")
        print("5) Check Attendance")
        print("6) Display all students in the school")
        print("7) Exit")
        try:
            inp = int(input("What would you like to do:"))
        except:
            print("Invalid input, please input an integer")

        if inp == 1:
            addClass()
        elif inp == 2:
            addSection()
        elif inp == 3:
            add_student()
        elif inp == 4:
            add_staff()
        elif inp == 5:
            checkAttendance()
        elif inp == 6:
            display()
        elif inp != 7:
            print("Invalid input, try again")


def userMenu():
    print("Welcome to the User Menu!")
    while True:
        stn = int(input("Please input your student number to login:"))
        if stn > len(stud_dict) or stn < 1:
            print("Invalid student number. Please try again.")
        else:
            break

    # Maybe add a welcome message using the student's number / name

    inp = 0
    while inp != 2:


        print("1) Get attendance")
        print("2) Exit")

        inp = int(input("What would you like to do:"))

        if inp == 1:
            while inp != 4:
                print("How would you like to view your attendance?")
                print("1) View weekly attendance")
                print("2) View Monthly attendance")
                print("3) View Yearly attendance")
                print("4) Exit")
                inp = int(input("What would you like to do:"))

                if inp == 1:
                    getAttendance(stn, 1)
                elif inp == 2:
                    getAttendance(stn, 2)
                elif inp == 3:
                    getAttendance(stn, 3)
                elif inp != 4:
                    print("Invalid input, try again")

        elif inp != 2:
            print("Invalid input, try again")


def checkAttendance():
    while True:
        inp = int(input("For which class would you like to check attendance?"))
        if inp < len(stud_dict):
            break
        print("Invalid year, try again")

    while True:
        str_inp = str(input("For which section would you like to check attendance?"))
        char_inp = charToInt(str_inp)
        if char_inp < len(year_list[inp-1].sect_list):
            break
        print("Invalid section, try again")

    print("Here is the attendance for that section:")

    l = year_list[inp-1].sect_list[char_inp].stud_list
    leng = len(l)
    i = 0
    b = "Present"

    while i < leng:
        if l[i].attendence[0]:
            b = "Present"
        else:
            b = "Absent"
        print(l[i].name, "-", b)
        i += 1

    print()


def getAttendance(stn, n):
    s = stud_dict[stn]
    year_id = int(s[0:1])
    sect_id = charToInt(s[1:2])
    if n == 1:
        x = (year_list[year_id - 1].sect_list[sect_id].get_student(stn).get_weekly_aten())
        x *= 100
        x = "{:.2f}".format(x)
        st = "Your attendance this week was " + str(x) + "%"
        print(st)
    if n == 2:
        x = (year_list[year_id-1].sect_list[sect_id].get_student(stn).get_monthly_aten())
        x *= 100
        x = "{:.2f}".format(x)
        st = "Your attendance this month was " + str(x) + "%"
        print(st)
    if n == 3:
        x = (year_list[year_id - 1].sect_list[sect_id].get_student(stn).get_yearly_aten())
        x *= 100
        x = "{:.2f}".format(x)
        st = "Your attendance this year was " + str(x) + "%"
        print(st)


    print()


def addClass():
    year_list.append(Year(24))
    # Do we ask the admin what the max_per_sect variable should be for this year??
    # Do we populate our new year with students???
    print("Class Added! :D")



def addSection():

    try:
        inp = int(input("In which year would like to add a section?:"))
        year_list[inp-1].sect_list.append(Section(chr(64 + inp), year_list[inp-1].max_per_sect))
        print("Successfully added Section :)")
    except:
        print("Error occurred while trying to add a section")


def add_staff():
    try:
        inp_year = int(input("Enter year:"))
        inp_sect = str(input("Enter section:"))
        teach_id = int(input("Enter teacher ID:"))
        sect_id = charToInt(inp_sect)
        year_list[inp_year-1].sect_list[sect_id].set_teacher(teach_id)
        print("Successfully assigned Teacher :)")
    except IndexError:
        print("Index out of bounds error")
    except:
        print("Error occurred while trying to assign Teacher")


def add_student():
    try:
        inp_year = int(input("Enter year:"))
        inp_name = str(input("Enter the student's name"))
        ind = year_list[inp_year-1].newest_sect()
        year_list[inp_year-1].sect_list[ind].stud_list.append(Student(stud_count, inp_name, intToChar(ind)))
        sect = str(inp_year) + intToChar(ind)
        print("Successfully added student",inp_name,"to section",sect)
    except:
        print("Something went wrong while trying to add a student")


def display():
    for x in year_list:
        print("This is the students in year", x.getYear())
        x.disp_year()


def init():
    global year_list
    global year_count
    global stud_count
    global stud_dict

    i = 0
    while i < 6:
        r = ceil(random() * 50 + 50)
        year_list.append(Year(24))
        year_list[i].num_students = r
        i += 1

    # Divide each set of kids into sections
    i = 0
    j = 0
    k = 0


    while i < 6:
        sects = ceil(year_list[i].num_students / year_list[i].max_per_sect)
        while j < sects:
            year_list[i].sect_list.append(Section(chr(65 + j), year_list[i].max_per_sect))
            while k < (year_list[i].max_per_sect) and (year_list[i].max_per_sect * j + k) < year_list[i].num_students:
                # Make a new section


                # Add kids to the section
                year_list[i].sect_list[j].stud_list.append(Student(stud_count, names.get_full_name(), chr(65 + j)))

                x = 0
                while x < 200:
                    r = random()
                    if r > 0.95:
                        year_list[i].sect_list[j].stud_list[k].add_attendence(False)
                    else:
                        year_list[i].sect_list[j].stud_list[k].add_attendence(True)

                    x+=1

                #printAttendance(year_list[i].sect_list[j].stud_list[k])

                stud_dict[stud_count] = str((i+1)) + chr(65 + j)
                stud_count += 1
                k += 1
            j += 1
            k = 0
        i += 1

        j = 0


def printAttendance(stud):
    x=0
    while x < 200:
        print(stud.attendence[x])
        x+=1


#####################################################################################################
########################### MAIN ####################################################################
#####################################################################################################


global year_list
global year_count
global stud_count
global stud_dict

stud_dict = {}
year_list = []
year_count = 1
stud_count = 1




init()
#display()



inp = 0
while inp != 3:
    print("Welcome to the Attendance Management System (AMS)")

    print("1) Login as Admin")
    print("2) Login as User")
    print("3) Exit")

    inp = int(input("What would you like to do:"))

    if inp == 1:
        adminMenu()
    elif inp == 2:
        userMenu()
    elif inp != 3:
        print("Invalid input, try again")


    print("Goodbye!")

