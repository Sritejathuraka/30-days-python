## ** Conditional Statements **


## if elif
arjun_decision = int(input("Enter 0 for Park or 1 for Mall:"))

if arjun_decision == 0: 
  print("Arjun decided to go Park")
elif arjun_decision == 1:
 print("Arjun decided to go Mall")
else:
  print("Arjun not yet decided")

  
   
## Match Statement
color = input("Enter color: ")

match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Get ready")
    case "green":
        print("Go")
    case _:
        print("Invalid color")