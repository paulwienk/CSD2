






def euclidean_rhythm(beats, pulses):
    if pulses is None or pulses < 0:
        pulses = 0
    if beats is None or beats < 0:
        beats = 0
    if pulses > beats:
        beats, pulses = pulses, beats
    if beats == 0:
        return []

    rests = beats - pulses
    result = [1] * pulses
    pivot = 1
    interval = 2

    while rests > 0:
        if pivot > len(result):
            pivot = 1
            interval += 1

        result.insert(pivot, 0)

        pivot += interval
        rests -= 1

    return result

print(euclidean_rhythm(6, 5))






