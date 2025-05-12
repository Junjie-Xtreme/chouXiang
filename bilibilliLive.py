import requests
import time

# 计算直播时长的函数
def get_live_duration(live_timestamp):
    duration = int(time.time()) - live_timestamp
    hours = duration // 3600
    minutes = (duration % 3600) // 60
    return f"{hours}小时 {minutes}分钟"

# B站API获取JSON 提取开播状态、标题、开播时长
def get_live_status(uid):
    url = f'https://api.live.bilibili.com/room/v1/Room/get_status_info_by_uids?uids[]={uid}'
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    resp = requests.get(url, headers=headers)

    print("HTTP状态码:", resp.status_code)
    print("原始响应:", resp.text[:1000])  # 截取前1000字符

    try:
        data = resp.json()
    except Exception as e:
        print("⚠️ 无法解析 JSON 响应:", e)
        return

    if data['code'] == 0:
        user_info = data['data'].get(str(uid))
        if user_info:
            status = user_info['live_status']
            name = user_info['uname']
            if status == 1:
                live_duration = get_live_duration(user_info['live_time'])
                print(f"🟢 {name} （{uid} 正在直播：《{user_info['title']}》｜ 已直播：{live_duration}）")
            else:
                print(f"🔴 {name} 没有开播")
        else:
            print("⚠️ 响应中没有该用户的数据")
    else:
        print("⚠️ API 响应错误:", data)


# 查询UID为 12345678（比如某位主播）
get_live_status(518103295) #石林爱打斧

get_live_status(2071691173)#无畏契约赛事

get_live_status(107034991) #抽象的唐彦祖

get_live_status(245040602) #叫我眼神丶

get_live_status(32731291) #Lisa的嘴

get_live_status(36805011) #滴滴滴-滴滴滴是大白

