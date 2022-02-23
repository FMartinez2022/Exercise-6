string = "X-DSPAM-Confidence:    0.8475"

exval = string.find(':')
number = string[exval + 1:]
final = float(number)

print(final)
