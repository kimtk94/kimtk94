<img src="https://github.com/kimtk94/kimtk94/assets/65493390/709c1366-2fd5-486e-8ede-9cdb94243ce3" height="200px">
<br/>

BISMARK 
=======

## 1.BISMARK MAP
```
bismark --parallel 8 --fastq --phred33-quals --output_dir {OUTPUT_DIR}
--bowtie2 -N {0} -L {20} -p {2} --path_to_bowtie {BOWTIE_POSITION} --temp_dir {TEMP_DIR}
--unmapped --samtools_path {SAMTOOLS_POSITION} {REF} -1 {READ1} -2 {READ2}
```
{OUTPUT_DIR} : Output 폴더명 <br>
{N} : mismatch 허용 개수 <br>
{L} : seed의 최소 길이 <br>
{p} : multiple processors/cores <br>
{BOWTIE_POSITION} : Bowtie2 실행 가능 위치 <br>
{TEMP_DIR} : temp 폴더 위치 <br>
{SAMTOOLS_POSITION} : samtools 실행 가능 위치 <br>
{REF} : Reference 위치 / bowtie2-build 필요 <br>
{READ1} / {READ2} : read1, read2 위치 <br>
<br>

## 2.BISMARK DEDUP
```
bismark --paired --output_dir {OUTPUT_DIR}
--bam --samtools_path {SAMTOOLS_POSITION} {BAM}
```
{OUTPUT_DIR} : Output 폴더명 <br>
{SAMTOOLS_POSITION} : samtools 실행 가능 위치 <br>
{BAM} : bam 위치
