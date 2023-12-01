Per Base Coverage Plot
=====

<b> ## Starts with BAM File ## <b>

## 1. Bam to Bedgraph(bg)

```
bedtools genomecov -ibam {sample.bam} -bg | gzip > {sample.bedgraph.gz}
```
