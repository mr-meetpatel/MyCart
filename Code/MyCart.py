'''

This File Manage all the Operation of user and admin.

'''

# import Admin.py
import Admin
# for printing table
from tabulate import tabulate
# import Argument
import Argument
# import User.py
import User
# import Validation
import Helper


if __name__ == '__main__':

    # fetch data from command line
    args = Argument.parser.parse_args()
    # object of Admin class
    admin=Admin.Admin()
    # object of User class
    user=User.User()
    # object of UserCart class from User.py
    cart=User.UserCart()
    # object of Validation class from Helper.py
    validation=Helper.Validation()
    if not User.db.is_connected():
        print("Something went wrong while connecting to database")
        exit()
    # Add Category
    if args.adminaddcategory is not None:
        if not validation.validate_name(args.adminaddcategory):
            print("Error Msg: Invalid Category Name")
            exit()
        print(admin.add_category(args.adminaddcategory))
        
    # Add Product
    elif args.adminaddproduct is not None:
        # assigning value to respective vairable.
        pname,cat_id,pdesc,pprice=args.adminaddproduct[0],args.adminaddproduct[1],args.adminaddproduct[2],args.adminaddproduct[3]
        # basic validation
        if (not validation.validate_number(cat_id,pprice)):
            print("Error Msg: Invalid category id or price")
            exit()
        elif(not validation.validate_length(pname,pdesc)):
            print("Error Msg: Invalid product name or pdesc ")
            exit()
        print(admin.add_product(args.adminaddproduct))
    
    # View Category for both admin and user
    elif args.adminviewcategory is not None or args.userviewcategory is not None:
        
        data=admin.dis_category(args.adminviewcategory)
        if type(data) is str:
            print(data)
        else:
            table_header=["Id","Category Name"]
            table_data=[]
            for x in data:
                table_data.append([x[0],x[1]])
            print(tabulate(table_data, headers=table_header, tablefmt="grid"))
    # view product
    elif args.userviewproduct is not None :

        # basic validation
        if (not validation.validate_number(args.userviewproduct)):
            print("Error Msg: Invalid category id")
            exit()

        if type(user.dis_product(args.userviewproduct)) is str:
            print(user.dis_product(args.userviewproduct))
        else:

            table_data=[]
            for x in user.dis_product(args.userviewproduct):
                table_data.append([x[0],x[2],x[4]])
            print(tabulate(table_data, headers=["Id","Product Name","Price"], tablefmt="grid"))
            
    # view product description
    elif args.userproductdesc is not None:
        prod_id=args.userproductdesc
        # basic validation
        if (not validation.validate_number(prod_id)):
            print("Error Msg: Invalid product id")
            exit()
        data=user.product_desc(args.userproductdesc)
        if type(data) is str:
            print(data)
        else:
            print(f"\n* Name : {data[0][0]} \n* Description :{data[0][1]}")
    # add to cart
    elif args.useraddtocart is not None:
        
        prod_id,prod_quantity=args.useraddtocart[0],args.useraddtocart[1]
        if (not validation.validate_number(prod_id,prod_quantity)):
            print("Error Msg: Invalid product id or product qunatity")
            exit()
        print(cart.add_to_cart(args.useraddtocart))
        
               
    # view cart , bill and do payment
    elif args.userviewcartandbill is not None:
        data =cart.view_cart(args.userviewcartandbill)
        if type(data) is str:
            print(data)
        else:
            bill=0



            table_data=[]
            for x in data:
                bill+=(x[2]*x[3])
                table_data.append([x[0],x[1],x[2],x[3],x[2]*x[3]])

            print(tabulate(table_data, headers=["Id","Product Name","Product Prince","Product Quantity","Total Price"], tablefmt="grid"))

            print(f"Your Actual Bill {bill}")
            if bill>=10000:
                print("Congrats you got  discount of rs 500")
                bill-=500

            print(f"\n\nYour Final Bill : {bill}")

            if input("Do you want to pay your bill?(y or Y to pay / other key to continue shopping)") in ['y','Y']:
                print("Your Order is placed successfully.Thank You!")

            else:
                print("No ProblemContinue your shopping...")



    # admin view cart and bill
    elif args.adminviewcartandbill is not None:
        data =admin.view_cart(args.adminviewcartandbill)
        if type(data) is str:
            print(data)
        else:
            bill=0




            table_data=[]
            for x in data:
                bill+=(x[2]*x[3])
                table_data.append([x[0],x[1],x[2],x[3],x[2]*x[3]])

            print(tabulate(table_data, headers=["Id","Product Name","Product Prince","Product Quantity","Total Price"], tablefmt="grid"))
            print(f"\n\nFinal Bill : {bill}")

    # remove product from cart
    elif args.userremovecartproduct is not None:
        cart_id=args.userremovecartproduct
        if (not validation.validate_number(cart_id)):
            print("Error Msg: Invalid cart id")
            exit()
        data =cart.remove_product_from_cart(args.userremovecartproduct)
        print(data)


























