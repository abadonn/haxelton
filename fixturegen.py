import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'newsic.settings'
import django
django.setup()

from newsic.news.models import Publisher, Topic
Publisher.objects.all().delete()
Topic.objects.all().delete()


pub_welt = Publisher(name="Die Welt")
pub_welt.save()

pub_bild = Publisher(name="Bild")
pub_bild.save()
pub_bz = Publisher(name="B.Z.")
pub_bz.save()
pub_sport_bild = Publisher(name="Sport Bild")
pub_sport_bild.save()
pub_auto_bild = Publisher(name="Auto Bild")
pub_auto_bild.save()
pub_computer_bild = Publisher(name="Computer Bild")
pub_computer_bild.save()
pub_musik = Publisher(name="Musikexpress")
pub_musik.save()
pub_rolling = Publisher(name="Rolling Stone")
pub_rolling.save()


topic = Topic(name="Politic")
topic.save()
topic.publishers.add(pub_welt, pub_bz, pub_bild)
topic.save()

topic = Topic(name="Economy")
topic.save()
topic.publishers.add(pub_welt, pub_bz, pub_bild)
topic.save()

topic = Topic(name="Sport")
topic.save()
topic.publishers.add(pub_sport_bild, pub_welt)
topic.save()

topic = Topic(name="Cars")
topic.save()
topic.publishers.add(pub_auto_bild, pub_welt)
topic.save()

topic = Topic(name="Computers")
topic.save()
topic.publishers.add(pub_computer_bild, pub_welt)
topic.save()

topic = Topic(name="Music")
topic.save()
topic.publishers.add(pub_musik, pub_rolling, pub_welt)
topic.save()
