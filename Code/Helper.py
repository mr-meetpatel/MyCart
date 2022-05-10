from multipledispatch import dispatch
import db
class Validation:
    # To validate that string is not null
    def validate_length(self,*name):
        for name in name:
            if len(name.strip())==0:
                return False
        return True
    # To Validate that number is not null,numeric,greater than zero
    def validate_number(self,*id):
        for id in id:
            id=str(id)
            if (not self.validate_length(id)) or (not id.isnumeric()) or (not int(id)>0):
                return False
        return True
        
    # To validate category name
    def validate_name(self,name):
        if (not self.validate_length(name)) or name.isnumeric():
            return False
        return True



class Controller:
    '''
        Method Overloading
    '''
    cursor = db.mydb.cursor(buffered=True)
    @dispatch(int)
    def is_cat_available(self,cat_id):
        self.cursor.execute("SELECT cat_id from category_master where cat_id=%s",(cat_id,))
        if self.cursor.rowcount==0:
            return False
        return True

    @dispatch(str)
    def is_cat_available(self,cat_name):
        self.cursor.execute("SELECT cat_name from category_master where cat_name=%s", (cat_name,))
        if self.cursor.rowcount==0:
            return False
        return True
    # checking product is available in product_master
    @dispatch(str)
    def is_product_available(self,prod_id):

        self.cursor.execute("SELECT product_id from product_master where product_id=%s",(prod_id,))
        if self.cursor.rowcount==0:
            return False
        return True
    # checking product is available in cart
    @dispatch(str,int)
    def is_product_available(self,prod_id,status):

        self.cursor.execute("SELECT cart_id,product_quantity from cart_master where product_id=%s and bill_status=%s", (prod_id,status))
        if self.cursor.rowcount==0:
            return False
        return True

    @dispatch(int,int)
    def is_product_available(self,cart_id,status):

        self.cursor.execute("SELECT cart_id from cart_master where cart_id=%s and bill_status=%s", (cart_id,status))
        if self.cursor.rowcount==0:
            return True
        return False



