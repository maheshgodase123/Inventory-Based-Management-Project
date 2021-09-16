import json
import datetime
with open('records.json') as f:
    data = json.load(f)

Product_No = ''
No_Stoks = ''


def status():
    for i in data:
        if data[i]['quantity'] == 0:
            with open('records.json', 'w') as f:
                data[i]['status'] = 'In-Active'
                json.dump(data, f)
        elif data[i]['quantity'] >= 0:
            with open('records.json', 'w') as f:
                data[i]['status'] = 'Active'
                json.dump(data, f)


status()

try:
    def products():
        categories = []
        for i in data:
            categories.append(data[i]['category'])
        print(set(categories))


    def purchase():
        bill = 0
        ans1 = input("Do You Want To Buy Products?Enter y for yes and n for no:- ")
        while ans1 != 'n' and ans1 == 'y':
            products()
            user = input("Enter The Category Of The Product Same As Mention Above You Want:- ")
            global Product_No, No_Stoks, total_bill
            for i in data:
                if data[i]['category'] == user:
                    print(i, data[i])
            Product_id = input("\nEnter The Product Id You Want:- ")
            Product_No = Product_id
            print(" The Product Is:- ", data[Product_id])
            Quantity = int(input("Enter The Quantity Of Product You Want:- "))
            No_Stoks = Quantity
            if data[Product_id]['quantity'] >= Quantity:
                bill = bill + data[Product_id]['price'] * Quantity
                total_bill = bill
                print("Confirming Your Order!!!!")

            else:
                print("No Enough Stocks Available!!\nAvailable Stocks Are:- ", data[Product_id]['quantity'])
                print("Try Again:-)")
            ans1 = input("Do You Want To Buy Products?Enter y for yes and n for no:- ")
        menu()


    def Bill():
        if data[Product_No]['quantity'] >= No_Stoks:
            with open('records.json', 'w') as f:
                data[Product_No]['quantity'] = (data[Product_No]['quantity'] - No_Stoks)
                json.dump(data, f)
            print("Your Total Billing Amount Is- ", total_bill, "Rs")
            with open('Sales.txt', 'a') as f:
                Name = input("Enter Your Name:- ")
                f.write("{}, {}, {}, {}\n".format(str(datetime.datetime.now()), Name, "Has Been Sale Of Total:-",
                                                  total_bill))
                print("Tanks For Shopping With Us!!Have A Good Dat:<) ")
        else:
            print("You Haven't Made A Sell Yet!!! ")

        menu()


    def check_for_stocks():
        print("************* Out Of Stock Products *************")
        for i in data:
            if data[i]['status'] == 'In-Active':
                print(i, data[i])
        ans = input("Do You Want To Import The Non-Available Product From Warehouse.Enter y for yes and n for no:- ")
        while ans != 'n' and ans == 'y':
            Product_id = input("\nEnter The Product Id You Want:- ")
            print(" The Product Is:- ", data[Product_id])
            Quantity = int(input("Enter The Quantity Of Product You Want:- "))
            with open('records.json', 'w') as f:
                data[Product_id]['quantity'] = (data[Product_id]['quantity'] + Quantity)
                json.dump(data, f)
            ans = input("Do You Want To Import The Non-Available Product From Warehouse.Enter y/n:- ")

        menu()


    def total_sale():
        print("Sales Til Now:- ")
        with open('Sales.txt') as f:
            last_sales = f.readlines()
            for i in range(len(last_sales) - 1, -1, -1):
                print(last_sales[i])
        menu()


    def total_earning():
        print("Total Earning From Your Branch :- ")
        earning = []
        total = []
        sum = 0
        with open('Sales.txt') as f:
            last_sales = f.readlines()
            for i in last_sales:
                earning.append(i.split(','))
        for i in range(len(earning)):
            total.append(earning[i][3].strip('/n'))
        for j in total:
            no = int(j.strip('\n'))
            sum = sum + no

        print("You Have Sell Products Of Amount:- ", sum, "Rs")
        menu()


    def menu():
        print(
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n0.Exit\n1.Purchase The Product\n2.Total Bill\n3.Check In-Active Stocks\n4.Check Total Sales By Customers\n5.Total Earning From Branch\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        choice = int(input("Enter The No Of Choice You Want:- "))
        while True:
            if choice == 0:
                exit()
            elif choice == 1:
                purchase()
            elif choice == 2:
                Bill()
            elif choice == 3:
                check_for_stocks()
            elif choice == 4:
                total_sale()
            elif choice == 5:
                total_earning()
            else:
                print("Enter The Correct Choice!!!")


    menu()


except Exception as e:
    print("Try Again!!")
