import db
class Bank(object):
	balance=0
	def __init__(self, arg):
		self.arg = arg

	def get_user(self,account,password):
		for person in db.all_people:
			if(person['user_name']==account and person["password"] == password):
				print "password exactly! Hello %s" % person['name']
				self.balance=person['balance']
				return person
		return False			

	def authenicate(self):
		account=raw_input("Your account _>")
		password=raw_input("Your password _>")
		user=self.get_user(account,password);
			
		i=1
		while(user==False):
			if(i==3):
				print "You input wrong pass more than 3 time!"
				return False
				
			print "Wrong user or password! please retry  ! or press CTRL+C to exit!"
			account= raw_input("Retry your account _>")
			password= raw_input("Retry your password _>")
			user=self.get_user(account,password);
			i=i+1
		
		return True
	def withdrawal(self):
		amount=int(raw_input("Amount to withdrawal_>"))
		while(amount > self.balance):
			print "Balance was not enough to withdrawl(press CTR+C to exit!)"
			amount=raw_input("Retry amount to withdrawl_>")
		self.balance = self.balance - amount
		print "withdrawal success! Now, amount in bank is %d. Thank you! " % self.balance
	def deposit(self):
		amount=int(raw_input("Amount to deposit>"))
		while(amount < 1):
			print "Amount must me >=1 (press CTR+C to exit!)"
			amount=raw_input("Retry amount to deposit _>")
		self.balance = self.balance + amount
		print "deposit success! Now, amount in bank is %d. Thank you! " % self.balance



stock= Bank("abc")
if stock.authenicate():
	print "What do you want to do? "
	do_action =raw_input("input 1: witdrawal, input 2: deposit _>")
	
	if do_action=="1":
		stock.withdrawal()
	elif do_action =="2":
		stock.deposit()
	else:
		while (do_action != "1" or do_action !="2"):
			print "you must be input 1 or 2"
			do_action =raw_input("input 1: witdrawal, input 2: deposit, 3: exit _>")	
			if do_action=="1":
				stock.withdrawal()
			elif do_action =="2":
				stock.deposit()
			elif do_action =="0":
				break
	