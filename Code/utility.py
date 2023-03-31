
def decorater(f):
    def wrapper():
        print("*******************")
        f()
        print("*******************")

    wrapper()

def clear_screen():
    print("*****************************")
    print("\n\n\n")





