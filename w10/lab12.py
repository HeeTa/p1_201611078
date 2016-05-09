lyrics=["When I find myself in times of trouble",
"Mother Mary comes to me",
"Speaking words of wisdom let it be",
"And in my hour of darkness",
"She is standing right in front of me",
"Speaking words of wisdom let it be",
"Let it be let it be",
"Let it be let it be",
"Whisper words of wisdom let it be",
"And when the broken-hearted people",
"Living in the world agree",
"There will be an answer let it be",
"For though they may be parted",
"There is still a chance that they will see",
"There will be an answer let it be",
"Let it be let it be",
"Let it be let it be",
"Yeah there will be an answer let it be",
"Let it be let it be",
"Let it be let it be",
"Whisper words of wisdom let it be",
"Let it be let it be",
"Ah let it be yeah let it be",
"Whisper words of wisdom let it be",
"And when the night is cloudy",
"There is still a light that shines on me",
"Shine on until tomorrow let it be",
"I wake up to the sound of music",
"Mother Mary comes to me",
"Speaking words of wisdom let it be",
"Let it be let it be",
"Let it be yeah let it be",
"Oh there will be an answer let it be",
"Let it be let it be",
"Let it be yeah let it be",
"Whisper words of wisdom let it be"]
word=dict()
for i in lyrics:
    words=i.split()
    for l in words:
        if l not in word:
            word[l]=1
        else:
            word[l]=word[l]+1
print word
num=[0,0,0,0,0]
wordlist=["","","","",""]
for i in word:
    for number in range(0,5):
        if word[i]>num[number]:
            num[number]=word[i]
            wordlist[number]=i
            break
    print num[0],num[1],num[2],num[3],num[4]
    print wordlist[0],wordlist[1],wordlist[2],wordlist[3],wordlist[4]