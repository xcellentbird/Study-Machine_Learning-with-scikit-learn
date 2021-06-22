def solution(n, words):
    said = [words[0]]
    for i, word in zip(range(2,len(words)+1), words[1:]):
        if word in said or word[0] != said[-1][-1]:
            turn = (i-1)//n+1
            return [i - (turn - 1) * n, turn]
        said.append(word)
    return [0, 0]
