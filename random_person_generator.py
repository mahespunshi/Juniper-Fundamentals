# # Generate 100 Random first, last name, email address, phone number.
#
# import string
# from random import choice
# from random import randint
#
# # list of first names
# first_names = ['Jon', 'Rick', 'Bill', 'Ben', 'Vishal']
#
# # list of last names
#
# last_names = ['Johnson', 'Andrews', 'Smith', 'Jones', 'Williams']
# for x in range(100):
#     #random_name = '{} {}'. format(choice(first_names), choice(last_names))
#     first, last = choice(first_names), choice(last_names)
#     random_name = f'{first} {last}'
#     print(random_name)
#
# # email address: I want a dot vishal.jones@gmail.com
# # valid email services: gmail, hotmail, yahoo, outlook, icloud
#
# email_services = ['gmail.com', 'hotmail.com', 'yahoo.com', 'outlook.com', 'icloud.com']
#
# # Random phone numbers.
#
# for x in range(100):
#     random_email_service = choice(email_services)
#     random_phone = f'{randint(0,9)}{randint(0,9)}{randint(0,9)}-{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}-{randint(0,9)}'\
#                    f'{randint(0,9)}{randint(0,9)}'
#     first, last = choice(first_names), choice(last_names)
#     print(f'{first}.{last}.{random_phone}', f'{first.lower()}.{last.lower()}@{random_email_service}')
#
#
#
# ###random phone number format
# #--------------------------------
# #978-356-6754
# # for i in range(100):
# #     print('-------------------------------------------------------')
# #     random_name='{} {}'.format(choice(first_names),choice(last_names))
# #     ''.format()
# #     print(random_name)
# #     random_email_service = choice(email_servics)
# #     print('Email address: {}@{}'.format(random_name, random_email_service))
# #     print('phone number:')
# #     random_phone_number1 = random.randint(101, 999)
# #     random_phone_number2 = random.randint(101, 999)
# #     random_phone_number3 = random.randint(1001, 9999)
# #     print('{}-{}-{}'.format(random_phone_number1,random_phone_number2,random_phone_number3))
#
#
#  # random_phone_number = '{}{}{}-{}{}{}-{}{}{}'.format(rand_digit,rand_digit,rand_digit,rand_digit,rand_digit,rand_digit,rand_digit,rand_digit,rand_digit)
#  #    print(random_mail_per_user," Phone number: ",random_phone_number)
#
#
# ## solution by instructor below:
# # every time you create module, program there is __name__ in builin and that is equal to main .. type .. print(dir())
#
#
# if __name__ == '__main__':
#     for x in range(100):

r = [1,2,3,4,5,6,7,8,9]
