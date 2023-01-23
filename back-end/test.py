import pandas as pd
import pandasql as ps

department = pd.read_csv("data/multiple_file_test/Department.csv")
employee = pd.read_csv("data/multiple_file_test/Employee.csv")
salary_payments = pd.read_csv("data/multiple_file_test/Salary_Payments.csv")



result = ps.sqldf("SELECT d.name, e.name FROM department d JOIN employee e ON d.id = e.department_id GROUP BY d.name, e.name HAVING COUNT(e.name) > 4")
# SELECT Store_ID, Daily_Customer_Count, Area FROM sales, store_area WHERE sales.Store_ID = Area.Store_ID
print (result)
