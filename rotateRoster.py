def rotateRoster(names, k):
    n = len(names)
    k = k % n  # Remove full turns[span_0](start_span)[span_0](end_span)
    # Each name at index i moves to index (i + k) % n[span_1](start_span)[span_1](end_span)
    return names[-k:] + names[:-k]
