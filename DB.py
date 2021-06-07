# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 20:54:29 2021

@author: Adham
"""

import sqlite3 as sl

def listToStr(lst):
    string=''
    try:
        for arr in lst:
            for array in arr:
                flag=True
                for element in array:
                    if (flag):
                        string += str(element)
                        flag=False
                    else:
                        string += '&' + str(element)
                string += '#'
            string +='$'
        return string[:-1]
    except:
        try:
            for array in lst:
                flag=True
                for element in array:
                    if (flag):
                        string += str(element)
                        flag=False
                    else:
                        string += '&' + str(element)
                string += '#'
            return string[:-1]
        except:
            flag=True
            for element in lst:
                    if (flag):
                        string += str(element)
                        flag=False
                    else:
                        string += '&' + str(element)
    return string

'''
lst=[[[1.0, 0.05, 5.2555], [12.0, 15.6, 65.0]],[[1.0, 0.05, 5.2555], [12.0, 15.6, 65.0]]]
print(listToStr(lst)) # & sparates elements # separates arrays
'''

def strToList(string):
    arr = list(string.split("$"))
    lists=[]
    for x in arr:
        lists.append(list(x[:-1].split("#")))
    
    for i in range(len(lists)):
        for j in range(len(lists[i])):
            lists[i][j] = list(lists[i][j].split("&"))
            lists[i][j] = [float(i) for i in lists[i][j]]
    
    if(len(lists)==1):
        lists = lists[0]
    if(len(lists)==1):
        lists = lists[0]
    
    return lists
    

'''
string='1.0&0.05&5.2555#12.0&15.6&65.0#$1.0&0.05&5.2555#12.0&15.6&65.0#' # & sparates elements # separates arrays
print((strToList(string)))

lst=[[[1.0, 0.05, 5.2555], [12.0, 15.6, 65.0]],[[1.0, 0.05, 5.2555], [12.0, 15.6, 65.0]]]
print(lst)
print(strToList(listToStr(lst))) # & sparates elements # separates arrays
'''


con = sl.connect('myDB.db')

def buildDB():
    con = sl.connect('myDB.db')
    with con:
        con.execute("""
            CREATE TABLE image (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                path TEXT,
                averageRGB TEXT,
                histogram TEXT,
                layoutHistograms TEXT
            );
        """)
    with con:
        con.execute("""
            CREATE TABLE video (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                path TEXT
                );
        """)
    with con:
        con.execute("""
            CREATE TABLE videoImages (
                video_id INTEGER NOT NULL,
                image_id INTEGER NOT NULL,
                FOREIGN KEY(video_id) REFERENCES video(id),
                FOREIGN KEY(image_id) REFERENCES image(id)
                );
        """)    

# buildDB()

def deleteDB(): 
    import os
    try:
        os.remove("myDB.db")
    except:
        con.close()
        os.remove("myDB.db")
    buildDB()


def clearDB(): 
    # con = sl.connect('myDB.db')
    con.execute("DELETE FROM videoImages")
    con.execute("DELETE FROM video")
    con.execute("DELETE FROM image")
    

def insertImage(path, averageRGB, histogram, layoutHistograms):
    
    sql = 'INSERT INTO image (path, averageRGB, histogram, layoutHistograms) values(?, ?, ?, ?)'
    data = [(path, listToStr(averageRGB), listToStr(histogram), listToStr(layoutHistograms))]
    with con:
        con.executemany(sql, data)
        sql = 'SELECT last_insert_rowid()'
        data = con.execute(sql)
        for i in data:
            image_id = i[0]
    return image_id

def getImages(image_ids=None):
    if(image_ids is None):
        data = con.execute("SELECT * FROM image")
    else:
        sql = "SELECT * FROM image where id in "
        try:
            string='('
            for image_id in image_ids:
                string+=str(image_id)+','
            string=string[:-1]+')'
        except:
            string='('+str(image_ids)+')'
        
        data = con.execute(sql+string)
            
    lst=[]
    for row in data:
        lst.append(row)
    return lst

'''
insertImage('image path', (1,2), [1,2], [1,2])
print(getImages())
print(getImages([1,2]))
'''

def insertVideoImage(video_id, image_id):
    
    sql = 'INSERT INTO videoImages (video_id, image_id) values(?, ?)'
    data = [(video_id, image_id)]
    with con:
        con.executemany(sql, data)

def insertvideo(path, averageRGB, histogram, layoutHistograms):
    sql = 'INSERT INTO video (path) values(?)'
    data = [(path,)]
    with con:
        con.executemany(sql, data)
        sql = 'SELECT last_insert_rowid()'
        data = con.execute(sql)
        for i in data:
            video_id = i[0]
    
    try:
        averageRGB[0][0]
        for i in range (len(averageRGB)):
            image_id = insertImage(0, averageRGB[i], histogram[i], layoutHistograms[i])
            insertVideoImage(video_id, image_id)
    except:
        image_id = insertImage(0, averageRGB, histogram, layoutHistograms)
        insertVideoImage(video_id, image_id)
        
    return

def getKeyFrameVideo(image_id):
    data = con.execute("SELECT * FROM videoImages where image_id = "+str(image_id))
    for row in data:
        data2 = con.execute("SELECT * FROM video where id = "+ str(row[0]))
        for row2 in data2:
            return row2[1]

def getVideos(video_ids=None):
    if(video_ids is None):
        data = con.execute("SELECT * FROM video")
        data2 = con.execute("SELECT * FROM videoImages ORDER BY video_id, image_id")
        videos_images_ids=[]
        for row in data2:
            if(videos_images_ids==[] or videos_images_ids[-1][0] != row[0]):
                videos_images_ids.append((row[0],[row[1]]))
            else:
                videos_images_ids[-1][1].append(row[1])
            
        # print(videos_images_ids)
    else:
        sql = "SELECT * FROM video where id in "
        try:
            string='('
            for video_id in video_ids:
                string+=str(video_id)+','
            string=string[:-1]+')'
        except:
            string='('+str(video_ids)+')'
        
        data = con.execute(sql+string)
        
        data2 = con.execute("SELECT * FROM videoImages where video_id in "+string+" ORDER BY video_id")
        videos_images_ids=[]
        for row in data2:
            if(videos_images_ids==[] or videos_images_ids[-1][0] != row[0]):
                videos_images_ids.append((row[0],[row[1]]))
            else:
                videos_images_ids[-1][1].append(row[1])
            
        # print(videos_images_ids)
    
    videos=[]
    i=0
    for row in data:
        frames=[]
        for image_id in videos_images_ids[i][1]:
                frames.append(getImages(image_id)[0])
        videos.append((row[0],row[1],frames))
        i+=1
    return videos

'''
insertvideo('video path', [(5,6),(7,8)], [[5,6],[7,8]], [[5,6],[7,8]]) #2 frames video
insertvideo('video path', (9,10), [9,10], [9,10]) #1 frame video
print(getVideos())
print(getImages())
'''

#########

'''
import os
os.remove("myDB.db")
con = sl.connect('myDB.db')
with con:
    con.execute("""
        CREATE TABLE image (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            path TEXT,
            averageRGB TEXT,
            histogram TEXT,
            layoutHistograms TEXT
        );
    """)
with con:
    con.execute("""
        CREATE TABLE video (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            path TEXT
            );
    """)
with con:
    con.execute("""
        CREATE TABLE videoImages (
            video_id INTEGER NOT NULL,
            image_id INTEGER NOT NULL,
            FOREIGN KEY(video_id) REFERENCES video(id),
            FOREIGN KEY(image_id) REFERENCES image(id)
            );
    """)    


# insert and retrieve from and into image 
sql = 'INSERT INTO image (path, histogram, layoutHistograms) values(?, ?, ?)'
data = [
    ('path1', 2, listToStr([2,5,6])),
    ('path2', 22, 22),
    ('path3', 23, 22)
]

with con:
    con.executemany(sql, data)
    
    data = con.execute("SELECT * FROM image")#" WHERE age <= 22")
    for row in data:
        print(row)


# insert into and retrieve from video
sql = 'INSERT INTO video (path) values (\'path5\')'
with con:
    con.execute(sql)
    data = con.execute("SELECT * FROM video")#" WHERE age <= 22")
    for row in data:
        print(row)



# insert into and retrieve from videoImages
sql = 'INSERT INTO videoImages (video_id, image_id) values(?, ?)'
data = [
    (1,1),
    (1,2),
    (1,3)
]
with con:
    con.executemany(sql, data)
    data = con.execute("SELECT * FROM videoImages")#" WHERE age <= 22")
    for row in data:
        print(row)


# printing videoImages
sql = 'SELECT * FROM videoImages'
with con:
    data = con.execute(sql)
for row in data:
    print(row)


con.close()
'''
