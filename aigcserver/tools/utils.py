import yaml
import uuid
import datetime
import decimal

# from flask.json import JSONEncoder as BaseJSONEncoder


def load_config(path):
    with open(path, "rt") as file:
        # yaml.full_load(file)
        config = yaml.safe_load(file)
        # config = yaml.load(file, Loader=yaml.Loader)
    return config


# class DoJSONEnCoder(BaseJSONEncoder):
#     def default(self, o):
#         """
#         如有其他的需求可直接在下面添加
#         :param o:
#         :return:
#         """
#         if isinstance(o, datetime.datetime):
#             # 格式化时间
#             return o.strftime("%Y-%m-%d %H:%M:%S")
#         if isinstance(o, datetime.date):
#             # 格式化日期
#             return o.strftime("%Y-%m-%d")
#         if isinstance(o, decimal.Decimal):
#             # 格式化高精度数字
#             return str(o)
#         if isinstance(o, uuid.UUID):
#             # 格式化uuid
#             return str(o)
#         if isinstance(o, bytes):
#             # 格式化字节数据
#             return o.decode("utf-8")
#         return super(BaseJSONEncoder, self).default(o)
