# Check for a valid input
try:
   accBal = float(input("Enter Account Balance: "))
except:
    print("Invalid Input")

# Check amount entered and format to GBP currency and two decimal places.
if accBal <1000 :
	print ("Your Interest would be: £", format(accBal * 0.001,",.2f"))
elif accBal >=1000 and <=5000
	print(accBal * 0.0015)
elif accBal >=5000 and <=10000
	print(accBal * 0.002)
elif accBal >=10000 and <=500000
	print(accBal * 0.0025)
elif accBal >=10000 and <=500000
	print(accBal * 0.003)
