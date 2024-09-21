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
Company = (input("Enter Company name: "))
Department = (input("Enter Department name: "))
Employee_code = (input("Enter Employee code/name: "))
Employee_name = (input("Enter Employee's name: "))
Salary_cutoff_date = (input("Enter Salary Cut-off Date: "))
Pay_period = (input("Enter Pay Period: "))

#input the rate per hour, number of hours, overtime hours, absent hours, and tardy hours per payday of the employee
Rate_per_hour = float(input("Enter Employee's rate per hour: "))
Hours_per_payday = float(input("Enter Employee's number of hours per payday: "))
Overtime_hours_per_payday = float(input("Enter Employee's overtime hours per payday: "))
Absent_hours_per_payday = float(input("Enter Employee's absent hours per payday: "))
Tardy_hours_per_payday = float(input("Enter Employee's tardy hours per payday: "))

#calculate the necessary
Basic_pay = Rate_per_hour * Hours_per_payday
Overtime = Overtime_hours_per_payday * Rate_per_hour
Absences = Absent_hours_per_payday * Rate_per_hour
Honorarium = Hours_per_payday * Rate_per_hour
Tardiness = Rate_per_hour * Tardy_hours_per_payday

#calculate the Philhealth contribution
Philhealth_contribution = Basic_pay * 0.05

#calculate the gross earnings
gross_earnings = Basic_pay + Overtime + Honorarium

#determine the SSS Contribution
def sss_contribution(gross_earnings):
    if gross_earnings < 4250:
        SSS_contribution = float(180)
    elif 4250 <= gross_earnings <= 4749.99:
        SSS_contribution = float(202.50)
    elif 4750 <= gross_earnings <= 5249.99:
        SSS_contribution = float(225)
    elif 5250 <= gross_earnings <= 5749.99:
        SSS_contribution = float(247.50)
    elif 5750 <= gross_earnings <= 6249.99:
        SSS_contribution = float(270)
    elif 6250 <= gross_earnings <= 6749.99:
        SSS_contribution = float(292.50)
    elif 6750 <= gross_earnings <= 7249.99:
        SSS_contribution = float(360)
    elif 8250 <= gross_earnings <= 8749.99:
        SSS_contribution = float(382)
    elif 8750 <= gross_earnings <= 9249.99:
        SSS_contribution = float(405)
    elif 9250 <= gross_earnings <= 9749.99:
        SSS_contribution = float(427)
    elif 9750 <= gross_earnings <= 10249.99:
        SSS_contribution = float(450)
    elif 10250 <= gross_earnings <= 10749.99:
        SSS_contribution = float(472)
    elif 10750 <= gross_earnings <= 11249.99:
        SSS_contribution = float(495)
    elif 11250 <= gross_earnings <= 11749.99:
        SSS_contribution = float(517)
    elif 11750 <= gross_earnings <= 12249.99:
        SSS_contribution = float(540)
    elif 12250 <= gross_earnings <= 12749.99:
        SSS_contribution = float(562)
    elif 12750 <= gross_earnings <= 13249.99:
        SSS_contribution = float(585)
    elif 13250 <= gross_earnings <= 13749.99:
        SSS_contribution = float(607)
    elif 13750 <= gross_earnings <= 14249.99:
        SSS_contribution = float(630)
    elif 14250 <= gross_earnings <= 14749.99:
        SSS_contribution = float(652)
    elif 14750 <= gross_earnings <= 15249.99:
        SSS_contribution = float(675)
    elif 15250 <= gross_earnings <= 15749.99:
        SSS_contribution = float(697)
    elif 15750 <= gross_earnings <= 16249.99:
        SSS_contribution = float(720)
    elif 16250 <= gross_earnings <= 16749.99:
        SSS_contribution = float(742.50)
    elif 16750 <= gross_earnings <= 17249.99:
        SSS_contribution = float(765)
    elif 17250 <= gross_earnings <= 17749.99:
        SSS_contribution = float(787)
    elif 17750 <= gross_earnings <= 18249.99:
        SSS_contribution = float(810)
    elif 18250 <= gross_earnings <= 18749.99:
        SSS_contribution = float(832)
    elif 18750 <= gross_earnings <= 19249.99:
        SSS_contribution = float(855)
    elif 19250 <= gross_earnings <= 19749.99:
        SSS_contribution = float(877)
    elif gross_earnings >= 19750:
        SSS_contribution = float(900)

#determine the daily tax for HDMF Contribution
def HDMF_contribution(gross_earnings):
    if 0 <= Basic_pay < 685:
        HDMF_contribution = 0
    elif 685 <= Basic_pay <= 1095:
        HDMF_contribution = 0 + 0.15/685
    elif 1096 <= Basic_pay <= 2191:
        HDMF_contribution = 61.65 + 0.20/1096
    elif 2192 <= Basic_pay <= 5478:
        HDMF_contribution = 280.85 + 0.25/2192
    elif 5479 <= Basic_pay <= 21917:
        HDMF_contribution = 1102.60 + 0.30/5479
    else:
        HDMF_contribution = 6034.30 + 0.35/21918

#calculate for deduction
Deductions = Absences + Tardiness + Withholding_tax + Philhealth_contribution

#calculate for net pay
Net_pay = Gross_earnings - Deductions

#display the following
print("Company name:", Company)
print("Department:", Department)
print("Employee's code:", Employee_code)
print("Employee's name:", Employee_name)
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
