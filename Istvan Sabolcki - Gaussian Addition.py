def getRange():
    try:
        integerRange = list(range(1, int(input("\nNumber To Conduct Gaussian Addition Upon: ")) + 1))
    except ValueError:
        print("Error Accounting Response...")
        getRange()
    for integer in integerRange[0: int(len(integerRange) / 2)]:
        print("[" + str(integer) + "]", str(integer), "+", str(integerRange[len(integerRange) - integer]), "=", str(integer + integerRange[len(integerRange) - integer]))
    print("\n-------------------\nIteration Count:", int(len(integerRange) / 2), "\nFinal Answer:", int(len(integerRange) * (len(integerRange) + 1) / 2),"\n-------------------")
    response = input("\nGenerate New Calculation? [Y/N]\n")
    if (response.lower() == "y") or (response.lower() == "yes"):
        getRange()
    else:
        exit()

getRange()