def secondHighest(scores):
    highest = -1
    second = -1
    
    for score in scores:
        if score > highest:
            second = highest
            highest = score
        elif score > second and score < highest:
            second = score
            
    return second if second != -1 else -1
