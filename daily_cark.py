from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import random

def create_daily_greeting_card(save_path="daily_greeting.png"):
    # 修改尺寸为手机友好的尺寸 (1080x1920 适合大多数手机屏幕)
    width, height = 1080, 1920
    card = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(card)
    
    # 调整字体大小以适应手机屏幕
    try:
        title_font = ImageFont.truetype("simhei.ttf", 96)
        date_font = ImageFont.truetype("simhei.ttf", 64)
        text_font = ImageFont.truetype("simhei.ttf", 72)
    except:
        title_font = ImageFont.load_default()
        date_font = text_font = ImageFont.load_default()
    
    # 调整边框宽度
    border_width = 40
    draw.rectangle([border_width, border_width, width-border_width, height-border_width], 
                  outline='#FFB6C1', width=5)
    
    # 获取当前日期
    current_date = datetime.now().strftime("%Y年%m月%d日")
    
    # 准备问候语列表
    greetings = [
        "愿今天充满阳光和希望！",
        "祝您今天心情愉快！",
        "新的一天，新的开始！",
        "愿您度过美好的一天！",
        "今天也要加油哦！"
    ]
    
    # 随机选择一条问候语
    greeting = random.choice(greetings)
    
    # 调整文字位置以更好地适应竖屏
    draw.text((width/2, height/4), "每日问候", 
              font=title_font, fill='#FF69B4', anchor="mm")
    
    draw.text((width/2, height/2.5), current_date, 
              font=date_font, fill='#4169E1', anchor="mm")
    
    # 问候语可能较长，所以给它更多空间
    draw.text((width/2, height/2), greeting, 
              font=text_font, fill='#20B2AA', anchor="mm")
    
    # 调整装饰元素的大小和位置
    corner_size = 200
    # 顶部装饰
    draw.arc([50, 50, corner_size, corner_size], 0, 360, fill='#FFB6C1', width=5)
    draw.arc([width-corner_size-50, 50, width-50, corner_size], 0, 360, fill='#FFB6C1', width=5)
    # 底部装饰
    draw.arc([50, height-corner_size-50, corner_size, height-50], 0, 360, fill='#FFB6C1', width=5)
    draw.arc([width-corner_size-50, height-corner_size-50, width-50, height-50], 0, 360, fill='#FFB6C1', width=5)
    
    # 保存图片
    card.save(save_path)
    return save_path

if __name__ == "__main__":
    # 测试函数
    create_daily_greeting_card()
