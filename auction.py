auction={}
more="yes"
while more=="yes":
    name=input("Whats's your name: ")
    bid=input("What's your bid: ")
    more=input("Any other bids? : ")

    auction[name]=bid



bids=[]
if more=='no':
    bids.append(auction[name])
winner=''
for key,value in auction.items():
    if value==max(bids):
        winner+=key
print (f'{winner} wins with bid of {max(bids)}')


