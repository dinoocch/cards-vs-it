begin = '''
\\documentclass[cards,frame]{flashcards}
\\usepackage[utf8]{inputenc}
\\cardfrontheadstyle[\\ttfamily]{left}
\\cardfrontfootstyle[\\small\\itshape]{left}
\\cardfrontstyle{headings}
\\newcommand\\black{{\\huge Black}\\par\\bigskip Cards\\\\ Against\\\\ IT\\par\\bigskip{\\huge Black}}
\\newcommand\\white{{\\huge White}\\par\\bigskip Cards\\\\ Against\\\\ IT\\par\\bigskip{\\huge White}}
\\begin{document}
\\cardfrontfoot{CVAdmin}
'''

def makeWhiteCard(text):
    return '''
    \\begin{flashcard}
    [1 $White$ ]
    {%s}
    \\white
    \\end{flashcard}
    ''' % text

def makeBlackCard(text):
    return '''
    \\begin{flashcard}
    [1 $Black$ ]
    {%s}
    \\black
    \\end{flashcard}
    ''' % text

end = '''
\\end{document}
'''
file = "" + begin
with open('black.txt') as f:
    for line in f:
	file = file + makeBlackCard(line.strip().replace('_', '\_'))

with open('white.txt') as f:
    for line in f:
	file = file + makeWhiteCard(line.strip().replace('_', '\_'))
file += end

print file
