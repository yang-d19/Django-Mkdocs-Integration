# pull the newest static webpages
cd static-webpages
git pull

wait

# copy the generated site folder to the templates folder of django project
cd ..
cp -r static-webpages/site/ source/content/templates/
cd source/content/templates/
rm -rf main
mv site main

# when first time launch the gunicorn process, use these 4 lines
#cd ~/dagrad-site/source
#conda activate dagrad
#gunicorn --reload -w 4 --bind=0.0.0.0:8000 app.wsgi -D

# restart the running gunicorn process
pid=$(pstree -ap | grep -m 1 gunicorn | awk -F ',' '{print $2}' | awk -F ' ' '{print $1}’)
kill -HUP '$pid'

