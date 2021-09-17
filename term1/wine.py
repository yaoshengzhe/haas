#! /usr/local/bin/python3

import graphviz

def main():
    graph = graphviz.Digraph(comment='Wine')

    graph.node('start', 'Start')
    graph.node('storm', 'Storm')
    graph.node('nostorm', 'NoStorm')
    graph.edge('start', 'storm', label='0.5')
    graph.edge('start', 'nostorm', label='0.5')

    graph.node('bmold', 'Botrytis Mold = $8')
    graph.node('thinwine', 'ThinWine = $2')
    graph.edge('storm', 'bmold', label='0.4')
    graph.edge('storm', 'thinwine', label='0.6')

    graph.node('bottle', 'Bottle')
    graph.node('notbottle', 'Not Bottle')
    graph.edge('thinwine', 'bottle', label='p')
    graph.edge('thinwine', 'notbottle', label='1-p')
    
    graph.node('fully', 'Faully Rapen = $3.5')
    graph.node('top20', 'Top 20% = $3')
    graph.node('lowacid', 'Low Acid = $2.5')
    graph.edge('nostorm', 'fully', label='0.4')
    graph.edge('nostorm', 'top20', label='0.4')
    graph.edge('nostorm', 'lowacid', label='0.2')
    
    
    
    graph.render('wine.gv', view=True)

if __name__ == '__main__':
    main()
