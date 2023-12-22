# Container

## 1. 특징
1) 기존의 Hypervisor(하이퍼바이저) + VM 방식 ['하드웨어 레벨'] 대비 가볍고 빠르게 동작
2) Container는 Kernel(커널)이 격리된 사용자 공간 인스턴스를 갖추도록 하는 가상화 방식이며, 이를 'OS 레벨 가상화'라고 불림
3) OS를 포함하고 있지 않아 MB 단위이며, 운영 체제 부팅이 필요하지 않아 부팅 시간이 빠름 -> 마이크로 서비스 구축에 최적

---

# Image

## 1. 특징
1) 컨테이너 실행에 필요한 파일과 설정값을 포함하고 있는 파일
2) 상태값을 가지지 않고 변하지 않는 특성 => 실행 중 추가되거나 변하는 겂은 컨테이너에 저장됨


---

# Docker

## 1. 특징
1) 오픈소스 기반의 컨테이너 관리 플랫폼
2) 리눅스의 응용 프로그램들을 소프트웨어 컨테이너 안에 배치시키는 일을 자동화하는 LXC(LinuX Container) 기술 기반

# DOCKER COMMAND
## ADD
1. copy file(directory) into Docker Image from 3 resouce
   1) files from local storage
   2) tarball from local storage
   3) URL
2. Code Syntax<br>
  
```
   ADD {source} {destination}
```

## /bin/sh -c rm -rf /var/lib/apt/lists/*
1. apt를 통해 패키지 설치 중에 생성된 패키지 cache 또는 tmp를 정리한다.
2. 이를 통해 Docker Image 크기를 줄이는 일반적인 단계


## /bin/sh -c set -xe 		&& echo '#!/bin/sh' > /usr/sbin/policy-rc.d 	&& echo 'exit 101' >> /usr/sbin/policy-rc.d 	&& chmod +x /usr/sbin/policy-rc.d 		&& dpkg-divert --local --rename --add /sbin/initctl 	&& cp -a /usr/sbin/policy-rc.d /sbin/initctl 	&& sed -i 's/^exit.*/exit 0/' /sbin/initctl 		&& echo 'force-unsafe-io' > /etc/dpkg/dpkg.cfg.d/docker-apt-speedup 		&& echo 'DPkg::Post-Invoke { "rm -f /var/cache/apt/archives/*.deb /var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin || true"; };' > /etc/apt/apt.conf.d/docker-clean 	&& echo 'APT::Update::Post-Invoke { "rm -f /var/cache/apt/archives/*.deb /var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin || true"; };' >> /etc/apt/apt.conf.d/docker-clean 	&& echo 'Dir::Cache::pkgcache ""; Dir::Cache::srcpkgcache "";' >> /etc/apt/apt.conf.d/docker-clean 		&& echo 'Acquire::Languages "none";' > /etc/apt/apt.conf.d/docker-no-languages 		&& echo 'Acquire::GzipIndexes "true"; Acquire::CompressionTypes::Order:: "gz";' > /etc/apt/apt.conf.d/docker-gzip-indexes 		&& echo 'Apt::AutoRemove::SuggestsImportant "false";' > /etc/apt/apt.conf.d/docker-autoremove-suggests
