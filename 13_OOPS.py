# A class variable is a variable that is shared by all objects of the class.

# shared properties = Class Variables


# A class method is used to access or modify class variables.

# @classmethod
# cls 




class OurBank:

    def __init__(self,name,place,balance):
        self.name = name
        self.place = place 
        self.total_amount = 0
        self.balance = balance
        OurBank.increment_cust_count()

    # CLASS VARIABLES 
    BankName = 'OurBank Private Limited' 
    FixedDeposit_InterestRate = 5
    Total_no_of_customers = 0

    # CLASS METHOD
    @classmethod
    def class_method_(cls):

        # Will play with Class variables (We will generally access the instance variables)
        print("Hey you are enjoying the services of ",cls.BankName)
        print("We are providing a fixed deposit service with interest rate of ",cls.FixedDeposit_InterestRate)
        print(OurBank.BankName,OurBank.FixedDeposit_InterestRate)

    @classmethod 
    def increment_cust_count(cls):
        cls.Total_no_of_customers = cls.Total_no_of_customers + 1
        print("Total no of customers registered in the bank is -> ", cls.Total_no_of_customers)


obj = OurBank('A','TPT',1000)
