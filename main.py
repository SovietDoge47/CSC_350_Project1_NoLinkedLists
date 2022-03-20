# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import time

class PCB:
    def __init__(self, parent, first_child, younger_sibling, older_sibling):
        self.parent = parent  # int
        self.first_child = first_child  # int
        self.younger_sibling = younger_sibling  # int
        self.older_sibling = older_sibling  # int


def getIndexGivenPCB(pcb, PCBList):
    for i in range(0, len(PCBList)):
        if PCBList[i] == pcb:
            return i
    raise Exception("PCB not found in PCBList!")


def traverse_younger_sibling(index, PCBList):
    if PCBList[index].younger_sibling is not None:
        return traverse_younger_sibling(PCBList[index].younger_sibling, PCBList)
    else:
        return index  # Returns the last PCB index in the chain of younger siblings


def create(index, PCBList):
    newProcessIndex = len(PCBList)

    # Parent, first child, and younger sibling always same
    parent = index
    first_child = None
    younger_sibling = None

    # Older Sibling can vary
    if PCBList[index].first_child is None:
        older_sibling = None
        # Appends our newly created PCB to the list
        PCBList.append(PCB(parent, first_child, younger_sibling, older_sibling))
    else:
        PCBIndexOfInterest = traverse_younger_sibling(PCBList[index].first_child, PCBList)  # Only enters if first_child isn't none
        older_sibling = PCBIndexOfInterest
        # Appends our newly created PCB to the list
        PCBList.append(PCB(parent, first_child, younger_sibling, older_sibling))
        # Adjusts younger sibling variable of our new PCBs older sibling
        PCBList[PCBIndexOfInterest].younger_sibling = getIndexGivenPCB(PCBList[newProcessIndex], PCBList)

    # Adjusts parent's first child if applicable
    if PCBList[index].first_child is None:
        PCBList[index].first_child = getIndexGivenPCB(PCBList[newProcessIndex], PCBList)


def destroy(index, PCBList):
    # Adjusts younger siblings
    if PCBList[index].younger_sibling is not None:
        if PCBList[index].older_sibling is not None:
            PCBList[PCBList[index].younger_sibling].older_sibling = PCBList[index].older_sibling
            PCBList[PCBList[index].older_sibling].younger_sibling = PCBList[index].younger_sibling
        else:
            PCBList[PCBList[index].younger_sibling].older_sibling = None
            PCBList[PCBList[index].parent].first_child = PCBList[index].younger_sibling

    # If the destroyed process has a child, call destroy on it
    if PCBList[index].first_child is not None:
        if PCBList[PCBList[index].first_child].younger_sibling is not None:
            destroy(PCBList[PCBList[index].first_child].younger_sibling, PCBList)
            destroy(PCBList[index].first_child, PCBList)
        else:
            destroy(PCBList[index].first_child, PCBList)

    # If the destroyed process has an older sibling, set the older siblings ys to None
    if PCBList[index].older_sibling is not None:
        PCBList[PCBList[index].older_sibling].younger_sibling = None

    # If the destroyed process is its parent's first child, set the parents fc to None
    if PCBList[index].parent is not None:
        if PCBList[PCBList[index].parent].first_child == index:
            PCBList[PCBList[index].parent].first_child = None

    PCBList[index].parent = None
    PCBList[index].first_child = None
    PCBList[index].younger_sibling = None
    PCBList[index].older_sibling = None


def printPCB(index, PCBList):
    print("PCB at index " + str(index) + ": ")
    print(PCBList[index].parent, PCBList[index].first_child, PCBList[index].younger_sibling, PCBList[index].older_sibling)
    print("")


def printAllPCB(PCBList):
    for i in range(0, len(PCBList)):
        if PCBList[i].parent is None:
            if PCBList[i].first_child is None:
                if PCBList[i].younger_sibling is None:
                    if PCBList[i].older_sibling is None:
                        pass
            else:
                printPCB(i, PCBList)
        else:
            printPCB(i, PCBList)


def main():
    start = time.time()
    PCBList = [PCB(None, None, None, None)]
    #create(0, PCBList)  # Creates first child node of PCB[0] at PCB[1]
    #create(0, PCBList)  # Creates second child node of PCB[0] at PCB[2]
    #create(0, PCBList)  # Creates third child node of PCB[0] at PCB[3]
    #create(2, PCBList)  # Creates third child node of PCB[2] at PCB[4]
    #create(2, PCBList)  # Creates third child node of PCB[2] at PCB[5]
    #create(5, PCBList)  # Creates third child node of PCB[5] at PCB[6]

    #printAllPCB(PCBList)
    #print("---------------------------")

    #destroy(2, PCBList)
    #printAllPCB(PCBList)

    for i in range(0, 10000):
        create(i, PCBList)
        create(i+1, PCBList)
        create(i+2, PCBList)
    for i in range(9999, 0, -1):
        destroy(i, PCBList)

    end = time.time()
    print(end - start)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
