def manipulate_data(data_type=None, data=None):
    accepted_data_types = {
        'list': 'data[-1:: -1]',
        'set': 'set.union(data, ["ANDELA", "TIA", "AFRICA"])',
        'dictionary': '[key for key, item in data.items()]'
    }
    return eval(accepted_data_types['%s' % data_type])

#def manipulate_data(data_struct=None, data=None):
  #if data_struct == 'list':
    #return data[-1:: -1]
  #if data_struct == 'set':
    #return set.union(data, ["ANDELA", "TIA", "AFRICA"])
  #if data_struct == 'dictionary':
    #return [key for key, item in data.items()]
  
#def manipulate_data(data_struct=None, data=None):
  #if data_struct == 'list':
    #return data[-1:: -1]
  #if data_struct == 'set':
    #return set.union(data, ['"ANDELA"', '"TIA"', '"AFRICA"'])
  #if data_struct == 'dictionary':
    #return [key for key, item in data.items()]

#def manipulate_data(struct, data):
  #if struct == 'list':
    #return data[::-1]
  #if struct == 'set':
    #return data | set(["ANDELA", "TIA", "AFRICA"])
  #if struct == 'dictionary':
    #return data.keys()
