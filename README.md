## Description
Scripts to make complex edits of an input string and output the results. The original purpose of these scripts was to remove information from the comments of a Newick tree of a NEXUS file. If more than one item is stored in a comment, the values are not read properly into R (using the readNexus function).

The scripts here are mostly made to address very specific, potentially non-standardized text-based file formats, but were funtionally necessary for me to pre-process files that needed to be loaded into R for statistical analysis. While these scripts may not be applicable to other situations, I have gathered them in this repo so that they are documented and available. 

