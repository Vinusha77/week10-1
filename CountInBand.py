import bisect

def countInBand(scores, low, high):
    # Find the first position with a score >= low
    left_index = bisect.bisect_left(scores, low)
    # Find the first position with a score > high
    right_index = bisect.bisect_right(scores, high)
    
    return right_index - left_index
