# CTI-110
# P4HW2 - Salary Calculator
# Sarah Perkins
# November 28, 2023
#

#Get employee name or termination of entering #

Emp_name = (input('Enter employee''s name or "Done" to terminate: \n'))
Emp_count = 0
Total_OT = 0
Total_reg = 0
Total_gross = 0

#Begin loop of entering employees until ended #

while Emp_name != "Done":
    
    print(f'How many hours did', Emp_name,'work?')
    Emp_hours = float(input())
    print(f"What is " + Emp_name + "'s pay rate?\n")
    Hourly_rate = float(input())
    
    print('Employee name:  ', Emp_name)
	
	#Determine regular and overtime hours #
    
    Overtime_hours = 0
    Reg_hours = 0
    
    if Emp_hours > 40:
        Overtime_hours = Emp_hours - 40
        Reg_hours = 40
    else:
        Overtime_hours = 0
        Reg_hours = Emp_hours
        
    # Calculate overtime, regular, and gross pay and display results #
    
    Overtime_rate = Hourly_rate * 1.5
    OT_pay = Overtime_hours * Overtime_rate
    Reg_pay = Reg_hours * Hourly_rate
    Gross_pay = OT_pay + Reg_pay
    
    print(' ')
    print('Hours Worked    Pay Rate    OverTime    OverTime Pay        Regular Pay        Gross Pay')
    print('-----------------------------------------------------------------------------------------------------')
    print(Emp_hours, '          ', Hourly_rate, '      ', Overtime_hours, '       ', OT_pay, '            $' , Reg_pay,  '            $', Gross_pay)
    
	#Count number of employees entered, calculate totals for overtime, regular, and gross wages #
	
    Emp_count = Emp_count + 1
    Total_OT = Total_OT + OT_pay
    Total_reg = Total_reg + Reg_pay
    Total_gross = Total_gross + Gross_pay
	
	#Determine if another employee is going to be entered #
    
    print('')  
    print('')
    Emp_name = (input('Enter employee''s name or "Done" to terminate: \n'))
    
#Display total number of employees entered and total amounts paid for overtime, regular and gross wages #

print('')
print('Total number of employees entered:', Emp_count)
print(f'Total amount paid for overtime: ${Total_OT:.2f}')
print(f'Total amount paid for regular hours: ${Total_reg:.2f}')
print(f'Total amount paid in gross: ${Total_gross:.2f}')

