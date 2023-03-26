import requests
import json
import math


def main():
    
    pricelen = '.3f'
    cointograb = ''
    userinput = ''
    #a 0.5% fee = 0.005
    #a 0.35% fee = 0.0035
    fee = 0.0035
    
#commands     
    def setfee(fee='notgiven'):
        if fee == 'notgiven':
            fee = (input('format: 0.5% = \'0.5\', 0.035% = \'0.035\' etc.\n' + \
                              'Default is 0.035%\n' + \
                              'What is your maker fee? '))
            while fee.isalpha():
                fee = input('\'' + fee + '\' contains alphabetical characters. Please try again. ')
            validfee = fee
        else:
            if fee.isalpha():
                print('\'' + fee + '\' is not a valid option/entry for fee. \n' + \
                      'Make sure your entry does not contain any alphabetical characters.')
                return
            else:
                validfee = fee   
                     
        fee = float(validfee)
        properformat = fee * 0.01
        print('Fee set to', str(fee) + '%. (' + str(properformat) + ')')
        return(properformat)
        
        
    def breakevencalc(entry):
        entryfee = (entry * fee)
        exitfee = ((entry + entryfee) * fee)
        breakeven = entry + entryfee + exitfee
        #stunt = (entry + (entry * fee) + ((entry + entryfee) * fee))
        porl = 0
        
    #for break even point
        print('In order to break even, you must sell at $' + format(breakeven, '.2f'), 'or higher.')
        print('Entry     Entry Fee   Exit Fee   Break Even        Fee %    ')
        #for break even calculations
        print('$' + format(entry, '.2f'), ' -$' + format(entryfee, '.2f') + \
              '    -$' + format(exitfee, '.2f') + '     $' + format(breakeven, '.2f') + \
              '          ' + str(fee * 10)+'%' + '    \n')
        
    #for profits
        print('For profits, represented as P on the far right, you must sell at \'Sell Point\'')
        print('Entry     Entry Fee   Exit Fee   Sell Point   Fee %     P')
        for i in range(25, 225, 25):
            exitfeeprof = ((entry + entryfee + i) * fee)
            sellpoint = entry + entryfee + exitfeeprof + i
            #print('Entry     Entry Fee   Exit Fee   Sell Point   Fee %     P')
            print('$' + format(entry, '.2f'), ' -$' + format(entryfee, '.2f') + \
              '    -$' + format(exitfeeprof, '.2f') + '     $' + format(sellpoint, '.2f') + \
              '   ' + str(fee * 10)+'%' + '    ', i)

        
    def breakevenpt1_validate(entry='notgiven'):
                                                                                                 # IF       #we know this is prompt entry because entry's default value has NOT changed.
        ####################### Input validation for prompt entry
        if entry == 'notgiven':
            entry = input('What was your entry point?')                                                     #initial prompt
            while entry.isalpha():                                                                          #initial promps entry is tested for alphabetical characters.
                entry = input('\'' + entry + '\' contains alphabetical characters. Please try again. ')     #if test fails, second prompt is repeated until entry is valid
            validentry = float(entry)                                                                       ##once prompt entry is valid, it is saved as 'validentry'
        ###################### Input validation for manual/acute entry
        else:                                                                                    # ELSE     #we know this is manual/acute entry because entry's default value HAS changed
            if entry.isalpha():                                                                             #the manual entry is tested for alphabetical characters.
                print('\'' + entry + '\' is not a valid option/entry for breakeven.\n')                     #If it FAILS the validity test, a message is shown. 
                print('Make sure your entry does not contain alphabetical characters')                      ## and 'return' is used to stop the function from continuing. (and calling calc)
                return                                                                                      
            validentry = float(entry)                                                                       #If it PASSES the validity test, the function continues and
                                                                                                            ## calls calc with valid data
        #print(validentry, 'ONLY VALID ENTRIES HERE!')
        ######################### Call calc function with valid entry
        breakevencalc(validentry)
            
    
#change price length    
    def changepricelen(newpricelen='notgiven'):
        if newpricelen == 'notgiven':
            newpricelen = input('What would you like the new price length to be? ')
            while newpricelen.isalpha():
                newpricelen = input('\'' + newpricelen + '\' contains alphabetical characters. Please try again.')
            validnewpricelen = float(newpricelen)
        else:
            if newpricelen.isalpha():
                print('\'' + newpricelen + '\' is not a valid option/entry for pricelength.\n' + \
                      'Make sure your entry does not contain alphabetical characters')
                return
            validnewpricelen = newpricelen
        #After validation, formatting
        new_properformat = '.' + str(newpricelen) + 'f'
        print('Price Length set to', newpricelen, 'numbers after decimal point ' + \
              '(' + new_properformat + ')')
        print('                    EG: $' + \
              format(math.pi, new_properformat))
        #print('the final is', newpricelen)
        return(new_properformat)
        
    
