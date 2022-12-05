''' This is a program to check if a group of numbers are part of the Fibonacci series or not'''
class Fibonacci:
    def check_fibo(self):
        while True:
            #Checking if range of numbers are in Fibonacci series
            fibo=[]
            nums=list(map(int,input("Enter range of numbers: ").split(",")))
            n1=0
            n2=1
            s=0
            while s<=(max(nums)):
                fibo.append(n1)
                nth=n1+n2
                n1=n2
                n2=nth
                s=s+1
                if max(nums) in fibo:
                    break
            for j in nums:
                if j in fibo:
                    print(j,"is valid")
                else:
                    print(j,"is not valid ")
            # Asking the User if they want to continue or not
            reply=input("Dear User ! Do you want to run it again? Reply with Y or N : ")
            if reply=="Y" or reply=="y":
                print("Let's GO !!!")
                continue
            elif reply=="N" or reply=="n":
                print("Thanks for executing my program !")
                break
            else:
                print("Invalid input")
                print("Thanks for executing my program !")
                break
#Function Call
F=Fibonacci()
F.check_fibo()




