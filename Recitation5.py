def intro_message(count):
    if count > 0:
        print("Iam a recursive function")
        intro_message(count-1)
    else:
        print('End of recursion')
def intro_message_iter():
    print('Iam a recursive function')
    intro_message_iter()