#grab price of specified coin,
    def grabdata(coin):
    
        url = 'https://rest.coinapi.io/v1/exchangerate/'+str(coin)+'/USD'
        headers = {'X-CoinAPI-Key' : 'XXXXXXXXX'}								#Enter your API key
        response = requests.get(url, headers=headers)

        status = response.status_code
        #print(status)
        if status == 550:
            print('\'' + coin + '\' is not a valid coin.\n' + \
                  'future option - \'coinlist\'')
            return
        
            
        data = response.text
        #convert data to dictionary
        resp_dict = json.loads(data)
        time1 = resp_dict['time']
        base1 = resp_dict['asset_id_base']
        quote1 = resp_dict['asset_id_quote']
        rate1 = resp_dict['rate']

        datalist = [time1, base1, quote1, rate1]
        #print(datalist)
        time = datalist[0]
        coin = datalist[1]
        price = datalist[3]
    
        print('As of', str(time) + ',', str(coin), 'is worth', format(price, pricelen) + ' USD')
    
    
#specify what coin's info to grab, and call grabcoin() with that coin
    def whatcoin(cointograb='notgiven'):
        if cointograb == 'notgiven':
            cointograb = input("What coin's price would you like to grab? ")
        grabdata(cointograb.upper())
        
        
#check connection to API. 
    def connectioncheck():
        url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
        headers = {'X-CoinAPI-Key' : 'XXXXXXXXX'}								#Enter your API key
        response = requests.get(url, headers=headers)
        
        statuscode = response.status_code
        if statuscode >= 200 and statuscode <= 300:
            statusdesc = 'Successful response. Connected to CBP API'
    
        elif statuscode >= 400 and statuscode <= 500:
           statusdesc = 'Client Error. Not Connected to CBP API\n'
           
        
           if statuscode == 400:
               statusdesc += 'Bad Request -- Invalid request format'
           elif statuscode == 401:
               statusdesc += 'Unauthorized - Bad API Key'
           elif statuscode == 403:
               statusdesc += 'Forbidden -- You do not have access to the requested resource'
           elif statuscode == 404:
               statusdesc += 'Not Found'
           elif statuscode == 500:
               statusdesc += 'Internal Server Error -- We had a problem with our server' 

        statusall = str(str(statuscode) + ', ' + str(statusdesc))
        return(statusall)



#start program
    print('cryptowatch v3 text interface' \
    '\n\n-->   Welcome to Cryptowatch v3!' \
    '\n\nConnection Status:', connectioncheck())
    print('To exit, type: exit\nFor help, type: help, -h, or --help.\n')
    
#user's console
    while userinput != 'exit':
        userinput = input('> ')
        userinput = userinput.split()
        if userinput[0] == 'help': 
            print('\n    Welcome to the help menu\n\n' + \
                  'grabcoin     - Grabs current price of a specified coin\n' + \
                  '                 \'grabcoin <coin>\'\n' + \
                  '                 \'grabcoin\' for prompt \n' + \
                  'breakeven    - Profit stats and break even point for a given entry point\n' + \
                  '                 \'breakeven <entry point>\'\n'+\
                  '                 \'breakeven\' for prompt\n\n' + \
                  
                  '          Settings\n\n' + \
                  'pricelength  - Change specificity of price by # values after decimal point\n' + \
                  '               Default is 3\n' + \
                  '                 \'pricelength <length>\'\n' + \
                  '                 \'pricelength\' for prompt \n' + \
                  'setfee       - Set your fee percent\n' + \
                  '                 \'setfee <%>\'\n' + \
                  '                 \'setfee\' for prompt')
         
#grabcoin         
        elif userinput[0] == 'grabcoin':
            if len(userinput) > 1:
                requestedcoin = userinput[1] 
                whatcoin(requestedcoin) 
            else:
                whatcoin()
 
 
#breakeven
        elif userinput[0] == 'breakeven':
            if len(userinput) > 1:
                price = userinput[1]
                breakevenpt1_validate(price)
            else:
                breakevenpt1_validate()


#setfee
        elif userinput[0] == 'setfee':
            if len(userinput) > 1:
                requestedfee = userinput[1]
                fee = setfee(requestedfee)
            else:
                fee = setfee()


#pricelength     
        elif userinput[0] == 'pricelength':
            if len(userinput) > 1:
                requestedpricelen = userinput[1]
                pricelen = (changepricelen(requestedpricelen))
            else:
                pricelen = changepricelen()
                

#clear
        elif userinput[0] == 'clear':
            for i in range(0, 25):
                print('\n')
                
        
#exit
        elif userinput[0] == 'exit':
            userinput = userinput[0]
        
        
        else:
            print('Command \'' + userinput[0] + '\' unrecognized.\n' + \
                  'Type \'help\' for help.')






main()

####TO DO 

#eliminate connectioncheck, integrate it into grabcoin. (ANYTHING TO CHECK CONNECTION WITHOUT USE OF NEW FUNCTION)
#figure out how to check actual profit, when they input a x.xxxxx btc value

#UI/UX


#add 'command/option unrecognized' prompts with:
#                                        'command unrecognized' and 'option unrecognized'.
#                                        'option unrecognized' shows valid options for that
#                                         specific command.
#add connection error codes, explaining each.
##eg: error 429. Too many requests
#add unknown coin error. Possibly one that relays coins that start/end with the same letter as the unknown coin.
## OR, just relay a list of all coins
### OR, relay all coins that start with the same letter as the coin entered.


########SUCCESSFUL UPDATES
# Users can now enter values while calling the command. EG 'coingrab btc' instead of just 'coingrab'....'btc'                                                          UX            ****
## Achieved by using acute and prompt procedures in one central function

#'exit' and 'clear' now allow users to exit the program, or clear the screen.


#changed setfee format
#changed pricelength format
##Now includes example of length based decimals of pi!
