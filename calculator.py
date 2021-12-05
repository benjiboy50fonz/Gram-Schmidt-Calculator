from vector import Vector

def calculate(vectors: list):
    """
    Calculate the othogonal basis.

    :param vectors: a list of vector objects
    """
    
    # Setup the variables.
    newValue = []
    subtract = Vector([0] * len(vectors[0]))
    
    # Make Vector objects from the vectors given.
    for vector in range(len(vectors)):
        vectors[vector] = Vector(vectors[vector])
        
    # Check to see if they are already orthogonal.
    for i in range(len(vectors)-1):
        if not Vector.isOrthogonal(vectors[i], vectors[i+1]):
            break                   # We found a pair of non-orthogonal vectors. Carry on.
        if i == len(vectors)-2:     # If all are orthogonal, return because no work needs to be done.
            return False
        
    # Perform the algorithm.
    for i in range(len(vectors)):
        newValue.append(vectors[i] + subtract)
        try:                        # Subtract until you cannot any more. Then, we are done.
            subtract -= (vectors[i+1].dotProduct(newValue[i]) / newValue[i].dotProduct(newValue[i])) * newValue[i]
        except(IndexError):
            break
        
    # Return the result.
    return [x.value for x in newValue]