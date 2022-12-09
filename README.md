# -Python
https://docs.docker.com/get-docker/
git@github.com:computer-science-itmo-ict/cs-lab-5-12262004-m.git



По поводу ssh ключей
Открываем терминал пишем
ssh-keygen -t rsa -b 4096
тыкаем энтер несколько раз

потом вводим
cat ~/.ssh/id_rsa.pub
копируем то что выдало и идем на гитхаб
settings => SSH and GPG keys => New SSH Key
вставляем то что скопировали и нажимаем добавить

все должно быть норм, после этого пишем в терминале

git clone git@github.com:computer-science-itmo-ict/cs-lab-1-<name>.git

где name ваше имя на гх
