class Article:
    title = ''
    image = ''
    aricle_src = ''

    def __init__(self, title, image, aricle_src):
        self.title = title
        self.image = image
        self.aricle_src = aricle_src

    def get_info (self):
        return "{} | {} | {}".format(self.title, self.image, self.aricle_src)

    def toArray(self):
        return {"title": self.title,
                "aricle_src": self.aricle_src,
                "img_src": self.image}
