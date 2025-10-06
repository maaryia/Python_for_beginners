from collections import OrderedDict

def counting_votes():
    while True:
        try:
            num = int(input("Please enter the number: "))
            votes = OrderedDict()

            for i in range(num):
                names = input("Enter the name: ")
                if names in votes:
                    votes[names] += 1
                else:
                    votes[names] = 1
            for names, count in sorted(votes.items()):
                print(names, count)

            choice = input("Do you want to continue counting votes? (y/n): ")
            if choice.lower() != 'y':
                break

        except ValueError:
            print("Invalid input")

counting_votes()

