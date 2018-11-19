all: output/hw9_1.txt output/hw9_2.txt output/hw9_3.txt

output/:
	mkdir output

py36/:
	mkdir py36

py36/Dockerfile: py36/
	printf "FROM python:3.6\n\nRUN pip install numpy\nRUN pip install pandas\n" > py36/Dockerfile

built: py36/Dockerfile
	docker build -t py36 ./py36/ && touch built

output/hw9_1.txt: built output/
	docker run -d --rm -v /home/kylefg95/hw9temp/Homework9:/workdir -w /workdir py36 /bin/bash -c "python3 hw9_1.py 2 3 7 4 6 > output/hw9_1.txt"

output/hw9_2.txt: built output/
	docker run -d --rm -v /home/kylefg95/hw9temp/Homework9:/workdir -w /workdir py36 /bin/bash -c "python3 hw9_2.py 5 2 17 > output/hw9_2.txt"

output/hw9_3.txt: built output/
	docker run -d --rm -v /home/kylefg95/hw9temp/Homework9:/workdir -w /workdir py36 /bin/bash -c "python3 hw9_3.py > output/hw9_3.txt"

clean:
	rm built
