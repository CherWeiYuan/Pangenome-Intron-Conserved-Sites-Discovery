# Discovering conserved sites within PIN3 intron with pangenomic analysis

## Objective 
The main objective is to identify conserved positions in PIN3 intron for site-directed mutagenesis in the wet laboratory.

## Methods and Results
My initial attempt to align PIN3/4/7 introns from the pseudogenome of 1125 Arabidopsis thaliana accessions did not yield positions in which there is 100% conservation. There are, however, many positions in which there is 90% conservation, which is not helpful to pinpoint which sites we should target in the wet lab.

A plausible solution is to identify conserved sites across related species (pangenome analysis). I mined the NCBI nucleotide database for plants (taxid ID: 3193) to yield 23 homologs of PIN3 introns. Subsequently, these homologs are then used to train a nucleotide hidden Markov model (HMMER) to find closely related sequences in 13 Brassica genomes (taxid ID: 3705). The 87 sequences mined using nhmmer is then aligned to find successfully find pangenome conserved sites.

## Workflow
![alt text](https://raw.githubusercontent.com/CherWeiYuan/Pangenome-Intron-Conserved-Sites-Discovery/main/Images/workflow.png)

## How to navigate this repository
"Report_slides.pptx" will visually guide you through the analyses and results. 
The directories are numbered according to the chronological order of analysis. 
Inside the directories, you will find the scripts used, input data and output.
