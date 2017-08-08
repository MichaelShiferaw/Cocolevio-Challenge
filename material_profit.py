##Author: Michael Shiferaw
##Date: 8/5/2017 - 8/5/2017
##Program Description: Maximize Profits for Raw Material Provider
##Key Components: List competitive pricing. Allow users to update price/amount. Be user friendly. Return results quickly.

import company

def main():

    company_dictionary = read_and_store()
    
    ##display menu##
    
    print_menu()

    ##Grab user input and validate##
    
    menu_choice = get_menu_choice()

    while menu_choice != 3:

        ##logic to update a prospective companies asking price

        if menu_choice == 1:
            
            select_company = input('''Which company would you like to update the price for?''')

            update_price = float(input('''What would you like to update the price to?'''))
        
            company_dictionary[select_company].set_asking_price(update_price)

            print("ACTION COMPLETE")

            print("=======================================================")

            print('')

            print_menu()

            menu_choice = get_menu_choice()

        ##logic to update a prospective companies asking amount

        elif menu_choice == 2:

            select_company = input('''Which company would you like to update the amount for?''')

            update_amount = float(input('''What would you like to update the amount to?'''))
        
            company_dictionary[select_company].set_desired_amount(update_amount)

            print("ACTION COMPLETE")

            print("=======================================================")

            print('')

            print_menu()

            menu_choice = get_menu_choice()
                        
    ##logic to build a dictionary for price ratios (key = company name, value = ratio)
    price_ratio_dict = build_ratio_dict(company_dictionary)

    sorted_ratio_list = build_ratio_list(price_ratio_dict)

    ##prompt user to enter in the amount of material x available for sale
    available_material = int(input('''How much material do you have available for sale?'''))

    total_profit = 0

    ##list contain who to purchase from
    purchase_from_list = []


    ##Begin logic for data processing
    while available_material != 0:

        ##use ratio list to avoid dictionary length edits during iterations
        for ratio in sorted_ratio_list:

            company_name = compare_ratio(company_dictionary, ratio)

            company_amount = int(company_dictionary[company_name].get_desired_amount())

            company_price = int(company_dictionary[company_name].get_asking_price())


            if available_material >= company_amount:

                available_material = available_material - company_amount

                current_profit = company_price

                purchase_from_list.append("Buy " + str(company_amount) + " from " + company_name)

            ##occurs only during last iteration
            else:

                purchase_from_list.append("Buy " + str(available_material) + " from " + company_name)
            
                current_profit = (company_price/company_amount) * available_material
            
                available_material = available_material - available_material

            total_profit = current_profit + total_profit

            sorted_ratio_list.remove(ratio)

    print(purchase_from_list)        

    print("Total Profit: $" + str(format(total_profit, '.2f')))

##search ratio dict for matching ratio and return the key
def compare_ratio(comp_dict, ratio_search):

    for item in comp_dict:

        compare_ratio = comp_dict[item].calc_value()

        if compare_ratio == ratio_search:

            company_letter = item

    return company_letter
        
##builds the list of ratios and sorts them greatest to least     
def build_ratio_list(ratio_info_dict):

    ratio_list = []

    for item in ratio_info_dict:

        ratio_list.append(ratio_info_dict[item])

    ratio_list.sort()

    ratio_list.reverse()

    return ratio_list
        
##grabs menu number choice from user, validates that its within range
def get_menu_choice():

    print('')

    menu_select = int(input("Please select a menu option number from the list above."))

    while menu_select <= 0 or menu_select > 3:

        menu_select = int(input(" Invalid Value: Please enter either 1, 2, or 3."))

    return menu_select

##displays menu
def print_menu():

    print('''1. Update a company's price.''')
    print('''2. Update a company's amount.''')
    print('''3. Begin data processing .''')
    
##read sample data file and create objects for each line. Store the data in a dictionary
def read_and_store():

    company_data_input = open('CompanyData.txt', 'r')

    company_dict = {}

    for line in company_data_input:

        seperated_info = line.split(':')

        company_name = seperated_info[0]

        quoted_amount = seperated_info[1]

        quoted_price = seperated_info[2]

        my_company_object = company.Company(company_name, quoted_price, quoted_amount)

        company_dict[company_name] = my_company_object

    return company_dict

##builds ratio dictionary containing the company name as the key    
def build_ratio_dict(info_dict):

    ratio_dict = {}

    for line in info_dict:

        price_ratio = info_dict[line].calc_value()

        ratio_dict[line] = price_ratio

    return ratio_dict

main()
