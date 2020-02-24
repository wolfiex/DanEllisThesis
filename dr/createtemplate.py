import sys
for what in 'pca,spca,tsne,umap,vae,gae'.split(','):

    s = r'''\subsection{'''+what+'''}

    \\qfig{4fig/DROTHER/'''+what+'''.png}{fig:'''+what+'''}{Distribution of the $x,y$ components for each input group using '''+what+'''. }{.9\\textwidth}




    '''

    t = "vec_spec,vec_smiles,embed_fn_,finger_mqn,finger_maccs,embed_graph".split(",");
    n = "Species Names,SMILES strings,Function Categories,MQN Fingerprints,MACCS Fingerprints,Molecule Graph".split(",");

    d = dict(zip(t,n))


    for inp in t:
        tab = inp+'_'+what
        s+= r'''
        \subsubsection{'''+d[inp]+'''}


\\qfig{4fig/DRCAT/'''+(tab+'_false'+tab)+'''_c-0.png}{fig:'''+tab+'''f}{ Grouping by '''+d[inp]+'''. }{.9\\textwidth}

\\dfig{4fig/DRCAT/'''+(tab+'_Carbons'+tab)+'''_c-0.png}{4fig/DRCAT/'''+(tab+'_ocratio'+tab)+'''_c-0.png}
{fig:'''+tab+'''}{'''+(d[inp]+' grouped using '+what)+'''}
'''

        if inp == 'embed_fn_':
            inp=inp[:-1]
            d[inp] = 'Function Categories'

        s+='''
        \\qfig{./4fig/DR/'''+(what+'_'+inp+'-0')+'''.png}{fig:'''+(what+'_'+inp)+'''}{A selection of colourings for the '''+d[inp]+''' inputs. Part 1  }{.9\\textwidth}
        \\qfig{./4fig/DR/'''+(what+'_'+inp+'-1')+'''.png}{fig:'''+(what+'_'+inp)+'''}{A selection of colourings for the '''+d[inp]+''' inputs. Part 2  }{.9\\textwidth}
    '''


    with open(what+'.tex','w') as f:
        print what
        f.write(s)


'''
#find . -name "*.pdf" -delete

for f in *; do mv "$f" `echo $f | tr ' ' '_'`; done

for i in *.png; do
     convert $i -crop 98.5% ${i}
done

rm *_c-1*.png *_c-2*.png *_c-3*.png

'''
