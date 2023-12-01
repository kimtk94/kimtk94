Per Base Coverage Plot
=====

<b> ## Starts with BAM File ## <b>

## 0. Prepare pyGenomeTrack
```
conda install -c bioconda pygenometracks
```

## 1. Bam to Bedgraph(bg)

```
bedtools genomecov -ibam {sample.bam} -bg | gzip > {sample.bedgraph.gz}
```

## 2. run pyGenomeTracks with 4C-seq

### 2-1. Prepare Bed File
```
track type=bed name=regions_to_plot

```

### 2-2. Prepare ini File

```
[x-axis]
where = top

[spacer]
height = 0.05

[test bedgraph]
file = {sample.bedgraph.gz}
color = blue
height = 5
title = bedgraph rasterize = true
rasterize = true
max_value = 10

[test bedgraph]
file = {sample.bedgraph.gz}
color = blue
height = 5
title = bedgraph
max_value = 10

[test bedgraph use middle]
file = {sample.bedgraph.gz}
color = blue
height = 5
title = bedgraph with use_middle = true
max_value = 10
use_middle = true

[genes]
file = HoxD_cluster_regulatory_regions_mm10.bed
height = 3
title = HoxD genes and regulatory regions
```

```
pyGenomeTracks --tracks ini/UP1K_DMR_S0001_S0002_bedgraph.ini --BED BED/LINC01419.target.bed --trackLabelFraction 0.1 --width 60 --dpi 130 -o UP1K_DMR_S0001_S0002_bedGraph.png --fontSize 13 --trackLabelHAlign left
```
