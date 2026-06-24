from random import randint

class Train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(slf, fro, to):
        print(f"Tickets is booked in train no:{slf.trainNo} from {fro} to {to}")

    def getStatus(slf,):
        print(f"Tickets no:{slf.trainNo} is running on time")
        

    def getFare(slf, fro, to):
        print(f"Tickets fare in train no:{slf.trainNo} from {fro} to {to} is{randint(222, 5555)}")
        

t = Train(12314)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")