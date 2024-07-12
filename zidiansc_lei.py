# coding=utf-8
import exrex


class Zidian:
    def __init__(self, url, new_file_name="new_dict.txt", file_name="muben.txt"):
        self.url = url
        self.file_name = file_name
        self.new_file_name = new_file_name

    def get_url(self):
        # 通过split切割出来是一个列表
        url_list = self.url.split(".")

        # 通过拿到url_list的列表长度
        # if len(url_list)
        len(url_list)

        # 永远都切第一位，因为第一位不纯粹有  http://内容
        # 第一位内容：
        new_url_list = []
        if url_list[0] != "http://www":
            new_url_list = [url_list[0].split("://")[-1]]

        for value in url_list:
            if value == url_list[0] or value == url_list[-1]:
                continue
            new_url_list.append(value)

        # 这个是我们处理之后的信息   列表
        return new_url_list

    """
    get_txt_contents
    传入文件名
    返回值是一个列表list
    """

    def get_txt_contents(self):
        with open(f"{self.file_name}", "r") as f:
            # 去除\n换行方法
            dict_list = f.read().splitlines()
        return dict_list

    """
    put_txt_contents
    dict_list是我们原始文件的内容。
    new_url_list是我们的url处理之后的值。
    """
    # self.get_url()  self.get_txt_contents()
    def put_txt_contents(self):
        # image.abc.music.lwz
        with open(f"{self.new_file_name}", "a", newline="") as f:
            for value in self.get_txt_contents():
                # 第一个参数值用range来改变  第二个就是不用刚刚用了个range的值的其他range值
                for i in range(0, len(self.get_url())):
                    for j in range(0, len(self.get_url())):
                        # if i == j:
                        #     continue
                        a = self.get_url()[i]
                        b = self.get_url()[j]
                        dicts = list(exrex.generate(rf"{a}{value}{b}"))
                        f.write(dicts[0] + "\n")
