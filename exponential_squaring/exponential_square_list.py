def WeightedValueOfList(OldUnweightedList: list):
    NewWeightedList=[]
    #For each value provided in the list of numbers
    for UnweightedValue in OldUnweightedList:
        UnweightedValueCountdown=UnweightedValue
        UnweightedValueRange=[]
        #Create a list out of a given number in the list all the numbers smaller than it.
        while UnweightedValueCountdown != 0:
            UnweightedValueRange.append(UnweightedValueCountdown)
            UnweightedValueCountdown-=1
        #Recreate said list with weighted values by taking each one and squaring them.
        WeightedValueRange=[]
        for GivenValue in UnweightedValueRange:
            WeightedGivenValue=GivenValue*GivenValue
            WeightedValueRange.append(WeightedGivenValue)
        WeightedValue=0
        #Take these new weighted values and add them together to create a new weighted value for the given number in the original list.
        for EachWeightedGivenValue in WeightedValueRange:
            WeightedValue+=EachWeightedGivenValue
        NewWeightedList.append(WeightedValue)
    #Add each weighted value together to create a total value for the list given.
    WeightedTotal=0
    for GivenWeightedValue in NewWeightedList:
        WeightedTotal+=GivenWeightedValue
    return (WeightedTotal)

