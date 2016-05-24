pywiki=open("pywiki.txt",'w')
imfor="Python is a widely used high-level, general-purpose, interpreted, dynamic programming language.[23][24] Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C++ or Java.[25][26] The language provides constructs intended to enable clear programs on both a small and large scale.[27]Python supports multiple programming paradigms, including object-oriented, imperative and functional programming or procedural styles. It features a dynamic type system and automatic memory management and has a large and comprehensive standard library."
pywiki.write(imfor)

pywiki=open("pywiki.txt",'r')
lines=pywiki.readlines()
for line in lines:
    uline=line.lower()
    if uline.count("python")>0:
        print line
 
