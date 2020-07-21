from line_notify import LineNotify

#ACCESS_TOKEN = 'TOKEN'
ACCESS_TOKEN = '2bXUH7qIDsnWKOkACnWDTD5OlvYEBJ0umNfjL5jEZh3' #1 to 1
notify = LineNotify(ACCESS_TOKEN)

notify.send('附張照片')
notify.send("合掌村", image_path='./image.jpg')

#ACCESS_TOKEN = 'A29E1yosXT9rKIqMHadrhESoRJK8WT6TE2qqtttd6O4' #1234
