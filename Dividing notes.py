amount=int(input('please enter how much dollars you want to take :'))
note_1=amount//100
note_2=(amount%100)//50
note_3=((amount%100)%50)//10
print('Notes of 100 dollars',note_1,)
print('Notes of 50 dollars',note_2,)
print('Notes of 10 dollars',note_3,)