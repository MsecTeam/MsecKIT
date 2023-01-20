read -p "Masukan URL : " int1
git clone https://github.com/devanshbatham/ParamSpider
cd ParamSpider
pip3 install -r requirements.txt
python3 paramspider.py --domain $int1 -o hasil.txt
echo
echo "Hasil Di Directory Tools ParamSpider"
