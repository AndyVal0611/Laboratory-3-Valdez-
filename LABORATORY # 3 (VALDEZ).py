#start

#initialize the variables
Company = " "
Department = " "
Employee_code = 0
Employee_name = " "
Salary_cutoff_date = 0
Pay_period = 0
Basic_pay = 0
Rate_per_hour = 0
Hours_per_payday = 0
Overtime = 0
Absences = 0
Honorarium = 0
Tardiness = 0
Withholding_tax = 0
SSS_contribution = 0
HDMF_contribution = 100.00
Philhealth_contribution = 0
Deductions = 0
Gross_earnings = 0
Net_pay = 0

#input the required data for the employee
print("-------------------------------------------EMPLOYEE'S INFORMATION----------------------------------------------")
Company = (input("Enter Company name: "))
Department = (input("Enter Department name: "))
Employee_code = (input("Enter Employee code/number: "))
Employee_name = (input("Enter Employee's name: "))
Salary_cutoff_date = (input("Enter Salary Cut-off Date: "))
Pay_period = (input("Enter Pay Period: "))

#input the rate per hour, number of hours, overtime hours, absent hours, and tardy hours per payday of the employee
print("                                                                                                               ")
Rate_per_hour = float(input("Enter Employee's rate per hour: "))
Hours_per_payday = float(input("Enter Employee's number of hours per payday: "))
Overtime_hours_per_payday = float(input("Enter Employee's overtime hours per payday: "))
Absent_hours_per_payday = float(input("Enter Employee's absent hours per payday: "))
Tardy_hours_per_payday = float(input("Enter Employee's tardy hours per payday: "))

#calculate the employee's basic pay, overtime, absences, honorarium, and tardiness
print("                                                                                                               ")
Basic_pay = Rate_per_hour * Hours_per_payday
Overtime = Overtime_hours_per_payday * Rate_per_hour
Absences = Absent_hours_per_payday * Rate_per_hour
Honorarium = Hours_per_payday * Rate_per_hour
Tardiness = Rate_per_hour * Tardy_hours_per_payday

#calculate the gross earnings
gross_earnings = Basic_pay + Overtime + Honorarium

#determine the conditional statement for SSS Contribution
def gross_earnings(SSS_contribution):
    if gross_earnings < 4250:
        SSS_contribution = 180
    elif 4250 <= gross_earnings <= 4749.99:
        SSS_contribution = 202.50
    elif 4750 <= gross_earnings <= 5249.99:
        SSS_contribution = 225
    elif 5250 <= gross_earnings <= 5749.99:
        SSS_contribution = 247.50
    elif 5750 <= gross_earnings <= 6249.99:
        SSS_contribution = 270
    elif 6250 <= gross_earnings <= 6749.99:
        SSS_contribution = 292.50
    elif 6750 <= gross_earnings <= 7249.99:
        SSS_contribution = 360
    elif 8250 <= gross_earnings <= 8749.99:
        SSS_contribution = 382
    elif 8750 <= gross_earnings <= 9249.99:
        SSS_contribution = 405
    elif 9250 <= gross_earnings <= 9749.99:
        SSS_contribution = 427
    elif 9750 <= gross_earnings <= 10249.99:
        SSS_contribution = 450
    elif 10250 <= gross_earnings <= 10749.99:
        SSS_contribution = 472
    elif 10750 <= gross_earnings <= 11249.99:
        SSS_contribution = 495
    elif 11250 <= gross_earnings <= 11749.99:
        SSS_contribution = 517
    elif 11750 <= gross_earnings <= 12249.99:
        SSS_contribution = 540
    elif 12250 <= gross_earnings <= 12749.99:
        SSS_contribution = 562
    elif 12750 <= gross_earnings <= 13249.99:
        SSS_contribution = 585
    elif 13250 <= gross_earnings <= 13749.99:
        SSS_contribution = 607
    elif 13750 <= gross_earnings <= 14249.99:
        SSS_contribution = 630
    elif 14250 <= gross_earnings <= 14749.99:
        SSS_contribution = 652
    elif 14750 <= gross_earnings <= 15249.99:
        SSS_contribution = 675
    elif 15250 <= gross_earnings <= 15749.99:
        SSS_contribution = 697
    elif 15750 <= gross_earnings <= 16249.99:
        SSS_contribution = 720
    elif 16250 <= gross_earnings <= 16749.99:
        SSS_contribution = 742.50
    elif 16750 <= gross_earnings <= 17249.99:
        SSS_contribution = 765
    elif 17250 <= gross_earnings <= 17749.99:
        SSS_contribution = 787
    elif 17750 <= gross_earnings <= 18249.99:
        SSS_contribution = 810
    elif 18250 <= gross_earnings <= 18749.99:
        SSS_contribution = 832
    elif 18750 <= gross_earnings <= 19249.99:
        SSS_contribution = 855
    elif 19250 <= gross_earnings <= 19749.99:
        SSS_contribution = 877
    else:
        SSS_contribution = 900

#determine the conditional statement for semi-monthly Philhealth contribution
def gross_earnings(Philhealth_contribution):
    if 0 <= gross_earnings < 10000:
        Philhealth_contribution = 500
    elif 10000.01 <= gross_earnings <= 99999.99:
        Philhealth_contribution = gross_earnings * 0.05
    elif gross_earnings == 100000:
        Philhealth_contribution = 5000
    else:
        Philhealth_contribution = 0

#determine the conditional statement of withholding tax
def gross_earnings(Withholding_tax):
    if 0 <= gross_earnings < 10417:
        Withholding_tax = 0
    elif 10417 <= gross_earnings <= 16666:
        Withholding_tax = 0 + 0.15/10417
    elif 16667 <= gross_earnings <= 33322:
        Withholding_tax = 937.50 + 0.20/16667
    elif 33333 <= gross_earnings <= 83332:
        Withholding_tax = 4270.70 + 0.25/33333
    elif 83333 <= gross_earnings <= 333332:
        Withholding_tax = 16770.70 + 0.30/83333
    else:
        Withholding_tax = 91770.70 + 0.35/333333

#calculate for deduction
Deductions = Absences + Tardiness + Withholding_tax + Philhealth_contribution

#calculate for net pay
Net_pay = Gross_earnings - Deductions

#display the following
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Company name:", Company)
print("Department:", Department)
print("Employee code:", Employee_code)
print("Employee name:", Employee_name)
print("Salary cut-off date:", Salary_cutoff_date)
print("Pay period:", Pay_period)
print("Basic pay:", Basic_pay)
print("Overtime:", Overtime)
print("Absences:", Absences)
print("Honorarium:", Honorarium)
print("Tardy:", Tardiness)
print("Withholding tax:", Withholding_tax)
print("SSS contribution:", SSS_contribution)
print("HDMF contribution:", HDMF_contribution)
print("Philhealth contribution:", Philhealth_contribution)
print("Deductions:", Deductions)
print("Gross earnings:", Gross_earnings)
print("Net Pay:", Net_pay)

#end
