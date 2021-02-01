#class Flight:

    #def __init__(self, origin, destination, duration):
   #     self.origin = origin
  #       self.duration = duration

#def main():
    # create flight.
    #f = Flight(origin="New york", destination="Paris", duration="600")

    # change the value of avariable.
    

    #print details about flight.
   # print(f.origin)
  #   print(f.duration)

#if __name__ == "__main__":
   # main()

class Flight:

    def __inti__ (self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(F"Flight duration: {self.duration}")

def main():

    f1 = Flight(origin="New York", destination="Paris", duration="540")
    f1.print_info()

    f2 = Flight(origin="Uganda", destination="kenya", duration="45")
    f2.print_info

    if __name__ == "__main__":
        main()
        