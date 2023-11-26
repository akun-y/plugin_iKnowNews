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
            self.group_welcome_msg = self.config.get("group_welcome_msg")
            self.group_paipai_msg = self.config.get("group_paipai_msg")
        
        logger.info(f"[iKnowNews] inited, config={self.config}")

    def _get_group_welcome_msg(self, user_name):
        #return self.group_welcome_msg.format(用户名称=user_name)
        return self.group_welcome_msg
    def on_handle_context(self, e_context: EventContext):
        if e_context["context"].type not in [
            ContextType.TEXT,
            ContextType.JOIN_GROUP,
            ContextType.PATPAT,
        ]:
            return

        if e_context["context"].type == ContextType.JOIN_GROUP:
            reply = Reply()
            reply.type = ReplyType.TEXT
            msg: ChatMessage = e_context["context"]["msg"]
            reply.content = self._get_group_welcome_msg('akun')
            e_context["reply"] = reply
            e_context.action = EventAction.BREAK_PASS
            return

        if e_context["context"].type == ContextType.PATPAT:
            e_context["context"].type = ContextType.TEXT
            msg: ChatMessage = e_context["context"]["msg"]
            e_context["context"].content = f"请你随机使用一种风格介绍你自己,介绍素材从如下内容中选择:徐医生门诊时间：普通门诊：周四、周五下午(门诊北楼1楼）;代谢性疾病早期恢复与干预特需门诊：周二、周六上午(门诊北楼1楼）;自然位疗法，由徐子军医生专利技术发展而来，为上海市优秀发明奖、医学科技奖专利技术，是一种非药物的健康干预方法，分阶段科学指导营养摄入、科学运动和睡眠促进身体的自然恢复和健康。这种方法强调自然、安全和无痛，适合各种年龄和身体状况的人群。自然位疗法包括多种技术，如呼吸训练、体态调整、代谢及肌功能矫正、脊柱整复等，可以帮助人们放松身体、增强身体柔韧性和平衡性，以及提高身体免疫力及代谢。自然位疗法不仅可以用于治疗身体疾病，还可以用于预防疾病和维护健康。"
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
                reply.content = f"\n{morningNews}"
            else:
                reply.content = f"\n{morningNews}"
            e_context["reply"] = reply
            e_context.action = EventAction.BREAK_PASS
            return

    def get_help_text(self, **kwargs):
        help_text = "输入$inews，我会回复你最新新闻\n"
        return help_text
