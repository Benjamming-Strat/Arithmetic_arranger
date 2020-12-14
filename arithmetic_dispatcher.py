#retrieving a list of numbers that have to be added or subtracted - printed out vertically
import problem_counter, re


def menu():
    print("""        #############################################\n\
        This is the menu for our arithmetic arranger!\n\
        chose a number between -9999 and +9999,\n\
        dont use chars,and only use addition an subtraction\n\
        ##############################################\n\
        ##############################################""")


def artithmetic_arranger(string_list):
    
    result_list = []
    #checking list for problem - no multiplication or division , only digits and numbers between -9999 and +9999
    for i in range(len(string_list)):

        # checl multiplication
        if "*" in string_list[i]:
            multiplication_counter += 1
            error = "Multiplication is not possible: " + string_list[i]
            problem_counter.add_problem(error)
            
        # check division
        elif "/" in string_list[i]:
            divisioncounter += 1 
            error = "Division is not possible: " + string_list[i]
            problem_counter.add_problem(error)
            

        #check -9999 < x < +9999
        #checking if digits only
        number = re.split("[+|\-|/|*]",string_list[i])
        for char in number:
            if len(char)>4:
                error_len = "Number is too big: "+ char
                problem_counter.add_problem(error_len)
            
            elif not char.isdigit():
                
                error = "Only Numbers, check: "+ char
                problem_counter.add_problem(error)
    
    for element in string_list:
        
        
        split_element = re.split("[+|-]",element)
        
        if "+" in element:
            
            int_list = [int(x) for x in split_element]
            result = sum(int_list)
            result_list.append(result)

            

            if len(str(int_list[0])) > len(str(int_list[1])):
                ddunder_length = len(str(int_list[0])) + 3
            else:
                ddunder_length = len(str(int_list[1])) + 3

            print(str(int_list[0]).rjust(10) +"\n" + (" + " + str(int_list[1])).rjust(10) + "\n"  +str("_"*ddunder_length).rjust(10) + "\n" + str(result).rjust(10))
            print()
                
        elif "-" in element:
            int_list = [int(x) for x in split_element]
            result = int_list[1] - int_list[0]
            result_list.append(result)

            if len(str(int_list[0])) > len(str(int_list[1])):
                ddunder_length = len(str(int_list[0])) + 3
            else:
                ddunder_length = len(str(int_list[1])) + 3

            print(str(int_list[0]).rjust(10) +"\n" + (" - " + str(int_list[1])).rjust(10) +"\n" +str("_"*ddunder_length).rjust(10) + "\n" + str(result).rjust(10))
            print()   
    print(result_list)
            

            
            
        
            
string_list=["33+33","2+8","1999+1","2000-5000","55+66"]           
menu()
artithmetic_arranger(string_list)
problem_counter.print_error()






    # #if operant is plus
    # if "+" in string_list[i]:
    #     split_string_list = string_list[i].split("+")
    #     try:
    #         for number in split_string_list:
    #             number = int(number)
    #             # if len(str(number))>4:
    #             #     problem_counter.add_problem("More than 4 digits")
                    
    #             sum_list.append(number)
    #         sume = sum(sum_list)    
    #         result_list.append(sume)


    #         if len(str(sum_list[0])) > len(str(sum_list[1])):
    #             ddunder_length = len(str(sum_list[0]))+3
    #         else:
    #             ddunder_length = len(str(sum_list[1]))+3
            
    #         #print results

    #         print(str(sum_list[0]).rjust(10) + "\n"+(" + "+str(sum_list[1])).rjust(10)+ "\n" + ("_"*ddunder_length).rjust(10) +"\n"+ str(result_list[i]).rjust(10), end=" ")
            

    #     except TypeError:
    #         print("not parsing possible")


    # #if operant is minus
    # elif "-" in string_list[i]:
    #     split_string_list = string_list[i].split("-")
    #     try:
    #         for number in split_string_list:
                
    #             number = int(number)
    #             # if len(str(number))>4:
    #             #     problem_counter.add_problem("More than 4 digits")
    #             sub_list.append(number)
            
    #         result = sub_list[0]-sub_list[1]
    #         result_list.append(result)   

    #         if len(str(sub_list[0])) > len(str(sub_list[0])):
    #             ddunder_length = len(str(sub_list[0])) + 3
    #         else:
    #             ddunder_length = len(str(sub_list[1])) + 3

    #         #print results

    #         print(str(sub_list[0]).rjust(10) + "\n"+(" - "+str(sub_list[1])).rjust(10)+ "\n"+("_"*ddunder_length).rjust(10) +"\n"+ str(result_list[i]).rjust(10), end=" ")     
            
    #     except TypeError:
    #         print("could not convert into integer")



    







        
            

            
            


    


