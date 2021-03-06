# DanEllisThesis
Understanding Atmospheric Chemistry using graph-theory, visualisation and machine learning.

### How to generate PDF
`python compile.py thesis.tex && open thesis.pdf`



### Documentation of python files
- `clean.py` :  removes aux files
- `git.py` :  pushes an update to git with message as argument
- `reference_check.py` :  locates missing citations from bibtex
- `compile.py` :  compiles the pdf
- `glossary.py` : 	generates the glossary
- `titleify.py` :  replaces each title with title case
- `flatten.py` :
- `makeindex.py` :  creates the index (NLP chapter keyword summary)
- `getbib.py` : 	generates a combigned and checked `bibligoraphy.bib` file
- `mini.py` :
- `./findline`: runs a grep command on the arguments
- `warning.txt` : output of compile containing things that need fixing
- `diff.py`: gets the diff for files between both branches using gitdiff. This is then parsed, filtered and converted to markdown. Eventually the markdown becomes a .pdf within the diff directory. 