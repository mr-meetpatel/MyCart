'''

This File Manage all Custom Command required to run this system.

'''

# to take argument for command line
import argparse
parser = argparse.ArgumentParser()
# Creating Custom Command

#add category by admin
parser.add_argument('--adminaddcategory',
                    type=str,
                    help='enter category name'
                    )

#view category by admin
parser.add_argument('--adminviewcategory',
                    type=str,
                    help='enter any string'
                    )

#add product by admin
parser.add_argument('--adminaddproduct',
                    type=str,
                    nargs=4,
                    help='parameter 1 : Name of product,2: Category id,3: Product Description,4:Product Price'
                    )

#view cart and bill of user by admin
parser.add_argument('--adminviewcartandbill',
                    type=str,

                    help='enter any string'
                    )

#view category by user
parser.add_argument('--userviewcategory',
                    type=str,
                    help='enter any string'
                    )
#view product by user
parser.add_argument('--userviewproduct',
                    type=str,
                    help='enter valid category id'
                    )

#view product description by user
parser.add_argument('--userproductdesc',
                    type=str,
                    help='enter valid product id'
                    )

#add product to cart by user
parser.add_argument('--useraddtocart',
                    type=str,
                    nargs=2,
                    help='parameter 1 :Product Id,2:Product Quantity'
                    )

#view cart and bill by user
parser.add_argument('--userviewcartandbill',
                    type=str,

                    help='enter any string'
                    )
#remove product from cart by user
parser.add_argument('--userremovecartproduct',
                    type=str,

                    help='enter valid cart_id'
                    )
