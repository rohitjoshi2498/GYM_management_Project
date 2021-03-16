class Gym_Rohit:
    
   
    
    def __init__(self):
        self.all_member_info={}               #to store the dict_store as member id
        self.mem_id = 100
        self.dict_store={}                    #to store the name,age and other details
        self.dict_super_mb={}
        self.dict1_18={}                        #to store the bmi<18.5
        self.dict1_25={}                        #to store the bmi<25
        self.dict1_30={}                        #to store the bmi<30
        self.dict1_m30={}                       #to store the bmi>30
        self.regimen_store={}
        

    def intro_Member(self):
        print('Hello Sir!!')
        print('Please Select what you want to view from the Following options:- ')
        print('1. My Regimen')
        print('2. My Profile')
        print('3. Main Menu')
        option_mem=int(input())
        if option_mem ==  1:
            self.mem_regimen()
        elif option_mem == 2:
            self.mem_profile()
        elif option_mem == 3:
            self.open_gym()
        
   
        
    def intro_Superuser(self):
        print('Please Select from the Following options:- ')
        print('1. Create a New Membership')
        print('2. View Membership')
        print('3. Cancel the Membership')
        print('4. Update Membership ')
        print('5. Create Regimen')
        print('6. View Regimen')
        print('7. Delete Regimen')
        print('8. Update Regimen')
        print('0. If you want to exit')
        option_super = int(input("Enter an option"))
        
        if option_super == 1:
            self.create_mem()    
        elif option_super == 2:
            self.view_mem()
        elif option_super == 3:
            self.cancel_mem()
        elif option_super == 4:
            self.update_mem()
        elif option_super ==5:
            self.create_regimen()
        elif option_super == 6:
            self.view_regimen()
        elif option_super == 7:
            self.delet_regimen()
        elif option_super == 8:
            self.update_regimen()
        elif option_super == 0:
            self.open_gym()
        else:
            print("Please try again!!!!!")
            self.intro_Superuser()
       
    
    
    def create_mem(self):
        
        print('To create a member, kindly enter your details ')
        self.name=input('Enter Name ')
        self.age=int(input('Enter Age '))
        self.gender=input('Enter your Gender ')
        self.phone=int(input('Enter your mobile number '))
        self.email=input('Enter your email ')
        self.bmi=float(input('Enter your BMI '))
        self.membership_mnths=int(input('Enter the membership duration 1,3,6 or 12 months '))
        self.mem_id +=1
        print('**',self.mem_id,'** this is your member id, kindly enter whenver prompted ')
        
        
                                                            #storing the member details in dict_store
        self.dict_store["Name"]=self.name
        self.dict_store["Gender"]=self.gender
        self.dict_store["Age"]=self.age
        self.dict_store["BMI"]=self.bmi
        self.dict_store["Mobile_No"]=self.phone
        self.dict_store["Email-id"]=self.email
        self.dict_store["Membership Duration(months)"]=self.membership_mnths
        self.dict_store["Member_ID"]=self.mem_id
        self.dict_store["Status"]="Subscription_ON"
        
        self.all_member_info[self.mem_id] = self.dict_store     #storing the dict_store as a key to all_member_info dict
        
        self.dict_super_mb[self.phone] =self.dict_store         #superuser get to know about the user thriugh mobile
        
        
        self.intro_Superuser()
        
    def view_mem(self):
        self.option3=int(input('Enter the member mobile number to get the details '))
        for k in self.dict_super_mb[self.option3]:
            print(k,self.dict_super_mb[self.option3][k])
        cont=input('Do you want to coontinue\nYes or No ')
        if cont =="Yes" or cont=='yes':
            self.intro_Superuser()
        else:
            self.open_gym()
    
    def cancel_mem(self):
        self.take_inp=int(input('Please enter the Member Id '))
        self.all_member_info[self.take_inp]['Status']="Subscription_OFF"
        
        print('Your Subscription is cancelled')
        self.intro_Superuser()
        

            
            
    
    def update_mem(self):
        self.extd=int(input('Please enter the following \n1. Revoke Membership\n2. Extend membership '))
        if self.extd==1:
              
            self.all_member_info["Status"]= "Subscription_OFF"
            print('update inisde revoke ',self.all_member_info["Status"])
            
        elif self.extd==2:
            self.mobi=int(input('Enter the mobile number of the member '))
            self.mem_extnd=int(input('Enter for how many months you would like to extend 1,3,6 or 12 '))
            self.dict_super_mb[self.mobi]["Membership Duration(months)"]=self.mem_extnd           #for the super user
            self.all_member_info[self.mem_id]["Membership Duration(months)"]=self.mem_extnd          #for the membr
            print('Your memebership has extended upto ',self.dict_super_mb[self.mobi]["Membership Duration(months)"],' months')
        self.intro_Superuser()
                         
            
            
    def create_regimen(self):
        self.enter_bmi_id=int(input('For creating a regimen please enter the Member Id '))                                                                                    
        self.a = self.all_member_info[self.enter_bmi_id]["BMI"]

        self.dict1_18= {'Mon': 'Chest',
                        'Tue': 'Biceps',
                        'Wed': 'Rest',
                        'Thu': 'Back',
                        'Fri': 'Triceps',
                        'Sat': 'Rest',
                        'Sun': 'Rest'}
    
        self.dict1_25= {'Mon': 'Chest',
                        'Tue': 'Biceps',
                        'Wed': 'Cardio/Abs',
                        'Thu': 'Back',
                        'Fri': 'Triceps',
                        'Sat': 'Legs',
                        'Sun': 'Rest'}
        
        self.dict1_30= { 'Mon': 'Chest',
                        'Tue': 'Biceps',
                        'Wed': 'Abs/Cardio',
                        'Thu': 'Back',
                        'Fri': 'Triceps',
                        'Sat': 'Legs',
                        'Sun': 'Cardio'}
        
        self.dict1_m30={ 'Mon': 'Chest',
                        'Tue': 'Biceps',
                        'Wed': 'Cardio',
                        'Thu': 'Back',
                        'Fri': 'Triceps',
                        'Sat': 'Cardio',
                        'Sun': 'Cardio'}
        if self.a <= 18.5:
            self.regimen_store[self.enter_bmi_id]=self.dict1_18
            print(self.regimen_store[self.enter_bmi_id])
        elif self.a > 18.5  and self.a <= 25:
            self.regimen_store[self.enter_bmi_id]=self.dict1_25

        elif self.a>25 and self.a <= 30:
            self.regimen_store[self.enter_bmi_id]=self.dict1_30

        elif self.a > 30: 
            self.regimen_store[self.enter_bmi_id]=self.dict1_m30

        else:
            print('Please Try Again')
            self.create_regimen()
            
        self.intro_Superuser()


    
    def view_regimen(self):
        self.ask_mem_id = int(input('To view the regimen please enter the member id '))
        print('Name: ',self.all_member_info[self.ask_mem_id]["Name"])
        print('Age: ',self.all_member_info[self.ask_mem_id]["Age"])
        if self.all_member_info[self.ask_mem_id] !='Deleted':
               for l in self.regimen_store[self.ask_mem_id]:
                    print(l,':',self.regimen_store[self.ask_mem_id][l])
        else:
            print('Member Not Found')
        self.intro_Superuser()
    
    def delet_regimen(self):
        self.ask_for_id = int(input('To view the regimen please enter the member id '))

        self.regimen_store[self.ask_for_id] ='Deleted'
        print('Your Regimen is Deleted ')
        self.intro_Superuser()
        
    def update_regimen(self):
        change_bmi=float(input('Enter your updated BMI'))
        updates_id=int(input('Enter your member ID'))
        self.all_member_info[updates_id]["BMI"] = change_bmi
        if change_bmi <=18.5:
            self.regimen_store[updates_id] = self.dict1_18
            print(self.regimen_store[updates_id])
        elif change_bmi > 18.5  and self.a <= 25:
            self.regimen_store[updates_id] = self.dict1_25

        elif change_bmi>25 and self.a <= 30:
            self.regimen_store[updates_id] = self.dict1_30

        elif change_bmi > 30: 
            self.regimen_store[updates_id] = self.dict1_m30
        print("Your Regimen updates succesfully ",self.all_member_info[updates_id]["BMI"]) 
        self.intro_Superuser()
        
    def mem_regimen(self):
        self.ask_mem_id1=int(input('To view the regimen please enter your Member id '))
