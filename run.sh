
# mkdir data

# 运行服务
# nohup python getTeleData.py &
source ~/.bashrc

project=ETC
mkdir -p $project/data
cat ~/qinsiyuan/LET/log/$project/* | python log2dict.py > $project/token2id.json
cat $project/token2id.json
cat $project/data/*.log | python teleDataFilter.py > $project/teleid2result.json
cat $project/teleid2result.json
python result2id.py > $project/server.preload.json
cat $project/server.preload.json
