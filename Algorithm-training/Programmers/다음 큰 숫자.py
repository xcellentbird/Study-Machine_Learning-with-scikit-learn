def solution(n):
    answer = 0
    bin_n = bin(n)[2:]
    
    if bin_n[:bin_n.count('1')] == '1' * bin_n.count('1'):
        return int('0b' +'10' + ''.join(sorted(bin_n[1:])), 2)
    else:
        for i in range(len(bin_n)-1,-1,-1):
            if bin_n[i] == '0' and i+1 < len(bin_n) and bin_n[i+1] == '1':
                list_n = list(bin_n)
                list_n[i+1], list_n[i] = list_n[i], list_n[i+1]
                return int('0b' + ''.join(list_n[:i+1] + sorted(list_n[i+1:])), 2)
    return answer
