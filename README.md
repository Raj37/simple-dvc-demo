1. create env
```bash
conda create -n wineq python=3.7 -y
```
2. activate env
```bash
conda activate wineq 
```
3. create requirements.txt file
4. install the requirements
```bash
pip install -r requirements.txt
```
5. download the data from
```bash
https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing
```
6. git init
7. dvc init
8. dvc add data_given/winequality.csv
9. git add .
10. git commit -m "first commit"

tox library- it's a test automation project. tox creates a virtual env for you based on your requirements and 
we can specify the environments suppose we want to test app for python 2.7 (legacy) and python 3.7 (latest)