<<<<<<< HEAD
# algorithm for a euclidean sequence
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
=======
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
>>>>>>> 22d48fc8a138a14d650ac88bb9e55ffd0f92aef9
