from password_generator import PasswordGenerator


def gera():

    pwo = PasswordGenerator()

    pwo.minlen = 30 # (Optional)
    pwo.maxlen = 30 # (Optional)
    pwo.minuchars = 2 # (Optional)
    pwo.minlchars = 3 # (Optional)
    pwo.minnumbers = 1 # (Optional)
    pwo.minschars = 1 # (Optional)

    return pwo.generate()


if __name__ == "__main__":
    gera()