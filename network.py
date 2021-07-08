from graphviz import Graph
import os

inp = "./Input/"
prof_count = 9
exp_count = 8


def loadData(fName):
    data = []
    with open(fName) as f:
        # This is just a nifty python thing that lets us avoid exceptions
        lines = f.readlines()  # Reads every line into a list
        lines.__delitem__(0) # delete the first line
        for line in lines:
            data.append(line.split())
    return data


def makeGraph():
    for filename in os.listdir(inp):
        print(filename)
        outName = filename.replace(".txt", "")
        g = Graph(engine='sfdp', strict=True)
        data = loadData(inp + filename)
        g.attr(overlap='false')
        g.node_attr.update(fixedsize='true', fontsize='12', width='0.5', height='0.5', style='filled')

        # [['47', '44', '45', '46', '49', '52'], ['35', '36', '37', '38'], ['39', '40', '43', '48'],
        #  ['76', '77', '78', '79'], ['0', '1', '6'], ['25', '29', '30'], ['26', '27', '28'], ['53', '54', '65'],
        #  ['73', '74', '75'], ['69', '70', '71'], ['4', '5'], ['2', '3'], ['7', '22'], ['23', '24'], ['32', '31'],
        #  ['33', '34'], ['41', '42'], ['50', '51'], ['60', '59'], ['61', '62'], ['55', '56'], ['57', '58'], ['64', '63'],
        #  ['67', '68'], ['8'], ['9'], ['10'], ['17'], ['11'], ['12'], ['13'], ['14'], ['15'], ['16'], ['18'], ['19'],
        #  ['20'], ['21'], ['66'], ['72']]

        for n in ['47', '44', '45', '46', '49', '52']:
            g.node(str(n), fillcolor='cyan')

        for n in ['35', '36', '37', '38']:
            g.node(str(n), fillcolor='orange')

        for n in ['39', '40', '43', '48']:
            g.node(str(n), fillcolor='yellow')

        for n in ['76', '77', '78', '79']:
            g.node(str(n), fillcolor='green')

        for n in ['0', '1', '6']:
            g.node(str(n), fillcolor='red')

        for n in ['25', '29', '30']:
            g.node(str(n), fillcolor='coral')

        for n in ['26', '27', '28']:
            g.node(str(n), fillcolor='cornflowerblue')

        for n in ['53', '54', '65']:
            g.node(str(n), fillcolor='darkgoldenrod1')

        for n in ['73', '74', '75']:
            g.node(str(n), fillcolor='aquamarine')

        for n in ['69', '70', '71']:
            g.node(str(n), fillcolor='deeppink')

        for n in ['4', '5']:
            g.node(str(n), fillcolor='darkolivegreen1')

        for n in ['2', '3']:
            g.node(str(n), fillcolor='hotpink')

        for n in ['7', '22']:
            g.node(str(n), fillcolor='peru')

        for n in ['23', '24']:
            g.node(str(n), fillcolor='magenta')

        for n in ['32', '31']:
            g.node(str(n), fillcolor='maroon')

        for n in ['33', '34']:
            g.node(str(n), fillcolor='orangered')

        for n in ['41', '42']:
            g.node(str(n), fillcolor='plum')

        for n in ['50', '51']:
            g.node(str(n), fillcolor='seagreen1')

        for n in ['60', '59']:
            g.node(str(n), fillcolor='skyblue1')

        for n in ['61', '62']:
            g.node(str(n), fillcolor='sienna1')

        for n in ['55', '56']:
            g.node(str(n), fillcolor='thistle')

        for n in ['57', '58']:
            g.node(str(n), fillcolor='tomato')

        for n in ['64', '63']:
            g.node(str(n), fillcolor='violet')

        for n in ['67', '68']:
            g.node(str(n), fillcolor='steelblue1')

        #------------------SumAbsWeightDiff - June2 - Adjusted - 50% -----------------------------------------------------------
        # [['53', '54', '65', '63', '66', '64'], ['6', '4', '1', '0', '5'], ['39', '48', '40', '43'],
        #  ['79', '76', '77', '78'], ['45', '44', '46'], ['28', '26', '27'], ['70', '71', '69'], ['51', '50'],
        #  ['56', '55'], ['2', '3'], ['68', '67'], ['41', '42'], ['24', '23'], ['31', '32'], ['8', '7'], ['75', '74'],
        #  ['49', '52'], ['61', '62'], ['9', '10'], ['59', '60'], ['58', '57'], ['30', '29'], ['16', '19'], ['33', '34'],
        #  ['38', '37'], ['35', '36'], ['17'], ['13'], ['18'], ['22'], ['47'], ['72'], ['14'], ['11'], ['73'], ['15'],
        #  ['25'], ['12'], ['20'], ['21']]

        # for n in ['53', '54', '65', '63', '66', '64']:
        #     g.node(str(n), fillcolor='cyan')
        #
        # for n in ['6', '4', '1', '0', '5']:
        #     g.node(str(n), fillcolor='orange')
        #
        # for n in ['39', '48', '40', '43']:
        #     g.node(str(n), fillcolor='yellow')
        #
        # for n in ['79', '76', '77', '78']:
        #     g.node(str(n), fillcolor='green')
        #
        # for n in ['45', '44', '46']:
        #     g.node(str(n), fillcolor='red')
        #
        # for n in ['28', '26', '27']:
        #     g.node(str(n), fillcolor='coral')
        #
        # for n in ['70', '71', '69']:
        #     g.node(str(n), fillcolor='cornflowerblue')
        #
        # for n in ['51', '50']:
        #     g.node(str(n), fillcolor='darkgoldenrod1')
        #
        # for n in ['56', '55']:
        #     g.node(str(n), fillcolor='aquamarine')
        #
        # for n in ['2', '3']:
        #     g.node(str(n), fillcolor='deeppink')
        #
        # for n in ['68', '67']:
        #     g.node(str(n), fillcolor='darkolivegreen1')
        #
        # for n in ['41', '42']:
        #     g.node(str(n), fillcolor='hotpink')
        #
        # for n in ['24', '23']:
        #     g.node(str(n), fillcolor='peru')
        #
        # for n in ['31', '32']:
        #     g.node(str(n), fillcolor='magenta')
        #
        # for n in ['8', '7']:
        #     g.node(str(n), fillcolor='maroon')
        #
        # for n in ['75', '74']:
        #     g.node(str(n), fillcolor='orangered')
        #
        # for n in ['49', '52']:
        #     g.node(str(n), fillcolor='plum')
        #
        # for n in ['61', '62']:
        #     g.node(str(n), fillcolor='seagreen1')
        #
        # for n in ['9', '10']:
        #     g.node(str(n), fillcolor='skyblue1')
        #
        # for n in ['59', '60']:
        #     g.node(str(n), fillcolor='sienna1')
        #
        # for n in ['58', '57']:
        #     g.node(str(n), fillcolor='thistle')
        #
        # for n in ['30', '29']:
        #     g.node(str(n), fillcolor='tomato')
        #
        # for n in ['16', '19']:
        #     g.node(str(n), fillcolor='violet')
        #
        # for n in ['33', '34']:
        #     g.node(str(n), fillcolor='steelblue1')
        #
        # for n in ['38', '37']:
        #     g.node(str(n), fillcolor='yellowgreen')
        #
        # for n in ['35', '36']:
        #     g.node(str(n), fillcolor='sandybrown')

