def test(string):
    answer = ''
    string += 'p'
    left, right = 0, 1
    while right != len(string):
        if string[right].isdigit():
            right += 1
        else:
            char = string[left:left+1]
            value = int(string[left+1:right])
            answer += char*value
            left = right
            right += 1
    return answer

print(test('a11b2f3'))

