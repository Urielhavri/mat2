def reword(word:str) ->str:
    st=''.rstrip()
    for letter in range(0,len(word)):
        st=word[letter]+st
    return st.lower()

def countword() ->int:
    file=open('text.txt')
    text=file.read()
    word_list=text.split()
    word=word_list[0]
    count=0
    for i in range(1,len(word_list)):
        fname=reword(word_list[i])
        if fname==word:
            count=count+1
    return count+1

        