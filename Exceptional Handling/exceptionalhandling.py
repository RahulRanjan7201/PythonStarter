for i in range(5):
    try:
        print(i / 0)
    except ZeroDivisionError as e:
        print(e, "--> Division by 0 is not allowed")
    except NameError:
        print("Name error detected!")
    except ValueError:
        print("Wrong Value !")
    finally :
        print("Finally Block execution")
