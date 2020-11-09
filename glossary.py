

glossary =  '''
\\section*{List of Abbreviations}
\\addcontentsline{toc}{section}{\\protect\\numberline{}List of Abbreviations}%
'''

def parse(x):
    data = x.split('=')
    return  '\\textbf{%s} & %s\\\\'%(data[0],data[1])
    #'\\item [] \\textbf{%s} - %s'%(data[0],data[1])





# Atmos

datastr  ='''
HOx = OH + \\ce{HO2}
NOx = NO + NO2
NOy = $\\Sigma$ oxidized atmospheric odd-nitrogen species
NOz = NOy - NOx
pp\\{m,b,t\\}v = parts per \\{million, billion, trillion\\} by volume
PAN = PeroxyAcyl Nitrate
'''


atmos = '''
\\subsection*{Atmosphere}
 \\begin{center}
  \\begin{tabular}{ p{.18\\textwidth}p{.65\\textwidth} }
        %s
  \\end{tabular}
 \\end{center}
'''%'\n'.join(list(map(parse,sorted(datastr.split('\n')[1:-1]))))



# Modelling


datastr  ='''
ROPA = Rate of Production (and Loss) Analysis
TUV = Tropospheric, Ultraviolet and Visible Radiation Model
KPP = Kinetic Pre Processor
GEOSChem = Chemistry component of NASA's Goddard Earth Observing System
DSMACC = Dynamically Simple Model of Atmospheric Chemical Complexity
'''


modelling = '''
\\subsection*{Modelling}
 \\begin{center}
  \\begin{tabular}{ p{.18\\textwidth}p{.65\\textwidth} }
        %s
  \\end{tabular}
 \\end{center}
'''%'\n'.join(list(map(parse,sorted(datastr.split('\n')[1:-1]))))






# Mechanisms


datastr  ='''
SMILES = Simplified Molecular-Input Line-Entry System
IUPAC =  International Union of Pure and Applied Chemistry
INCHI = International Chemical Identifier (developed by IUPAC)
MACCS = Molecular ACCess System
MCM = Master Chemical Mechanism
CRI = Common Representative Intermediates
MQN = Molecular Quantum Number
SMARTS = SMILES arbitrary target specification
'''



mech = '''
\\subsection*{Artificial Intelligence}
 \\begin{center}
  \\begin{tabular}{ p{.18\\textwidth}p{.65\\textwidth} }
        %s
  \\end{tabular}
 \\end{center}
'''%'\n'.join(list(map(parse,sorted(datastr.split('\n')[1:-1]))))







# Machine Learning


datastr  ='''
DR = Dimensionality Reduction
AE = Auto Encoder
t-SNE = t-distributed Stochastic Neighbor Embedding
OPTICS = Ordering Points To Identify the Clustering Structure
DBSCAN = Density-Based Spatial Clustering of Applications with Noise
GNN = Graph Neural Network
GMM = Gaussian Mixture Model
ML = Machine Learning
PCA = Principle Component Analysis
'''


ml = '''
\\subsection*{Artificial Intelligence}
 \\begin{center}
  \\begin{tabular}{ p{.18\\textwidth}p{.65\\textwidth} }
        %s
  \\end{tabular}
 \\end{center}
'''%'\n'.join(list(map(parse,sorted(datastr.split('\n')[1:-1]))))


glossary+= atmos
glossary+= modelling
glossary+= mech
glossary+= ml

with open('glossary.tex','w') as f:
    f.write(glossary)
