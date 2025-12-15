amount= int(input("Enter amount: "))
notes500= amount//500
notes100= (amount%500)//100
notes50= ((amount)%100)//50
print("500 notes:", notes500)
print("100 notes:", notes100)
print("50 notes:", notes50)