from os import listdir
import json
# name = 'Building a Second Brain'
name = 'Effortless'
fpath2RM = 'C:/Users/mariv/AppData/Roaming/remarkable/desktop'
listRMDesktop = listdir(fpath2RM); 
# listRMDesktop[2].split('.')
listMetadata =  [fRM for fRM in listRMDesktop if fRM.split('.')[-1] == 'metadata']

lMd = []
for ii in range(len(listMetadata)):
    try:
    
        f = open(fpath2RM+'/'+listMetadata[ii], 'r')
        json_meta = f.read();
        f.close()
        #print(json_meta)
        l = [att.strip('\n').strip(' ').split(':')[1].strip(' ').strip('"') for att in json_meta.strip('\n')[1:-1].strip('\n').strip(' ').split(',') if 'visibleName' in att][0]
        #print(f'{l[0:20]:30s}, 4')
        
        if name in l:
            lMd.append(listMetadata[ii].split('.')[0])
            print(f'{l:30s}, {listMetadata[ii]}')
        
    except:
        pass
        #print(listMetadata[ii])

lMd0 =  [[fRM for fRM in listRMDesktop if fRM.split('.')[0] == ii] for ii in lMd]
lMd0.sort()
lMd0 = lMd0[0] # 1 for BASB
n = [ii for ii in range(len(lMd0)) if 'highlights' in lMd0[ii]]
fpath = fpath2RM + '/'+lMd0[n[0]]
highlightslist = listdir(fpath)


with open('C:/Users/mariv/Documents/1-Projects/RM-Notes/' + name +'.md', 'a+', encoding='utf-8') as fmd:
    # fmd.write('# ' +name + '\n')
    # s = ''
    fmd.seek(0)
    dataFile = fmd.read()
    if len(dataFile) ==  0:
        fmd.write('# ' +name + '\n')

    for highfile in highlightslist:

        with open(fpath + '/'+ highfile, encoding='utf-8') as fh:
            data = json.load(fh)

        color = list()
        start = list()
        text  = list()
        for n in range(len(data['highlights'][0])):
            color.append(data['highlights'][0][n]['color'])
            start.append(data['highlights'][0][n]['start'])
            text.append(data['highlights'][0][n]['text'])

        # Order data by using the start information
        start, color, text = zip(*sorted(zip(start, color, text)))

        # print(color, start, text)
        for i in range(len(color)):
            if text[i] not in dataFile:
                fmd.write('\n')
                if color[i] == 8: # gray
    #                 s = s + '\t * ' + text[i] + '\n'
                    fmd.write('* ' + text[i] + '\n')
                if color[i] == 3: # yellow
    #                 s = s + '### ' + text[i] + '\n'
                    fmd.write('## ' + text[i] + '\n')
                if color[i] == 4:
                    fmd.write('### ' + text[i] + '\n')
                # fmd.write('\n')