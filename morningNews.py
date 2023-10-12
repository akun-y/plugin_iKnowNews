import json
import time
import requests

#每日60秒早报
#https://www.alapi.cn/api/view/93
#每天获取一次
# 在每天的9点调度函数
def getMorningNewsOnDay():
    url = "https://v2.alapi.cn/api/zaobao"

    payload = "token=cu1HWtIiBHGqu16t&format=json"
    headers = {'Content-Type': "application/x-www-form-urlencoded"}

    response = requests.request("POST", url, data=payload, headers=headers)

    result = json.loads(response.text)
    #print(result)
    print("getMorningNewsOnDay===>")

    news = ""
    count = 1
    for item in result["data"]["news"]:
        news += item + "\n"
        count += 1
        if(count > 6):
            break
    weiyu = result["data"]["weiyu"]
    return news +'\n' +weiyu


#main 全局
newsOfDay = ""
lastDate = 0

def getMorningNews():
    global newsOfDay, lastDate
    
    currentDate = time.strftime("%Y%m%d", time.localtime())
    if newsOfDay=="" or currentDate != lastDate :
        newsOfDay = getMorningNewsOnDay()
        lastDate = time.strftime("%Y%m%d", time.localtime())
        print("getMorningNews最新一次调用时间:"+lastDate)
    
    print("getMorningNews最后一次调用时间:"+lastDate)
    return newsOfDay


def getMorningNews2():
    result = {"code": 200, "msg": "success", "data": {"date": "2023-10-12", "news": ["1、财政部：停止销售“六六顺“等41款即开型福利彩票游戏；", "2、国际最新研究：基因编辑可让鸡获得禽流感抗性，助力减少禽流感传播；最新研究：中国人口初婚推迟速度加快，低学历男性终身不婚率或继续走高；", "3、北京：推行施工图审查等多项改革，优化工程建设领域营商环境；", "4、四川仁寿一中学过滤水池盖板突然塌陷，官方通报：14名学生掉入，目前无大碍；", "5、浙江绍兴：全面放开住房限售，支持满足购房者“以旧换新“、“以小换大“；", "6、网曝“四川广元一出租车高速路甩客致乘客身亡“，媒体调查：女乘客系下高速后溺亡，司机称其执意下车；", "7、潜水员韩颋失联第4天在水 下百余米处被找到，知情人：身体被卡洞里，仍未能打捞出水面；", "8、11日晚，台湾花莲发生5.4级地震，汕头、福州等地网友称有震 感；", "9、日本政客窜访台湾地区，中使馆：坚决反对，已向日方提出严正交涉；", "10、澳籍公民成蕾服刑期满后被依法驱逐出境，原 系境内媒体聘用人员，为境外提供国家秘密，外交部回应：中国司法机关依法审理判决；", "11、外媒：安哥拉对中国公民赴安旅游实行 免签；11日早上，阿富汗西北部再发6.3级地震，此前该区域地震已致4000余人伤亡；", "12、外媒：当地11日，泽连斯基突访北约总部，与北约官员会面要过冬援助；泽连斯基10日表示：担忧巴以冲突恐分散对乌克兰战场注意力；", "13、哈马斯宣布：当地11日下午，对以 色列首都机场发动了大规模火箭弹袭击。暂无人员伤亡的报告；以色列成立紧急联合政府：内塔尼亚胡与反对党领袖甘茨已达成一致；", "14、美国中央司令部：“福特“号航母已抵达地中海东部，进行“威慑“。美或向中东部署第二艘航母，拜登称正对以提供更多军援；", "15、巴以冲突第四天：加沙地带遭遇以军数千炸弹轰击，多座大楼被“夷为平地“，以色列重兵集结加沙边境，或将发动大规模地面进攻。美中情局前局长：巷战会非常残酷。冲突已造成双方近2300死，7000多伤；"], "weiyu": "【微语】一生欢喜不为世俗所及，生活就是一边失去一边拥有，就像我不知道前面的路如何，但我永远都在路上。", "image": "https:\/\/file.alapi.cn\/60s\/202310121697043854.png", "head_image": "https:\/\/file.alapi.cn\/60s\/202310121697043854_head.png"}, "time": 1697091566, "usage": 0, "log_id": "570977175872253952"}

    news = ""
    count = 1
    for item in result["data"]["news"]:
        news += item + "\n"
        count += 1
        if(count > 6):
            break
    weiyu = result["data"]["weiyu"]
    return news +'\n' +weiyu


def get_weather(city_name):
    url = "https://v2.alapi.cn/api/weather/"
    payload = "city=" + city_name
    headers = {'Content-Type': "application/x-www-form-urlencoded"}
    response = requests.request("POST", url, data=payload, headers=headers)
    result = response.json()
    return result


