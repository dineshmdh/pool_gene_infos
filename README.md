## Pooling metadata information for all human genes

This is a resource repository. The goal was to collect these information for all gencode (version 19) or RefSeq genes:
1. Gene Symbols
2. TSS location
3. TAD information
4. Expression across various cell types in Epigenomics Roadmap database.

The final output file is [this](/merge_tad_and_gexes/roadmap.rnase_imputed.LogRPKM.signal.mergedWTADlocs.txt) (filesize: 24MB). Check the  the notes below and the functions in the directories to see how the metadata for the genes were processed and pooled. (**Note: Currently, only Roadmap RNA-seq data is used. I am working to generate a similar metadata file with ENCODE RNA-seq data as well.**)


### TAD information - TAD domain boundaries and sizes

TAD boundary lists across 21 cell types is obtained from [this paper](http://www.sciencedirect.com/science/article/pii/S2211124716314814) (Table S3). While merging these TAD boundaries, only those that are present in at least 20 % of the cell types (i.e. >= 4 out of 21 from the paper) are considered. Additionally, telomere regions and centromere-containing TADs are eventually thrown out. For this, the `hg19.gaps.txt` file was downloaded from the ucsc database (click [here](hgdownload.cse.ucsc.edu/goldenPath/hg19/database/gap.txt.gz) to download the file), and used. Specifically, (i) boundaries of the first and last TAD domains in every chromosome demarcate the boundaries of the telomeres as well, and (ii) TADs overlapping centromeres are discarded.

chr17 assembly gap info was missing from the gap file. However, chr17 is also treated as other chromosomes and telo-/centro-meres are removed similarly (first and last 10kb are discarded as telomeres). chrY TAD info was missing in the paper. So, this chromosome is not considered for the TAD boundary specification step.


### Expression across various cell types in Epigenomics Roadmap database.

hg19 RefSeq gtf gene annotation file was downloaded from the UCSC webpage. For each gene, only reads mapping to TSS +/- 500bp region was used as proxy of the expression level, as done in [this paper](https://www.nature.com/articles/ng.3950). A gene with multiple TSS+/-500bp regions corresponding to its transcripts had a transcript randomly selected for downstream analyses. This resulted in a total of 27,544 genes.

For the ROADMAP data, only imputed RNA-seq data for the 127 samples (Epigenome IDs ranging from E001-E129) were downloaded and processed. As with the DNase-seq samples, these 127 RNA-seq epigenome samples represent uniformly processed, consolidated samples. The log RPKM bigwig signal file for each sample was converted to bedgraph file, and mapped onto each TSS+/-500bp region as a proxy of raw imputed expression value of the gene on the sample.


## Contact
Email dm237 [at] duke [dot] edu for any questions or suggestions.

