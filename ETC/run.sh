
# mkdir data

# 运行服务
# nohup python getTeleData.py &
source ~/.bashrc

project=ETC
mkdir -p data
cat ~/qinsiyuan/LET/log/$project/* | python log2dict.py > token2id.json
cat token2id.json
cat data/*.log | python teleDataFilter.py > teleid2result.json
cat teleid2result.json
python result2id.py > server.preload.json
cat server.preload.json
