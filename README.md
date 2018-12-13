# Sequence_align
Python script for DNA sequence alignments. Biopython의 기능을 사용.

## How to use
1. 하나의 폴더안에 Template_DNA.txt 파일과 Sequencing 결과 파일이 필요
2. Align.py 스크립트를 복사해서 동일한 폴더에 넣음
3. 스크립트 파일을 실행하면 algin_result.seq 파일이 생성

터미널을 사용할 경우 폴더안에서 다음의 명령어를 입력
```bash
$ python Align.py
```

## 생각할점
Template_DNA 파일에는 하나의 시퀀스만 들어있어야 함.
파일의 확장자가 다름을 확인 할 것.
모든 시퀀스는 엄격한 Fasta format의 형태 일 것

## 앞으로 수정할 점
- [ ] Template_DNA 파일에 여러 시퀀스가 들어가 있을 경우에도 작동할수 있어야함.
- [ ] GUI를 만들어서 보다 쉽게 이해 할수 있어야함.
- [ ] 결과 파일을 좀 더 알기 쉽게

