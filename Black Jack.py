import random
suits = {"Heart","Spade","Diamond","Club"}
rank = {"Two","Three","Four","Five","Six","Seven","Eight","Nine","Jack","King","Queen","Ace"}
value = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Jack":10,"King":10,"Queen":10,"Ace":11}
class Chips():
    def __init__(self,balance):
        self.balance = balance
    def credit(self,amount):
        self.balance +=amount
        print(f"Available Balance:{self.balance}")
    def debit(self,amount):
        self.balance -=amount
        print(f"Available Balance:{self.balance}")
    def __str__(self):
        return (f"Balance : Rs{self.balance}")
class Card():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return (f'{self.suit} {self.rank}')     
class Deck():
    def __init__(self):
        self.deck = []
        for s in suits:
            for r in rank:
                self.deck.append(Card(s,r))
    def __str__(self):
        deckview = " "
        for i in self.deck:
            deckview += "\n"+i.__str__()
        return deckview
    def shuffle(self):
        random.shuffle(self.deck)
class Hand():
    def __init__(self,name):
        self.name = name
        self.cards = []
        self.values = 0
    def add_card(self,card):
        self.cards.append(card)
    def hand_value(self):
        self.values = 0
        for eachcard in self.cards:
            if (eachcard.rank == "Ace" and self.values > 10):
                self.values += 1
            else:
                self.values += value[eachcard.rank]
    def __str__(self):
        handview = ""
        for i in self.cards:
              handview += "\t"+i.__str__()
        return (f"Cards:{handview} \n\tValue:{self.values}")
def hit(participant):
    participant.add_card(mydeck.deck.pop(-1))
    participant.hand_value()
def show_some(participant):
        handview = ""
        handvalue = 0
        for i in range(0,len(participant.cards)-1):
            handview +="\t"+participant.cards[i].__str__()
            handvalue += value[participant.cards[i].rank]
        return (f"Dealer || Cards:{handview}\n\tValue{handvalue}")
def check_bust(participant):
    if (participant.values > 21):
        print(f"\n{participant.name} is busted")
        return True
def check_winner(participant1,participant2):
    d1 = 21-participant1.values
    d2 = 21-participant2.values
    if(participant1.values<=21 and participant2.values<=21):
        if (d1<=d2):
            print(f"{participant1.name} is winner")
            return True
        else:
            print(f"{participant2.name} is winner")
            return False
    elif(participant2.values>21):
        print(f"{participant1.name} is winner")
        return True
    else:
        print(f"{participant2.name} is winner")
        return False
def place_bet():
    dep = True
    bet = 0
    while(dep):
        choice = input("Y to deposit amount, B to proceed to bet, E to exit:\t")
        if(choice == "Y"):
            deposit = int(input("Enter deposit amount: "))
            player_accnt.credit(deposit)
        elif(choice == "B"):
            bet = int(input("Enter amount to bet: "))
            if(bet <= player_accnt.balance):
                player_accnt.debit(bet)
                dep = False
                return bet
            else:
                print("Transaction Declined: Insufficient balance.")
        else:
            dep = False
            return bet
play = "Y"
print("Welcome to Black Jack Game, made by Rudra")
amount = int(input("Enter amount to open account: "))
player_accnt = Chips(amount)
while(play=="Y"):
    choice = "H"
    dchoice = 1
    mydeck = Deck()
    mydeck.shuffle()
    player = Hand("Player 1")
    dealer = Hand("Computer")
    bet_ammount = place_bet()
    if (bet_ammount > 0):
        hit(player)
        hit(dealer)
        hit(player)
        hit(dealer)
        print(show_some(dealer))
        print("Player ||",player)
        while (choice == "H"):
            choice = input("Player, H to Hit or S to Stand: ")
            if (choice=="H"):
                hit(player)
                print("Player ||",player)
                if check_bust(player):
                    choice = "S"
                    dchoice = 0
            else:
                print("Dealer's turn")
        while (dchoice == 1):
            dchoice = random.randint(0,1)
            if (dchoice==1):
                hit(dealer)
                if check_bust(dealer):
                    dchoice=0
                    print("Dealer:",dealer)
                else:
                    print(show_some(dealer))
            else:
                print("Dealer:",dealer)
        if(check_winner(player,dealer)):
            player_accnt.credit(bet_ammount*2)
        play = input("Want to play again? Y:Yes, N:No\t")
    else:
        print("No Bet placed, exiting the game")
        break
print("Thank you for playing this game!\nHave a great day!")        