package weighting

func exponentialSquare(list []int) (int, error){
	var weightedList []int
	//For value in provided numbers list
	for _, num := range list{
		numRange := []int{}
		//Create a list of of the value and every number smaller than it.
		for c := num; c != 0; c--{
			numRange = append(numRange, c)
		}	
		//Recreate this list with squared values.
		numRangeSquared := []int{}
		for _, n := range numRange{
			nSquared := n * n
			numRangeSquared = append (numRangeSquared , nSquared) 
		}
		//Take the squared values and add them into a single "weighted value"
		weightedVal := 0
		for _, givenSquaredVal := range numRangeSquared{
			weightedVal += givenSquaredVal
		}
		weightedList = append(weightedList, weightedVal)
	} 
	returnedWeight := 0
	for _, eachWeightedVal := range weightedList{
		returnedWeight += eachWeightedVal
	}
	return returnedWeight, nil 
}

