# encoding:utf-8

from plugins.plugin_iKnowNews.morningNews import getMorningNews
import plugins
from bridge.context import ContextType
from bridge.reply import Reply, ReplyType
from channel.chat_message import ChatMessage
from common.log import logger
from plugins import *


@plugins.register(
    name="iKnowNews",
    desire_priority=100,
    hidden=False,
    desc="一个获取最新新闻的插件",
    version="0.5",
    author="akun.yunqi",
)
class iNews(Plugin):
    def __init__(self):
        super().__init__()
        self.handlers[Event.ON_HANDLE_CONTEXT] = self.on_handle_context
    
        self.config = super().load_config()
        if not self.config:
            # 未加载到配置，使用模板中的配置
            self.config = self._load_config_template()
        if self.config:
            self.alapi_token = self.config.get("alapi_token")
        
        logger.info(f"[iKnowNews] inited, config={self.config}")

    def on_handle_context(self, e_context: EventContext):
        if e_context["context"].type not in [
            ContextType.TEXT,
            ContextType.JOIN_GROUP,
            ContextType.PATPAT,
        ]:
            return

        if e_context["context"].type == ContextType.JOIN_GROUP:
            e_context["context"].type = ContextType.TEXT
            msg: ChatMessage = e_context["context"]["msg"]
            e_context["context"].content = f'请你随机使用一种风格说一句问候语来欢迎新用户"{msg.actual_user_nickname}"加入群聊。'
            e_context.action = EventAction.BREAK  # 事件结束，进入默认处理逻辑
            return

        if e_context["context"].type == ContextType.PATPAT:
            e_context["context"].type = ContextType.TEXT
            msg: ChatMessage = e_context["context"]["msg"]
            e_context["context"].content = f"请你随机使用一种风格介绍你自己，并告诉用户输入#help可以查看帮助信息。"
            e_context.action = EventAction.BREAK  # 事件结束，进入默认处理逻辑
            return

        content = e_context["context"].content
        logger.debug("[Hello] on_handle_context. content: %s" % content)
    
        if content == "inews" or content.startswith("$inews"):
            reply = Reply()
            reply.type = ReplyType.TEXT
            msg: ChatMessage = e_context["context"]["msg"]
            morningNews = getMorningNews(self.alapi_token)
            if e_context["context"]["isgroup"]:
                reply.content = f"{morningNews}"
            else:
                reply.content = f"{morningNews}"
            e_context["reply"] = reply
            e_context.action = EventAction.BREAK_PASS

    def get_help_text(self, **kwargs):
        help_text = "输入$inews，我会回复你最新新闻\n"
        return help_text
