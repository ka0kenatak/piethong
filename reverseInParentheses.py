def reverseInParentheses(s):
    def flip(seq, begin, end):
        return seq[:begin]+seq[begin+1:end][::-1]+seq[end+1:]
    p_index_stack = []
    i = 0
    while i < len(s):
        if s[i] == '(':
            p_index_stack.append(i)
        elif s[i] == ')':
            s = flip(s,p_index_stack.pop(),i)
            print("s=",s)
            i -= 2
        i += 1
    return s
