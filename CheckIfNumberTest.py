x=0
while True:
    try:
        x=int(raw_input("ENeter a number"))
    except ValueError:
        print "please enter number"
    else:
        print "This is a number"
        break
