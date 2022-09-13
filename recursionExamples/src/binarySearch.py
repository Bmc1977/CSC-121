def binarySearch(needle, haystack, left=None, right=None):
    #  `left` and `right` are indexes of `haystack`
    # `left` defaults to the 0 index.
    # `right` defaults to the last index.
    if left is None:
        left = 0
    if right is None:
        right = len(haystack) - 1

    print('Searching:', left, right+1)

    if left > right:  # BASE CASE where `needle` is not in `haystack`.
        return None

    mid = (left + right) // 2
    if needle == haystack[mid]:  # BASE CASE where `needle` has been found in `haystack`
        return mid

    # RECURSIVE CASES
    elif needle < haystack[mid]:
        return binarySearch(needle, haystack, left, mid - 1)
    elif needle > haystack[mid]:
        return binarySearch(needle, haystack, mid + 1, right)

print(binarySearch(13, [1, 4, 8, 11, 13, 16, 19, 19]))

def main():
    dictionary = open("../large.txt")
    words = dictionary.readlines()
    words = [x[:-1] for x in words]     # remove the newline character at the end
    print(len(words))
    print(binarySearch("hippopotamus", words))

if __name__ == '__main__':
    main()