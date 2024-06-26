# cognitive_env (servingmodel and modelmanager)
git clone https://github.com/EmersonFariaOliveira/MLOPs.git
cd cognitive_env/
sudo docker build -t platserver -f dockerbuilds/DockerServer.txt .

sudo docker network create plat_network

sudo docker run -d --network plat_network -p 10001:8080 --restart always --name serving01 platserver python servingmodel.py ./models/model1.joblib 8080

sudo docker run -d --network plat_network -p 10002:8080 --restart always --name serving02 platserver python servingmodel_fake.py models/modelo02.joblib 8080

bash geraconfig.sh

sudo docker run -d --network plat_network -p 443:8080 --restart always -v $(pwd)/config:/myServer/config -v $(pwd)/Log:/myServer/Log --name modelmanager platserver python modelmanager.py

sudo docker network inspect plat_network

# interface
cd inference_interface/

sudo docker build -t gradio_interface -f dockerfile .

sudo docker run -d --network plat_network -p 7860:7860 --restart always --name interface gradio_interface python main.py