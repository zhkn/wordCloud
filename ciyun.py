import jieba
import wordcloud
from PIL import Image
import numpy as np

c = wordcloud.WordCloud(
    background_color="white", 
    collocations=False,
    font_path="fonts/msyh.ttf", 
    max_font_size=60,
    mask=np.array(Image.open("map.png")))
with open('data.txt', 'r') as f:
    c.generate(" ".join(jieba.lcut(f.read()))).to_file("wordCloud_map.png")