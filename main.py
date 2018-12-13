import tabulate
import sys
from osrs_ge import OSRS_GE_Data
from visualization import Visualization

def display_alch_profit():      
    ge = OSRS_GE_Data()
    #This doesn't work right if the traded quantity is 0
    alchfunc = lambda x: ge.ge_json[x]['sp']*0.6 - ge.nature_rune - ge.ge_json[x]['overall_average'] if ge.ge_json[x]['overall_average'] > 0 else -sys.maxsize - 1
    lf = alchfunc
    jl = ge.sort_json(ge.ge_json, lf,True)
    small_list = ge.get_top_values(10, jl)
    sorted_list = []
    for id in small_list:
        #TODO: This should be parameterized and maybe made into an insert function
        temp_entry = ge.get_entry(id)
        temp_entry['alch_diff'] = lf(id)
        print(temp_entry)
        sorted_list.append(temp_entry)
    '''header = sorted_list[0].keys()
    rows =  [x.values() for x in sorted_list]
    print(tabulate.tabulate(rows, header))'''
    vis = Visualization()
    vis.display(sorted_list, x='name', y='alch_diff')

if __name__ == "__main__":
    display_alch_profit()

#Sample usage:
'''
ge = OSRS_GE_Data(nature_rune=280)
price_sort = lambda x: ge.ge_json[x]['sp']
lf = lambda x: ge.ge_json[x]['sell_quantity']
jl = ge.sort_json(ge.ge_json, lf, True)
small_list = ge.get_top_values(10, jl)
named_list = ge.get_list_by_value(small_list, "name")
print(named_list)
'''
#Results: lf contains the sorting key, jl contains the sorted list (only ids), small_list takes the top of the sorted list

#high alch lambda sort_function - testing mediawiki api calls
'''
alchfunc = lambda x: ge.ge_json[x]['sell_average'] - ge.ge_json[x]['sp']*0.6
'''
