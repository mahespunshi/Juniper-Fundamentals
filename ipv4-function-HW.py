# Write a function called create_ip_address_4()
# Has default parameters of a='172', b='16', c='254', d='1'
#  'a' must be exactly length of 3 and contains ONLY strings of digits
# 'b' must be exactly length 2 and contains ONLY strings of digits
# 'c' must be exactly length 3 and contains ONLY strings of digits
# 'd' must be exactly length 1 and contains ONLY strings of digits
# If any of the following conditions are invalid then a ValueError() exception will be raised.
# Research how to raise a ValueError

def create_ip_address_4(a ='172', b='17', c='254', d='1'):
    try:
        if len(a) == 3 and isinstance(a, str) and a.isdigit() \
            and len(b) == 2 and b.isdigit() and isinstance(b, str) \
            and len(c) == 3 and c.isdigit() and isinstance(c, str) \
            and len(d) == 1 and d.isdigit() and isinstance(d, str):
            return (f'{a}.{b}.{c}.{d}')
        else:
            raise ValueError("This is wrong input")


    except ValueError as err:
        print(err.with_traceback())
        return (err)


# Example valid input/output:
# print(create_ip_address_4())
# print(create_ip_address_4(a='263'))
# print(create_ip_address_4(b='21'))
# print(create_ip_address_4(b='21', a='872'))
# print(create_ip_address_4(a='872', b='21', c='876', d='8'))

# Example invalid input/output:
# print(create_ip_address_4(a='hello'))
# print(create_ip_address_4(a='65'))
# print(create_ip_address_4(a='722', b='ku'))
# print(create_ip_address_4(a='179', b='76', c='9817'))
# print(create_ip_address_4(a='262', b='12', c='123', d='bu'))



#
# create_ip_address_4('172','17','234','1')

