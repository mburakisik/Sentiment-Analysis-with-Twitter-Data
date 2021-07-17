# Gerekli kütüphanelerin içe aktarılması
import pandas as pd
import numpy as np
import re

# Veri ön işleme için fonksiyon
def temizle(data, col_name, hastag=True, url=True, rt=True, mention=True, emoji=True, digit=True, punct=True, stopword=True, stopwords_list=[]):

    lower = str.maketrans("ABCÇDEFGĞHIİJKLMNOÖPQRŞSTUÜVWXYZ", "abcçdefgğhıijklmnoöpqrşstuüvwxyz")

    #Tweet'in küçültülmesi
    data[col_name] = data[col_name].apply(lambda x: str(x).translate(lower))

    #"\n" ve "\t" nin kaldırılması
    data[col_name] = data[col_name].apply(lambda x: x.replace("\n"," "))

    data[col_name] = data[col_name].apply(lambda x: x.replace("\t"," "))

    #Hashtag'in kaldırılması
    if hastag == True: data[col_name] = data[col_name].apply(lambda x: x.replace("#",""))

    #Url'nin kaldırılması
    if url == True: data[col_name] = data[col_name].apply(lambda x: re.sub(r"http\S+","", x))

    #Rt'lerin kaldırılması
    if rt == True: data[col_name] = data[col_name].apply(lambda x: " ".join([i for i in x.split() if i!= "rt"]))

    #Mention'ların kaldırılması
    if mention == True: data[col_name] = data[col_name].apply(lambda x: re.sub(r"@\S+","", x))

    #Emoji'lerin kaldırılması
    if emoji == True:

        emoji_pattern = re.compile("["
                            u"\U0001F600-\U0001F64F"  # emoticons
                            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                            u"\U0001F680-\U0001F6FF"  # transport & map symbols
                            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            u"\U00002702-\U000027B0"
                            u"\U000024C2-\U0001F251"
                            "]+", flags=re.UNICODE)

        data[col_name] = data[col_name].apply(lambda x: emoji_pattern.sub(r"", x))

    #Sayıların kaldırılması
    if digit == True: data[col_name] = data[col_name].str.replace("\d","")

    #Noktalama işaretlerinin kaldırılması
    if punct == True:

        #Remove " ' "
        data[col_name] = data[col_name].apply(lambda x: x.replace("'",""))

        #Remove other punct
        data[col_name] = data[col_name].str.replace("[^\w\s]"," ")


    #Stopword'lerin kaldırılması
    if stopword == True:

        #Varsayılan Stopword'lerin listesi
        if stopwords_list == []:


            stopwords_list=["acaba",  "aslında", "az", "bazı", "belki", "biri", "birkaç", "birşey", "biz", "bu",
                            "çünkü", "da", "daha", "de", "defa", "diye", "eğer", "en", "gibi", "hem", "her",
                            "için", "ile", "ise", "kez", "ki", "kim", "mı", "mu", "mü", "nasıl", "ne", "neden", "nerde", "nerede",
                            "nereye", "niçin", "niye", "o", "sanki", "şey", "siz", "şu", "tüm", "ve", "veya", "ya", "yani"]

        for cou,tweet in enumerate(data[col_name]):

            data[col_name][cou]=" ".join([word for word in tweet.split() if not word in stopwords_list])

    data[col_name] = data[col_name].apply(lambda x: x.strip())

    return data

data = pd.read_excel("kirli_veri.xlsx",index_col=0)

data = temizle(data,"tweet")

data.to_excel("temizlenmis_veri.xlsx")
