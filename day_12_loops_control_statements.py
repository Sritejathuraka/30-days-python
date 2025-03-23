## Loop Control Statements
team_selection_list = [
    "Virat Kohli",
    "Rohit Sharma",
    "Jasprit Bumrah",
    "Shubman Gill",
    "KL Rahul",
    "Hardik Pandya",
    "Ravindra Jadeja",
    "Suryakumar Yadav",
    "Rishabh Pant",
    "Mohammed Siraj",
    "Kuldeep Yadav",
    "Shreyas Iyer"
]
print("no of players in list", len(team_selection_list))

# break - The break statement is used to immediately exit a loop (either for or while) before it has finished all its iterations. 
for player in team_selection_list:
    print(player)
    if player == "KL Rahul":
        break


# continue - The continue statement is used to skip the current iteration of a loop and move to the next iteration 
for player in team_selection_list:
    if player == "KL Rahul" or player == "Kuldeep Yadav":
        continue
    print(player)
    

# pass - it is a null statement or do nothing statement in Python.
# It acts as a placeholder where Python expects a statement but you don’t want to write any code yet.
for player in team_selection_list:
    if player == "KL Rahul":
        pass 