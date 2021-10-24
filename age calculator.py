# Python3 code to calculate age in years 
while True:
        from datetime import date 

        def calculateAge(born): 
                today = date.today() 
                try: 
                        birthday = born.replace(year = today.year) 

                # raised when birth date is February 29 
                # and the current year is not a leap year 
                except ValueError: 
                        birthday = born.replace(year = today.year, 
                                        month = born.month + 1, day = 1) 

                if birthday > today: 
                        return today.year - born.year - 1
                else: 
                        return today.year - born.year 
        year1 = int(input("enter your birth year: "))
        month1 = int(input("enter your birth month: "))
        day1 = int(input("enter your birth day: "))
        # Driver code 


        print("you are" ,calculateAge(date( year1,month1,day1)) + 1, "years old") 
