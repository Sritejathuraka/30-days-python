## Error Handling
def atm_withdrawal():
    try:
        print("Karthik entered the ATM.")
        print("Karthik inserted ATM card.")

        pin = int(input("Enter Pin: "))
        if pin != 1212:
            raise ValueError("Entered Pin mismatched")
        
        amount = int(input("Enter amount to withdraw: "))
        if amount > 1000:
            raise Exception("Insufficient Balance!")

        print(f"${amount} withdrawn successfully. 💸")
    except ValueError as ve:
        print(ve, "Please enter correct pin")
    except Exception as e:
        print(e, "your account balance is $1000. Please enter accordingly")
    finally:
        print("Card ejected, Please take out the card")
        

    
# Run the function
atm_withdrawal()