# ------------------SumAbsWeightDiff - June2 - Adjusted - 50% -----------------------------------------------------------
# ------------------SumSqrWeightDiff - June2 - Adjusted - 50% -----------------------------------------------------------

        # [['77', '78', '76', '79'], ['40', '39', '43', '48'], ['71', '70', '69'], ['65', '54', '53'], ['45', '44', '46'],
        #  ['66', '63', '64'], ['27', '28', '26'], ['19', '20', '16'], ['41', '42'], ['0', '1'], ['50', '51'],
        #  ['38', '37'], ['11', '13'], ['59', '60'], ['5', '4'], ['12', '18'], ['55', '56'], ['67', '68'], ['10', '9'],
        #  ['34', '33'], ['23', '24'], ['7', '8'], ['15', '21'], ['31', '32'], ['29', '30'], ['2', '3'], ['62', '61'],
        #  ['74', '75'], ['58', '57'], ['35', '36'], ['14'], ['72'], ['6'], ['47'], ['49'], ['22'], ['17'], ['73'],
        #  ['52'], ['25']]

        # for n in ['77', '78', '76', '79']:
        #     g.node(str(n), fillcolor='cyan')
        #
        # for n in ['40', '39', '43', '48']:
        #     g.node(str(n), fillcolor='orange')
        #
        # for n in ['71', '70', '69']:
        #     g.node(str(n), fillcolor='yellow')
        #
        # for n in ['65', '54', '53']:
        #     g.node(str(n), fillcolor='green')
        #
        # for n in ['45', '44', '46']:
        #     g.node(str(n), fillcolor='red')
        #
        # for n in ['66', '63', '64']:
        #     g.node(str(n), fillcolor='coral')
        #
        # for n in ['27', '28', '26']:
        #     g.node(str(n), fillcolor='cornflowerblue')
        #
        # for n in ['19', '20', '16']:
        #     g.node(str(n), fillcolor='darkgoldenrod1')
        #
        # for n in ['41', '42']:
        #     g.node(str(n), fillcolor='aquamarine')
        #
        # for n in ['0', '1']:
        #     g.node(str(n), fillcolor='deeppink')
        #
        # for n in ['50', '51']:
        #     g.node(str(n), fillcolor='darkolivegreen1')
        #
        # for n in ['38', '37']:
        #     g.node(str(n), fillcolor='hotpink')
        #
        # for n in ['11', '13']:
        #     g.node(str(n), fillcolor='peru')
        #
        # for n in ['59', '60']:
        #     g.node(str(n), fillcolor='magenta')
        #
        # for n in ['5', '4']:
        #     g.node(str(n), fillcolor='maroon')
        #
        # for n in ['12', '18']:
        #     g.node(str(n), fillcolor='orangered')
        #
        # for n in ['55', '56']:
        #     g.node(str(n), fillcolor='plum')
        #
        # for n in ['67', '68']:
        #     g.node(str(n), fillcolor='seagreen1')
        #
        # for n in ['10', '9']:
        #     g.node(str(n), fillcolor='skyblue1')
        #
        # for n in ['34', '33']:
        #     g.node(str(n), fillcolor='sienna1')
        #
        # for n in ['23', '24']:
        #     g.node(str(n), fillcolor='thistle')
        #
        # for n in ['7', '8']:
        #     g.node(str(n), fillcolor='tomato')
        #
        # for n in ['15', '21']:
        #     g.node(str(n), fillcolor='violet')
        #
        # for n in ['31', '32']:
        #     g.node(str(n), fillcolor='steelblue1')
        #
        # for n in ['29', '30']:
        #     g.node(str(n), fillcolor='yellowgreen')
        #
        # for n in ['2', '3']:
        #     g.node(str(n), fillcolor='sandybrown')
        #
        # for n in ['62', '61']:
        #     g.node(str(n), fillcolor='rosybrown3')
        #
        # for n in ['74', '75']:
        #     g.node(str(n), fillcolor='powderblue')
        #
        # for n in ['58', '57']:
        #     g.node(str(n), fillcolor='mistyrose')
        #
        # for n in ['35', '36']:
        #     g.node(str(n), fillcolor='indianred')

# ------------------SumSqrWeightDiff - June2 - Adjusted - 50% -----------------------------------------------------------

        for d in data:
            # if d[0] <= d[1]:
            g.edge(d[0], d[1], weight="0.5", label=d[2])

        g.render(filename=outName+"_louvain_communities", directory='Output/', cleanup=True,
                 format='png')



def main():
    makeGraph()
    pass


main()

