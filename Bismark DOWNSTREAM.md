Bismark DOWNSTREAM
```
/TBI/People/tbi/siyoo/miniconda3/envs/mine/bin/bedtools intersect
-a /data05/project/jhshin/TBD231116_18814_methylseq_mine_20231017/analysis/do_metilene/DMR0001/metilene_G1_G2.output.denovo
-b /TBI/Share/BioPeople/siyoo/Pipelines/MINE/ref/Homo_sapiens/ENS72/data/anno_Merge/1.annoTable
-wa -wb > /data05/project/jhshin/TBD231116_18814_methylseq_mine_20231017/analysis/do_metilene/DMR0001/metilene_G1_G2.output.denovo.1.anno
```

CHR	START	END<br>
8	84314784	84317057
<be>

MEMBER.UP1K<br>
8_84314993_84315992_UP1K_ENST00000522365



```
head -1 /data05/project/jhshin/TBD231116_18814_methylseq_mine_20231017/report/DMR/DMR0001-PHH-Huh7_5.xls > DMR_LINC01419.xls
grep 000522365 /data05/project/jhshin/TBD231116_18814_methylseq_mine_20231017/report/DMR/DMR0001-PHH-Huh7_5.xls >> DMR_LINC01419.xls
```

```
head -1 /TBI/Share/BioPeople/siyoo/Pipelines/MINE/ref/Homo_sapiens/ENS72/data/anno_Merge/8.annoTable > 8.LINC01419.annoTable
grep 8_84314993_84315992_UP1K_ENST00000522365 /TBI/Share/BioPeople/siyoo/Pipelines/MINE/ref/Homo_sapiens/ENS72/data/anno_Merge/8.annoTable >> 8.LINC01419.annoTable
```
