from Bio import SeqIO

######
#PIN3#
######

pin3 = SeqIO.parse("PIN3 AT1G70940_gene.fasta", "fasta")
pin3_lst = []
pin3_len = []
for seq in pin3:
    pin3_lst += [seq[1892:2328]]

#check if extracted sequence is full intron
print(pin3_lst[0].seq)
#correct

#now extract +- 50 bp
pin3 = SeqIO.parse("PIN3 AT1G70940_gene.fasta", "fasta")
pin3_lst = []
for seq in pin3:
    pin3_lst += [seq[1842:2378]]
    
#write out as FASTA
SeqIO.write(pin3_lst, "PIN3_intron_1130acc.fasta", "fasta")

######
#PIN4#
######

pin4 = SeqIO.parse("PIN4 AT2G01420_gene.fasta", "fasta")
pin4_lst = []
pin4_len = []
for seq in pin4:
    pin4_lst += [seq]
    pin4_len += [len(seq)]

#find shortest seq
min(pin4_len)
#3209 bp


#extract intron
pin4 = SeqIO.parse("PIN4 AT2G01420_gene.fasta", "fasta")
pin4_lst = []
pin4_len = []
for seq in pin4:
    pin4_lst += [seq[873:1250]]
    pin4_len += [len(seq[873:1250])]

#check intron extraction
print(pin4_lst[0])
print(len(pin4_lst[0]))
#correct

#extract intron +- 50 bp
pin4 = SeqIO.parse("PIN4 AT2G01420_gene.fasta", "fasta")
pin4_lst = []
pin4_len = []
for seq in pin4:
    pin4_lst += [seq[823:1300]]
    pin4_len += [len(seq[823:1300])]


#write out as FASTA
SeqIO.write(pin4_lst, "PIN4_intron_1130acc.fasta", "fasta")

######
#PIN7#
######
pin7 = SeqIO.parse("PIN7 AT1G23080_gene.fasta", "fasta")
pin7_lst = []
pin7_len = []
for seq in pin7:
    pin7_lst += [seq]
    pin7_len += [len(seq)]

#check pin7 len and seq
min(pin7_len)
print(pin7_lst[0].seq)
print(len(pin7_lst[0]))

#extract intron
pin7 = SeqIO.parse("PIN7 AT1G23080_gene.fasta", "fasta")
pin7_lst = []
pin7_len = []
for seq in pin7:
    pin7_lst += [seq[664:1105]]
    pin7_len += [len(seq[664:1105])]

#check pin7 intron len and seq
min(pin7_len)
print(pin7_lst[0].seq)
print(len(pin7_lst[0]))

#extract intron +- 50 bp
pin7 = SeqIO.parse("PIN7 AT1G23080_gene.fasta", "fasta")
pin7_lst = []
pin7_len = []
for seq in pin7:
    pin7_lst += [seq[614:1155]]
    pin7_len += [len(seq[614:1155])]

#write out as FASTA
SeqIO.write(pin7_lst, "PIN7_intron_1130acc.fasta", "fasta")













    