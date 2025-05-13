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

    print("\nHTTP状态码:", resp.status_code)
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

get_live_status(1888621682) #孤胆骑手小李

get_live_status(46462447) #唐牛故事会

get_live_status(375450192) #在花777

get_live_status(1553366630) #地上足球直播号


# resp.text[:1000]的JSON如下
# {
#   "code": 0,
#   "msg": "success",
#   "message": "success",
#   "data": {
#     "2071691173": {
#       "title": "【预告】14日17点 TE vs ZETA",
#       "room_id": 22908869,
#       "uid": 2071691173,
#       "online": 22774,
#       "live_time": 1731912337,
#       "live_status": 1,
#       "short_id": 0,
#       "area": 12,
#       "area_name": "手游直播",
#       "area_v2_id": 561,
#       "area_v2_name": "游戏赛事",
#       "area_v2_parent_name": "赛事",
#       "area_v2_parent_id": 13,
#       "uname": "无畏契约赛事",
#       "face": "https://i1.hdslb.com/bfs/face/44ca2be4d17a8c7cd545fdc933808811151e20eb.jpg",
#       "tag_name": "王者荣耀,碧蓝航线,崩坏3,阴阳师,Fate/GO,少女前线,ICHU,狼人杀,荒野行动,决战！平安京",
#       "tags": "无畏契约赛事,瓦罗兰特赛事,东京大师赛,VCT,VCTCN,CQ,全球冠军赛",
#       "cover_from_user": "https://i0.hdslb.com/bfs/live/def922b162b3685b6957722f34ca34ba7c1fdc53.jpg",
#       "keyframe": "https://i0.hdslb.com/bfs/live-key-frame/keyframe05140032000022908869xeco0v.jpg",
#       "lock_till": "0000-00-00 00:00:00",
#       "hidden_till": "0000-00-00 00:00:00",
#       "broadcast_type": 0
#     }
#   }
# }
