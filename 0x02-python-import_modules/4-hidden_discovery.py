#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    ls = dir(hidden_4)
    for item in ls:
        if not item.startswith("__"):
            print("{}".format(item))
