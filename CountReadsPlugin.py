import pandas as pd

import PyPluMA
import PyIO
class CountReadsPlugin:
    def input(self, inputfile):
       self.parameters=PyIO.readParameters(inputfile)
    def run(self):
       pass
    def output(self,outputfile):
       samples_list = [x.strip('\n') for x in open(PyPluMA.prefix()+"/"+self.parameters["samples"]).readlines()]
       samples_dir = self.parameters["samplesdir"]
       out_read_counts = outputfile

       read_count_dict = {"sample":[], "n_reads":[]}
       for sample in samples_list:
           count=0
           with open(samples_dir+sample+'.fastq', 'r') as f:
               print(sample)
               for line in f.readlines():
                   if line[0]=='@':
                       count+=1
           read_count_dict["sample"].append(sample)
           read_count_dict["n_reads"].append(count)

       df = pd.DataFrame.from_dict(read_count_dict)
       df.to_csv(out_read_counts, index=False)

