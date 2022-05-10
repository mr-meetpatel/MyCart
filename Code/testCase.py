import Admin
import User

def test_case_1():

    # for admin
    assert Admin.Admin().add_category("Office") == "Category Added Successfully..."
    assert not Admin.Admin().view_cart(' ')== str
    assert not Admin.Admin().dis_category(' ')== str
    assert Admin.Admin().add_product(['Chair',"1","Conformable Chair","10000"]) == "Product Added Successfully..."

    # for user
    assert not User.UserCart().view_cart(' ')== str
    assert not User.User().dis_product(' ')== str
    assert not User.User().product_desc("1")==str
    assert User.UserCart().add_to_cart(["1","10"])=="Product Added to cart Successfully..."
    assert User.UserCart().remove_product_from_cart("1")=="Product Deleted from your cart..."


def test_case_2():

    # for admin
    assert Admin.Admin().add_category("Kitchen") == "Category Added Successfully..."
    assert not Admin.Admin().view_cart(' ')== str
    assert not Admin.Admin().dis_category(' ')== str
    assert Admin.Admin().add_product(['Knife',"2","Long Sharp Knife","100"]) == "Product Added Successfully..."

    # for user
    assert not User.UserCart().view_cart(' ')== str
    assert not User.User().dis_product(' ')== str
    assert not User.User().product_desc("1")==str
    assert User.UserCart().add_to_cart(["2","10"])=="Product Added to cart Successfully..."
    assert User.UserCart().remove_product_from_cart("2")=="Product Deleted from your cart..."

def test_case_3():
    '''
    Note: All testcase will fail because of in valid data
    '''
    # for admin
    assert Admin.Admin().add_category("1") == "Category Added Successfully..."
    assert not Admin.Admin().view_cart('')== str
    assert not Admin.Admin().dis_category('')== str
    assert Admin.Admin().add_product("") == "Product Added Successfully..."

    # for user
    assert not User.UserCart().view_cart(' ')== str
    assert not User.User().dis_product(' ')== str
    assert not User.User().product_desc("1a")==str
    assert User.UserCart().add_to_cart(["2a","10"])=="Product Added to cart Successfully..."
    assert User.UserCart().remove_product_from_cart("z")=="Product Deleted from your cart..."