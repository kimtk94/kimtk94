# SINGULARITY <img src="https://github.com/kimtk94/kimtk94/assets/65493390/a258420d-3ec4-485a-960a-a10c0a82000c" width="120"/>

## 1. Download DOCKER
```
singularity pull docker://galaxyworks/pygenometracks:latest
```
<img src="https://github.com/kimtk94/kimtk94/assets/65493390/5a49f79c-36b8-4358-85a4-6daba35d08e6"/>

## 2. RUN SINGULARITY
```
singularity shell --bind {$PWD}:/mnt pygenometracks_latest.sif
```
