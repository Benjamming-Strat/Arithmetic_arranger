import sys

problem_list = []




def add_problem(problem):
    problem_list.append(problem)
    
    if len(problem_list)>5:
        print("Error: Too much problems in your List - Python will automatically shut down")
        sys.exit()
    # return problem_list

def print_error():
        print("List of problems: ", end="")
        print(problem_list)
        