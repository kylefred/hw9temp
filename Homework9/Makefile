all: output/hw9_1.txt output/hw9_2.txt output/hw9_3.txt

built: py36/Dockerfile
	docker build -t py36 ./py36/ && touch built

output/hw9_1.txt: built
	docker run -d --rm -v /home/kylefg95/hw9temp/Homework9:/workdir -w /workdir py36 /bin/bash -c "python3 hw9_1.py 2 3 7 4 6 > output/hw9_1.txt"

output/hw9_2.txt: built
	docker run -d --rm -v /home/kylefg95/hw9temp/Homework9:/workdir -w /workdir py36 /bin/bash -c "python3 hw9_2.py 5 2 17 > output/hw9_2.txt"

output/hw9_3.txt: built
        docker run -d --rm -v /home/kylefg95/hw9temp/Homework9:/workdir -w /workdir py36 /bin/bash -c "python3 hw9_3.py > output/hw9_3.txt"

clean:
	rm built
