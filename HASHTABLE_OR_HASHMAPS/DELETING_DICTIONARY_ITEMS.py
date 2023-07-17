mj_dict={'madhu':'001', 'sudhan':'002', 'vagale':'003', 'j':'004'}

print(mj_dict)

print(mj_dict.pop('sudhan'))    #pops specific key pair

print(mj_dict.popitem())        #pops last item

del mj_dict['madhu']            #deletes the record

print(mj_dict)

print(mj_dict.clear())          #clears tho whole dictionary
