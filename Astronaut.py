import csv
import random


class Astronaut:
    """Astronaut class"""
    def __init__(self,name,flight_hrs,status):
        self.__status=status
        self.__name=name
        self.__flight_time=flight_hrs
        self.__missions=[]
        self.__alma_mater=[]
        self.__undergrad_major=[]
        self.__grad_major=[]
    
    @property
    def name(self):
        return self.__name
    
    @property
    def status(self):
        return self.__status

    @property
    def flight_hours(self):
        return self.__flight_time

    @property
    def year(self):
        return self.__year

    @property
    def group(self):
        return self.__group

    @property
    def date_of_birth(self):
        return self.__birth_date

    @property
    def birth_place(self):
        return self.__birth_place

    @property
    def gender(self):
        return self.__gender

    @property
    def alma_maters(self):
        return self.__alma_mater

    @property
    def undergrad_majors(self):
        return self.__undergrad_major

    @property
    def graduate_majors(self):
        return self.__grad_major

    @property
    def military_rank(self):
        return self.__rank

    @property
    def military_branch(self):
        return self.__branch

    @property
    def space_flights(self):
        return self.__flights

    @property
    def space_walks(self):
        return self.__walks
    
    @property
    def space_walk_time(self):
        return self.__walk_time
    
    @property
    def missions(self):
        return self.__missions

    @property
    def death_date(self):
        return self.__death_date

    @property
    def died_on_mission(self):
        return self.__mission_death

    @property
    def death_mission(self):
        if self.__mission_death:
            return self.__missions[-1]
        else:
            return "didn't die on mission"
    
    @name.setter
    def name(self,new_name):
        self.__name=new_name
    
    @status.setter
    def status(self,new_status):
        self.__status=new_status

    @flight_hours.setter
    def flight_hours(self,fl_hrs):
        self.__flight_time=fl_hrs

    @year.setter
    def year(self,new_year):
        self.__year=new_year

    @group.setter
    def group(self,new_group):
        self.__group=new_group

    @date_of_birth.setter
    def date_of_birth(self,new_dob):
        self.__birth_date=new_dob

    @birth_place.setter
    def birth_place(self,place):
        self.__birth_place=place

    @gender.setter
    def gender(self,new_gender):
        self.__gender=new_gender

    @military_rank.setter
    def military_rank(self,new_rank):
        self.__rank=new_rank

    @military_branch.setter
    def military_branch(self,new_branch):
        self.__branch=new_branch

    @space_flights.setter
    def space_flights(self,num_flights):
        self.__flights=num_flights

    @space_walks.setter
    def space_walks(self,num_walks):
        self.__walks=num_walks
    
    @space_walk_time.setter
    def space_walk_time(self,walk_time):
        self.__walk_time=walk_time
    
    def add_mission(self,new_mission):
        self.__missions.append(new_mission)

    @death_date.setter
    def death_date(self,new_date):
        if self.status !="Deceased":
            print("This person isn't dead.")
        else:
            self.__death_date=new_date

    @died_on_mission.setter
    def died_on_mission(self,mission_fatality_bool):
        if self.status !="Deceased":
            print("This person isn't dead.")
        else:
            self.__mission_death=mission_fatality_bool


    def add_alma_mater(self,new_school):
        self.__alma_mater.append(new_school)

    def add_undergrad_major(self,new_major):
        self.__undergrad_major.append(new_major)

    def add_graduate_major(self,new_major):
        self.__grad_major.append(new_major)

    def __gt__(self,other):
        if self.__flight_time>other.__flight_time:
            return True
        else:
            return False
    
    def __eq__(self,other):
        if self.__flight_time==other.__flight_time:
            return True
        else:
            return False
    
    def __ge__(self,other):
        if self.__flight_time>=other.__flight_time:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.__name}, {self.__status}"


file=open(r"astronauts.csv",'r')
reader = csv.DictReader(file)
astronaut_list=[]
for row in reader:
    astronaut_list.append(Astronaut(row["Name"],row["Space Flight (hr)"],row["Status"]))

file.close()

astronaut1=random.choice(astronaut_list)
print(type(astronaut1))
astronaut2=random.choice(astronaut_list)
print(f"{astronaut1}, {astronaut1.flight_hours}")
print(f"{astronaut2}, {astronaut2.flight_hours}")
print(astronaut1>astronaut2)
print(astronaut1==astronaut2)
print(astronaut1>=astronaut2)
for i in range(len(astronaut_list)):
    print(astronaut_list[i])

