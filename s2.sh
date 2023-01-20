read -p "Masukan Dork : " int1
git clone https://github.com/Bitwise-01/SQL-scanner
cd SQL-scanner
pip install -r requirements.txt
python main.py -d $int1
