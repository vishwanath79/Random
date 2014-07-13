import os
import string
import sys
import avro
from avro import io
from avro import schema
from avro import datafile

if __name__ == '__main__':
    if len(sys.argv) !=2:
        sys.exit('Usage: %s <data_file>' %sys.argv[0])
    avro_file =sys.argv[1]
    writer = open(avro_file,'wb')
    datum_writer = io.DatumWriter()
    schema_object = schema.parse("""\
{"type":"record",
 "name":"StringPair",
 "doc":"A pair of strings.",
 "fields": [
   {"name":"left","type":"string"},
   {"name":"right","type":"string"}
    ]
}""")
    dfw =datafile.DataFileWriter(writer,datum_writer,schema_object)
    for line in sys.stdin.readlines():
        (left,right) =string.split(line.strip(),',')
        dfw.append({'left':left,'right':right});
    dfw.close()
	
# python AvroSave.py pairs.py
#	a,1
#	b,2
#	c,3
#   CTRl+z

# Reading the Avro File

import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
reader = DataFileReader(open("pairs.avro", "r"), DatumReader())
for user in reader:
    print user
reader.close()