#         print(self.all_member_info)
        print('Name: ',self.all_member_info[self.ask_mem_id1]["Name"])
        print('Age: ',self.all_member_info[self.ask_mem_id1]["Age"])
        for j in self.regimen_store.get(self.ask_mem_id1):
            print(j,':',self.regimen_store[self.ask_mem_id1][j])
        self.intro_Member()
        
        
            
    def mem_profile(self):
        self.ask_mem_id2=int(input('To view the Profile please enter your Member id '))
        print(self.all_member_info)
        for i in self.all_member_info.get(self.ask_mem_id2):
            print(i,self.all_member_info[self.ask_mem_id2][i])
        cont=input('Do you want to coontinue\nYes or No')
        if cont =="yes" or cont=='Yes':
            self.intro_Member()
        else:
            self.open_gym()
            
            

    def open_gym(self):
        inpu=int(input("********Welcome to RJ_FITNESS********\nPlease enter the following options: \n1. SuperUser\n2. Member\n\n"))

        if inpu ==1:
            password=input('Please enter the password for super ')
            if password =="super@123":
                self.intro_Superuser()
        elif inpu==2:
            self.intro_Member() 
        else:
            self.open_gym()


if __name__ == "__main__":
    Rohit = Gym_Rohit()
    Rohit.open_gym()
    
        
