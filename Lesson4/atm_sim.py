# The Smart ATM Withdrawal Simulator
print("\n~~ The Smart ATM Withdrawal Simulator ~~\n")

bank_balance = 500

withdraw_cash = float(input("How much money do you want to withdraw: "))

if withdraw_cash <= 0:
    print(" “Invalid amount”. You must withdraw more than “R0”.")
elif withdraw_cash <= bank_balance:
    print(f"“Withdrawal successful! Remaining balance: R{bank_balance - withdraw_cash}”.")
else:
    print("“Declined. Insufficient funds”")