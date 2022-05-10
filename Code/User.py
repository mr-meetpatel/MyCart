'''

This File Manage the functionality of user

'''
# import db.py
import db
import Helper
# Manage User functionality to manage product
class User:
    # display product
    def dis_product(self,args):
        cat_id=args
        cursor=db.mydb.cursor(buffered=True)
        
        # executing query
        cursor.execute("select * from product_master where cat_id = %s",(cat_id,))
        # fetching total number of row
        if cursor.rowcount==0:
            return "No Data Found"
        # fetch all data
        prod_data=cursor.fetchall()
        # returning data
        return  prod_data
        
            

    # view product description
    def product_desc(self,args):
        prod_id=args
        cursor=db.mydb.cursor(buffered=True)
        cursor.execute("SELECT product_name,product_desc FROM product_master WHERE product_id=%s",(prod_id,))
        if cursor.rowcount==0:
            return "No Data Found"
        prod_data=cursor.fetchall()
        return  prod_data

# Manage User Cart functionality.
class UserCart:
    # add to cart
    def add_to_cart(self,args):
        
        cursor = db.mydb.cursor(buffered=True)
        # checking that product is available
        if not Helper.Controller().is_product_available(args[0]):
            return "this product id is not product list"
        # checking that product is already in cart or not if not than insert to db
        if not Helper.Controller().is_product_available(args[0],0):
            cursor.execute("INSERT INTO cart_master (product_id,product_quantity) VALUES (%s,%s)", (args[0],args[1]))
            db.mydb.commit()
            return "Product Added to cart Successfully..."
        else:
            # updating cart if product  is already available in cart
            self.update_cart(args[0],args[1])
            return f"Product Quantity is increase by {args[1]}"
           
        
    #view cart
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
        ON (`cart_master`.`product_id` = `product_master`.`product_id`) where `cart_master`.`bill_status`=%s;
            
            ''',(0,))
        if cursor.rowcount==0:
            return "Your Cart is Empty Now"

        cart_data=cursor.fetchall()

        return  cart_data
        

    # remove product from cart
    def remove_product_from_cart(self,args):
        cart_id=args
        cursor = db.mydb.cursor(buffered=True)
        
        if not Helper.Controller().is_product_available(int(cart_id),0):
            cursor.execute("DELETE FROM cart_master where cart_id=%s", (cart_id,))
            db.mydb.commit()
            return "Product Deleted from your cart..."
        else:
            return "no data found"
        
    # update cart
    def update_cart(self,*d):
        cursor = db.mydb.cursor(buffered=True)
        cursor.execute("SELECT cart_id,product_quantity from cart_master where product_id=%s and bill_status=%s", (d[0],0))
        # fetch data of above select query
        data=cursor.fetchall()
        # increment by previous product quantity by current passed product quantity
        cursor.execute("UPDATE cart_master SET product_quantity=%s WHERE cart_id=%s",(int(data[0][1])+int(d[1]),data[0][0]))
        db.mydb.commit()
    



    
        


















