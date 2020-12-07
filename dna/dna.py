import csv
import sys  # use sys.argv[2] for ex


def main():

    # python dna.py databases/large.csv sequences/5.txt
    f = open(sys.argv[2], "r")
    sequence = f.read()  # getting the sequence into a string to deal with
    seq_length = len(sequence)

    # Opening database file
    with open(sys.argv[1], "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        row1 = next(csv_reader)  # getting row 1 that has STR kinds required
        STR = []
        i = 1
        STR_NUM = (len(row1) - 1)
        # Adding str kinds
        while i <= STR_NUM:
            STR.append(row1[i])
            i += 1
        STR_VALUES = []  # Creating A max holder for corresponding str in STR
        for i in range(STR_NUM):
            STR_VALUES.append(0)
        # iterate over each str
        # iterate over sequence
        for i in range(STR_NUM):
            tmplist = []
            count = 0
            flag = False
            STR_LENGTH = len(STR[i])  # STR Character length
            j = 0
            while j < seq_length:
                if STR[i] == sequence[j:j + STR_LENGTH]:
                    count += 1
                    tmplist.append(count)
                    flag = True
                    j += STR_LENGTH - 1
                else:
                    count = 0
                j += 1
            if flag == True:
                STR_VALUES[i] = max(tmplist)
            tmplist.clear()

        success = 0  # flag for success detection
        for line in csv_reader:  # for each person in the database
            i = 1
            tmplist = []
            while i <= STR_NUM:
                tmplist.append(int(line[i]))
                success += 1
                i += 1
            if tmplist == STR_VALUES:
                print(line[0])
                exit(0)
                tmplist.clear()
        if not (success == STR_NUM):
            print("No match")

    # READ CSV FILE ..
    # FROM FIRST ROW, RECORD SEQUENCES REQUIRED ..
    # FOR EACH SEQUENCE, GO TO SEQUENCES FILE AND GET ITS MAXIMUM NUMBER
    # ARRANGE THESE SEQUENCES IN A LIST IN ORDER TO ENCAPSULATE THEM FOR A PERSON
    # TAKING THIS CAPSULE SEARCH FOR IT IN DNA DATABASE
    # IF FOUND, GET THE NAME OF THE PERSON DETECTED AND END PROGRAM
    # IF NOT FOUND, PRINT THAT AND END PROGRAM


main()