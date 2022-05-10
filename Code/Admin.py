'''

This File Manage the functionality of admin

'''
# import db.py
import db
import Helper
# Manage admin functionality to manage product
class Admin:
    #add category
    def add_category(self,args):
        category=args
        # check that db is connected
        cursor = db.mydb.cursor(buffered=True)
        # checking  that user category is add to category_master
        if not Helper.Controller().is_cat_available(category):
            cursor.execute("INSERT INTO category_master (cat_name) VALUES (%s)", (category,))
            db.mydb.commit()
            return "Category Added Successfully..."
        else:
            return "This Category is Already Added..."

    # display category
    def dis_category(self,args):
        
        cursor=db.mydb.cursor(buffered=True)
        cursor.execute("SELECT * from category_master")
        cat_data=cursor.fetchall()
        if cursor.rowcount==0:
            return "No Data Found"
        return  cat_data


    # add product
    def add_product(self,args):

        cursor = db.mydb.cursor(buffered=True)
        # checking  that cat id not register
        if not Helper.Controller().is_cat_available(int(args[1])):
            return "please enter valid category id"
        # checking  that product name id not register
        cursor.execute("SELECT product_name from product_master where product_name=%s", (args[0],))
        if cursor.rowcount == 0:
 
            cursor.execute("INSERT INTO product_master (cat_id,product_name,product_desc,product_price) VALUES (%s,%s,%s,%s)", (args[1],args[0],args[2],args[3]))
            db.mydb.commit()

            return "Product Added Successfully..."
        else:
            return "This Product is Already Added..."
        
    # view cart
    def view_cart(self,args):

        cursor=db.mydb.cursor(buffered=True)


        cursor.execute('''
            SELECT
    `cart_master`.`cart_id`
    , `product_master`.`product_name`
    , `product_master`.`product_price`
    , `cart_master`.`product_quantity`
    , `cart_master`.`bill_status`
FROM
    `mycart`.`cart_master`
    INNER JOIN `mycart`.`product_master` 
        ON (`cart_master`.`product_id` = `product_master`.`product_id`);
            
            ''')

        if cursor.rowcount==0:
            return "Cart is Empty Now"

        cart_data=cursor.fetchall()

        return cart_data







