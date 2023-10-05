#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    print("{} argument{}".format(argc - 1, "s" if argc != 2 else ""), end="")
    print("{}".format(":" if argc > 1 else "."))
    for i in range(1, argc):
        print("{}: {}".format(i, sys.argv[i]))
