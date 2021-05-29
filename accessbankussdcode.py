print('welcome To Access Bank Ussd code Transaction ')
def check():
	if len(pin) == 4:
		print('your account balance is',balance,'Naira')
	else:
		pin = input('Enter pin to continue:')
def Airtime():
	print('Buy Airtime\n1.Self\n2.Other')
	Airtime_option = int(input(':'))
	if Airtime_option == 1:
		amount = int(input('Enter amount:'))
		print('transaction successifull')
	elif Airtime_option == 2:
		amount = int(input('Enter amount:'))
		phone_number = int(input('Enter number:'))
		print('Are you sure you want to Transfer',amount,'Naira to',phone_number,'\n1.YES\n2.NO')
		Airtime_Assure = int(input(':'))
		print('transaction successifull') 
		exit()
def return_option():
	while True:
		pass
		option = int(input('select option:'))
		print('''--------------------------------------------------''')
		if option == 1:
			pin = input('Enter four Digit pin to continue:')
			if len(pin) == 4:
				print('your account balance is',balance,'Naira')
				break
			else:
				print('Wrong pin')
				pin = input('Enter four Digit pin to continue:')
				
			break
		elif option == 2:
			amount = int(input('Enter amount:'))
			account_number = int(input('Enter account:'))
			print('''------------------------------------------------''')
			list_of_accont_number.append(account_number)
			find_name = list_of_accont_name[0]
			print('1.Access Bank\n2.Zenith Bank\n3.First Bank')
			print('''----------------------------------------------''')
			beneficiary_bank = int(input('Select beneficiary bank: '))
			for x in range(0,4):
				if x == beneficiary_bank:
					print('you want to Transfer',amount,'to',find_name,'.\nEnter four Digit pin to continue')
			print('''-------------------------------------------------''')
			pin = input(':')
			if len(pin) == 4:
				print('transaction successifull')
				break 
			else:
				print('Wrong pin')
				print('''----------------------------------------------''')
				print('you want to Transfer',amount,'to',find_name,'.\nEnter four Digit pin to continue')
				pin = input(':')
				print('transaction successfull')
			break
		elif option == 3:
			print('Buy Airtime\n1.Self\n2.Other')
			Airtime_option = int(input(':'))
			if Airtime_option == 1:
				amount = int(input('Enter amount:'))
				print('transaction successfull')
				break
			elif Airtime_option == 2:
				amount = int(input('Enter amount:'))
				phone_number = int(input('Enter number:'))
				print('Are you sure you want to Transfer',amount,'Naira to',phone_number,'\n1.YES\n2.NO')
				Airtime_Assure =int(input(':')) 
				if Airtime_Assure == 1:
					print('transaction successfull')
					break
				else:
					Airtime_Assure == 2
					Airtime()
					break	
		elif option == 4:
			print('1> Pay Bills\n2> AccessPay\n3> Pay Day Loan \n4> Enquiry Saervices\n5> Reset pin\n6> cardless Withdrawal\n7> Referra Scheme\n8> Update info\n9> Opt Out')
			print('''----------------------------------------------''')
			other_services_option = int(input(':'))
			if other_services_option == 1:
				print('select biller\n1>DSTV\n2>GOTV\n3>LCD\n4>Data purchase\n5>Bet9ja\n6>Other billes')
				print('''----------------------------------------------''')
				biller_option = int(input(':'))
				for x in range(0,7):
					
					if x == biller_option:
						print('Sorry, this service is corrently unavailable.\nWe are working to restore it soon.\n kindly use our alternative channels')
			elif other_services_option == 2:
				print('Select your option\n1>Make payment\n2>Biller last number of Transaction\n3>Enroll as biller\n4>My payment code')
				print('''----------------------------------------------''')
				account_pay = int(input(':'))
			elif other_services_option == 3:
				print('Dear customer, access more with Access Bank!\nOpen a salary account today to be\neligible for this product. Call 0700300000\nto get started')
				break
			elif other_services_option == 4:
				print('Sorry, this service is corrently unavailable.\nWe are working to restore it soon.\n kindly use our alternative channels')
				break
			elif other_services_option == 5:
				print('Sorry, this service is corrently unavailable.\nWe are working to restore it soon.\n kindly use our alternative channels')
				break
			elif other_services_option == 6:
				print('Sorry, this service is corrently unavailable.\nWe are working to restore it soon.\n kindly use our alternative channels')
				break
			elif other_services_option == 7:
				print('Sorry, this service is corrently unavailable.\nWe are working to restore it soon.\n kindly use our alternative channels')
				break
			elif other_services_option == 8:
				print('Sorry, this service is corrently unavailable.\nWe are working to restore it soon.\n kindly use our alternative channels')
				break
			elif other_services_option == 9:
				print('Sorry, this service is corrently unavailable.\nWe are working to restore it soon.\n kindly use our alternative channels')
				break
			else:
				print('Wrong comand')
			break
		elif option == 5:
			print('Sorry, this service is corrently unavailable.\nWe are working to restore it soon.\n kindly use our alternative channels')
			break

		elif option == 6:
			print('Selec option\n1> Send money\n2> Get a loan\n3> Pay Bills\n4> AccessPay\n5> Withdraw money')
			print('''----------------------------------------------''')
			print('Sorry, this optons can not be access now We are working on then')
		

		elif option == 7:
			print('Dear customer, access more with Access Bank!\nOpen a salary account today to be\neligible for this product. Call 0700300000\nto get started')
			break

		elif option == 8:
			print('Sorry, this service is corrently unavailable.\nWe are working to restore it soon.\n kindly use our alternative channels')
			break
		else:
			return_option()
			break

while True:
	list_of_accont_name = ['Sani busu mohammed']
	list_of_accont_number = []
	# account_pin = 2000
	balance = 5000000
	ussd_code = int(input("Enter ussd code here: "))
	if ussd_code == 901:
		print('''-------------------------------------------------''')
		print('Access bank')
		print("1.check balance\n2.Transfer\n3.Airtime\n4.other services\n5.Access money\n6.Diamond Extra\n7.Extra cash loan\n8.Mobile wallet")
		print('''--------------------------------------------------''')
		return_option()
		break
	else:
		print('you have enterd a wrong ussd code')
		


