# algorithm for a euclidean sequence by Kountanis, https://kountanis.com/2017/06/13/python-euclidean/
def euclidean_rhythm(beats, pulses):
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
