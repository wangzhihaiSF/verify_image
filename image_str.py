from aip import AipOcr


def get_file_content(file):
    with open(file, "rb") as f:
        return f.read()


class ImageStr(object):
    def __init__(self):
        self.APP_ID = "15438264"
        self.API_KEY = "Rpl0oPR6NzSVeQ4AuFcaYIFE"
        self.SECRET_KEY = "IC2Rz183pl7qUbKlGQR5fPg6YVOrkY4D"
        self.client = AipOcr(self.APP_ID, self.API_KEY, self.SECRET_KEY)

    def img_to_str(self, image_path):
        image = get_file_content(image_path)
        result = self.client.basicAccurate(image)
        if "words_result" in result:
            return "\n".join([w['words'] for w in result['words_result']])


if __name__ == "__main__":
    base_url = "rtmp://play.8qweda.cn/iev/"
    image_str = ImageStr()
    result1 = image_str.img_to_str("./images/1.png").strip()
    print(result1)
