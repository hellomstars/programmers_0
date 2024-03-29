#어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.
#제한 조건
#공백은 아무리 밀어도 공백입니다.
#s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
#s의 길이는 8000이하입니다.
#n은 1 이상, 25이하인 자연수입니다.
def solution(s, n):
    answer = ''
    s = list(s)
    for i in s:
        if i == " ":
            answer += " "
        elif i == 'z' or i == 'Z':
            answer += chr(ord(i)-26+n)
        else :
            if i.isupper():
                if ord(i)+n > 90 :
                    answer += chr(ord(i)+n-26)
                else :
                    answer += chr(ord(i)+n)
            else : 
                if ord(i)+n > 122 :
                    answer += chr(ord(i)+n-26)
                else :
                    answer += chr(ord(i)+n)
    return answer

'''
다른 사람들은?

def solution(s, n):
    low = "abcdefghijklmnopqrstuvwxyz" # 소문자. 인덱스는 0에서 25
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = ''
    for char in s:
        if char in low:
            ind = low.find(char)+n # low 문자열에서 찾은 해당 알파벳 인덱스 + n
            answer += low[ind%26] # 26으로 나눈 나머지를 사용할 경우 25를 초과하는 경우도 활용 가능
        elif char in up:
            ind = up.find(char)+n
            answer += up[ind%26]
        else: # 공백일 경우도 고려
            answer += " "
    return answer

def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))
 
    return "".join(s)

def solution(s, n):
    u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    l = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for c in s:
        if c.isupper():
            result += u[(u.find(c)+n)%26]
        elif c.islower():
            result += l[(l.find(c)+n)%26]
        else:
            result += ' '
    return result
'''