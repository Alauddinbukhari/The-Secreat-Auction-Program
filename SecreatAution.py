from os import system, name 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux
    else: 
        _ = system('clear') 
       
def highest_bidder(autions_nominee):
    highest_bid=0
    Highest_bidder=""
    for key in autions_nominee:
        if autions_nominee[key]>highest_bid:
            highest_bid=autions_nominee[key]
            Highest_bidder=key
  
    print(f"The Winner is {Highest_bidder} with a bid of ${highest_bid }  ")   



print( '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
                        ''')



                        
print("Welcome to the secret auction program.")
autions_nominee={}
bidding_finished=False
while not bidding_finished:
    name=input('What is your name?:')
    bid_amount=int(input('What is your bid?: $'))
    other_bidders=input('Are there any other bidders? Type "Yes" or "No".\n').lower()
    autions_nominee[name]=bid_amount
    if other_bidders=='yes':
        clear()
    elif other_bidders=='no':
        bidding_finished=True
        highest_bidder(autions_nominee=autions_nominee)
       



    