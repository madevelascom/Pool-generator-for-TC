__author__ = 'Made'

from string import Template

file1 = open("pool_try.txt", "r", encoding='utf-8')
result = open('pool_gameobject.txt', 'w', encoding='utf-8')
result2 = open('pool_template.txt', 'w', encoding='utf-8')

pool_start = 7370           //Pool id
pool_event = 5              //How many gameobjects involved
count = 0
event = 1                   //How many gameobjects will appear 
chance = 0                  //Chance, default = 0 to keep all chances equal
gob_name = 'Gameobject Name' //For comments in pool_template and pool_gameobject
gob_zone = 'Zone Name'      //For comments in pool_template and pool_gameobject
entry = Template('( $GUID, $start, $chance, \' $gob_name - $gob_zone $event \' ),\n')
entry2 = Template('($START, 1, \' $gob_name - $gob_zone $event \' ),\n')

insert1 = ('INSERT INTO pool_template VALUES)
insert2= ('INSERT INTO pool_gameobject VALUES)
result2.write(insert1)
result.write(insert2)

for line in file1:
    guid = format(line)
    guid = ''.join(guid.split())
    enter = str(entry.substitute(GUID=guid, start=pool_start, chance=chance, gob_name=gob_name, gob_zone=gob_zone,
                                 event=event))
    count += 1
    if count == pool_event:
        count = 0
        enter2 = str(entry2.substitute(START=pool_start, gob_name=gob_name, gob_zone=gob_zone, event=event))
        event += 1
        pool_start += 1
        result2.write(enter2)
    result.write(enter)


result.close()
result2.close()
