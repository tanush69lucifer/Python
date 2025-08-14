def print_binary_burjkhalifa(h):
    for i in range(h):
        binary=bin(i)[2:]
        spaces=""*(h-len(binary))
        print(spaces+binary)
h=int(input())
print_binary_burjkhalifa(h)