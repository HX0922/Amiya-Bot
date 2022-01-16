import abc
import json

from typing import Union


class WSOpration:
    @abc.abstractmethod
    async def connect_websocket(self):
        """
        建立连接
        :return:
        """
        pass

    @abc.abstractmethod
    async def send(self, reply):
        """
        发送消息的方式，传入 Chain 对象
        :param reply: Chain 对象
        :return:
        """
        pass


def response(data: Union[str, int, float, bool, dict, list] = None,
             code: int = 200,
             message: str = ''):
    """
    HTTP 请求的响应体

    :param data:    响应的数据
    :param code:    响应码
    :param message: 响应消息
    :return:
    """
    return json.dumps({
        'data': data,
        'code': code,
        'message': message
    }, ensure_ascii=False)