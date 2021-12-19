import requests, json

V = "5.131"
DOMAIN = "https://api.vk.com/method/"
VKURL = "{DOMAIN}{METHOD_NAME}?{PARAMETERS}&access_token={ACCESS_TOKEN}&v={V}"
ACCESS_TOKEN = "5225fcc35756b681f39a5f8666851ca3639692744092fe64f2623d666e350ea385644d98befff2cd01ba5"

message = """🥰Друзья, нажмите кнопку ❤
👪Вам не трудно - а именинникам приятно)))

🎉Сегодня День рождения отмечают:
{ids}"""

def newAlbum():
    url = VKURL.format(
        DOMAIN=DOMAIN,
        METHOD_NAME="photos.createAlbum",
        PARAMETERS=f"title=Jams&description=Jams",
        ACCESS_TOKEN=ACCESS_TOKEN,
        V=V)
    response = requests.get(url)

def uploadImage():
    url = VKURL.format(
        DOMAIN=DOMAIN,
        METHOD_NAME="photos.getUploadServer",
        PARAMETERS=f"album_id=282121824&group_id=208480690",
        ACCESS_TOKEN=ACCESS_TOKEN,
        V=V)
    response = requests.get(url)
    upload_server = response.json()['response']['upload_url']

    files = {'file1': open('static/img.jpg','rb')}
    response = requests.post(upload_server, files=files)
    response = response.json()
    img_hash = response['hash']
    photos_list = response['photos_list']
    server = response['server']

    url = VKURL.format(
        DOMAIN=DOMAIN,
        METHOD_NAME="photos.save",
        PARAMETERS=f"album_id=282121824&group_id=208480690&server={server}&photos_list={photos_list}&hash={img_hash}",
        ACCESS_TOKEN=ACCESS_TOKEN,
        V=V)
    response = requests.get(url)
    response = response.json()
    data = (response["response"][0]["id"], response["response"][0]["owner_id"])
    return data

def sendPost(ids, group_id):
    id, owner_id = uploadImage()
    url = VKURL.format(
        DOMAIN=DOMAIN,
        METHOD_NAME="wall.post",
        PARAMETERS=f"owner_id={group_id}&message={message.format(ids=ids)}&attachments=photo{owner_id}_{id}",
        ACCESS_TOKEN=ACCESS_TOKEN,
        V=V)
    response = requests.get(url)
    print(response.json(), group_id)

def getId(group):
    url = VKURL.format(
        DOMAIN=DOMAIN,
        METHOD_NAME="groups.getById",
        PARAMETERS=f"group_id={group.split('/')[-1]}",
        ACCESS_TOKEN=ACCESS_TOKEN,
        V=V)
    response = requests.get(url)
    return f"-{response.json()['response'][0]['id']}"

if __name__ == '__main__':
    pass
    # sendPost("*id5966400 (Алексей Демин), *id6606805 (Ирина Бабушкина), *id8008478 (Мишаня Дмитриев)", getId("https://vk.com/testsustem"))
    # print(getId("https://vk.com/testsustem"))
