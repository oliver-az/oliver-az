 
 ​from​ __future__ ​import​ ​unicode_literals 
 ​import​ ​asyncio 
 ​import​ ​math 
 ​import​ ​os 
 ​import​ ​time 
 ​import​ ​aiofiles 
 ​import​ ​aiohttp 
 ​import​ ​wget 
 ​from​ ​pyrogram​ ​import​ ​Client​, ​filters 
 ​from​ ​pyrogram​.​errors​ ​import​ ​FloodWait​, ​MessageNotModified 
 ​from​ ​pyrogram​.​types​ ​import​ ​Message 
 ​from​ ​youtubesearchpython​ ​import​ ​SearchVideos 
 ​from​ ​yt_dlp​ ​import​ ​YoutubeDL 
 ​from​ ​config​ ​import​ ​HNDLR 
 ​@​Client​.​on_message​(​filters​.​command​([​"تحميل"​, ​"تنزيل"​], ​prefixes​=​f"​{​HNDLR​}​"​)) 
 ​async​ ​def​ ​song​(​client​, ​message​: ​Message​): 
 ​    ​urlissed​ ​=​ ​get_text​(​message​) 
 ​    ​if​ ​not​ ​urlissed​: 
 ​        ​await​ ​client​.​send_message​(            ​message​.​chat​.​id​,            ​"صيغة الأمر غير صالحة!"​,        ) 
 ​        ​return 
 ​    ​pablo​ ​=​ ​await​ ​client​.​send_message​(​message​.​chat​.​id​, ​f"**🔎 جاري تحميل ** `​{​urlissed​}​`"​) 
 ​    ​search​ ​=​ ​SearchVideos​(​f"​{​urlissed​}​"​, ​offset​=​1​, ​mode​=​"dict"​, ​max_results​=​1​) 
 ​    ​mi​ ​=​ ​search​.​result​() 
 ​    ​mio​ ​=​ ​mi​[​"search_result"​] 
 ​    ​mo​ ​=​ ​mio​[​0​][​"link"​] 
 ​    ​mio​[​0​][​"duration"​] 
 ​    ​thum​ ​=​ ​mio​[​0​][​"title"​] 
 ​    ​fridayz​ ​=​ ​mio​[​0​][​"id"​] 
 ​    ​mio​[​0​][​"channel"​] 
 ​    ​kekme​ ​=​ ​f"https://img.youtube.com/vi/​{​fridayz​}​/hqdefault.jpg" 
 ​    ​await​ ​asyncio​.​sleep​(​0.6​) 
 ​    ​sedlyf​ ​=​ ​wget​.​download​(​kekme​) 
 ​    ​opts​ ​=​ {        ​"format"​: ​"bestaudio"​,        ​"addmetadata"​: ​True​,        ​"key"​: ​"FFmpegMetadata"​,        ​"writethumbnail"​: ​True​,        ​"prefer_ffmpeg"​: ​True​,        ​"geo_bypass"​: ​True​,        ​"nocheckcertificate"​: ​True​,        ​"postprocessors"​: [            {                ​"key"​: ​"FFmpegExtractAudio"​,                ​"preferredcodec"​: ​"mp3"​,                ​"preferredquality"​: ​"720"​,            }        ],        ​"outtmpl"​: ​"%(id)s.mp3"​,        ​"quiet"​: ​True​,        ​"logtostderr"​: ​False​,    } 
 ​    ​try​: 
 ​        ​with​ ​YoutubeDL​(​opts​) ​as​ ​ytdl​: 
 ​            ​ytdl_data​ ​=​ ​ytdl​.​extract_info​(​mo​, ​download​=​True​) 
 ​    ​except​ ​Exception​ ​as​ ​e​: 
 ​        ​await​ ​pablo​.​edit​(​f"**هناك خطأ ** ​\n​**الخطأ هو  :** `​{​str​(​e​)​}​`"​) 
 ​        ​return 
 ​    ​c_time​ ​=​ ​time​.​time​() 
 ​    ​capy​ ​=​ ​f""" 
 ​**🏷️ اسم الاغنيه :** [​{​thum​}​](​{​mo​}​) 
 ​**🎧 طلب من :** ​{​message​.​from_user​.​mention​} 
 ​""" 
 ​    ​file_stark​ ​=​ ​f"​{​ytdl_data​[​'id'​]​}​.mp3" 
 ​    ​await​ ​client​.​send_audio​(        ​message​.​chat​.​id​,        ​audio​=​open​(​file_stark​, ​"rb"​),        ​duration​=​int​(​ytdl_data​[​"duration"​]),        ​title​=​str​(​ytdl_data​[​"title"​]),        ​performer​=​str​(​ytdl_data​[​"uploader"​]),        ​thumb​=​sedlyf​,        ​caption​=​capy​,        ​progress​=​progress​,        ​progress_args​=​(            ​pablo​,            ​c_time​,            ​f"**📥 تحميل** `​{​urlissed​}​`"​,            ​file_stark​,        ),    ) 
 ​    ​await​ ​pablo​.​delete​() 
 ​    ​for​ ​files​ ​in​ (​sedlyf​, ​file_stark​): 
 ​        ​if​ ​files​ ​and​ ​os​.​path​.​exists​(​files​): 
 ​            ​os​.​remove​(​files​) 
 ​def​ ​get_text​(​message​: ​Message​) ​->​ [​None​, ​str​]: 
 ​    ​text_to_return​ ​=​ ​message​.​text 
 ​    ​if​ ​message​.​text​ ​is​ ​None​: 
 ​        ​return​ ​None 
 ​    ​if​ ​" "​ ​not​ ​in​ ​text_to_return​: 
 ​        ​return​ ​None 
 ​    ​try​: 
 ​        ​return​ ​message​.​text​.​split​(​None​, ​1​)[​1​] 
 ​    ​except​ ​IndexError​: 
 ​        ​return​ ​None 
 ​def​ ​humanbytes​(​size​): 
 ​    ​if​ ​not​ ​size​: 
 ​        ​return​ ​"" 
 ​    ​power​ ​=​ ​2​ ​**​ ​10 
 ​    ​raised_to_pow​ ​=​ ​0 
 ​    ​dict_power_n​ ​=​ {​0​: ​""​, ​1​: ​"Ki"​, ​2​: ​"Mi"​, ​3​: ​"Gi"​, ​4​: ​"Ti"​} 
 ​    ​while​ ​size​ ​>​ ​power​: 
 ​        ​size​ ​/=​ ​power 
 ​        ​raised_to_pow​ ​+=​ ​1 
 ​    ​return​ ​str​(​round​(​size​, ​2​)) ​+​ ​" "​ ​+​ ​dict_power_n​[​raised_to_pow​] ​+​ ​"B" 
  
 ​async​ ​def​ ​progress​(​current​, ​total​, ​message​, ​start​, ​type_of_ps​, ​file_name​=​None​): 
 ​    ​now​ ​=​ ​time​.​time​() 
 ​    ​diff​ ​=​ ​now​ ​-​ ​start 
 ​    ​if​ ​round​(​diff​ ​%​ ​10.00​) ​==​ ​0​ ​or​ ​current​ ​==​ ​total​: 
 ​        ​percentage​ ​=​ ​current​ ​*​ ​100​ ​/​ ​total 
 ​        ​speed​ ​=​ ​current​ ​/​ ​diff 
 ​        ​elapsed_time​ ​=​ ​round​(​diff​) ​*​ ​1000 
 ​        ​if​ ​elapsed_time​ ​==​ ​0​: 
 ​            ​return 
 ​        ​time_to_completion​ ​=​ ​round​((​total​ ​-​ ​current​) ​/​ ​speed​) ​*​ ​1000 
 ​        ​estimated_total_time​ ​=​ ​elapsed_time​ ​+​ ​time_to_completion 
 ​        ​progress_str​ ​=​ ​"{0}{1} {2}%​\n​"​.​format​(            ​""​.​join​(​"🔴"​ ​for​ ​i​ ​in​ ​range​(​math​.​floor​(​percentage​ ​/​ ​10​))),            ​""​.​join​(​"🔘"​ ​for​ ​i​ ​in​ ​range​(​10​ ​-​ ​math​.​floor​(​percentage​ ​/​ ​10​))),            ​round​(​percentage​, ​2​),        ) 
  
 ​        ​tmp​ ​=​ ​progress_str​ ​+​ ​"{0} of {1}​\n​ETA: {2}"​.​format​(            ​humanbytes​(​current​), ​humanbytes​(​total​), ​time_formatter​(​estimated_total_time​)        ) 
 ​        ​if​ ​file_name​: 
 ​            ​try​: 
 ​                ​await​ ​message​.​edit​(                    ​"{}​\n​**اسم الفايل:** `{}`​\n​{}"​.​format​(​type_of_ps​, ​file_name​, ​tmp​)                ) 
 ​            ​except​ ​FloodWait​ ​as​ ​e​: 
 ​                ​await​ ​asyncio​.​sleep​(​e​.​x​) 
 ​            ​except​ ​MessageNotModified​: 
 ​                ​pass 
 ​        ​else​: 
 ​            ​try​: 
 ​                ​await​ ​message​.​edit​(​"{}​\n​{}"​.​format​(​type_of_ps​, ​tmp​)) 
 ​            ​except​ ​FloodWait​ ​as​ ​e​: 
 ​                ​await​ ​asyncio​.​sleep​(​e​.​x​) 
 ​            ​except​ ​MessageNotModified​: 
 ​                ​pass 
 ​def​ ​get_user​(​message​: ​Message​, ​text​: ​str​) ​->​ [​int​, ​str​, ​None​]: 
 ​    ​asplit​ ​=​ ​None​ ​if​ ​text​ ​is​ ​None​ ​else​ ​text​.​split​(​" "​, ​1​) 
 ​    ​user_s​ ​=​ ​None 
 ​    ​reason_​ ​=​ ​None 
 ​    ​if​ ​message​.​reply_to_message​: 
 ​        ​user_s​ ​=​ ​message​.​reply_to_message​.​from_user​.​id 
 ​        ​reason_​ ​=​ ​text​ ​or​ ​None 
 ​    ​elif​ ​asplit​ ​is​ ​None​: 
 ​        ​return​ ​None​, ​None 
 ​    ​elif​ ​len​(​asplit​[​0​]) ​>​ ​0​: 
 ​        ​user_s​ ​=​ ​int​(​asplit​[​0​]) ​if​ ​asplit​[​0​].​isdigit​() ​else​ ​asplit​[​0​] 
 ​        ​if​ ​len​(​asplit​) ​==​ ​2​: 
 ​            ​reason_​ ​=​ ​asplit​[​1​] 
 ​    ​return​ ​user_s​, ​reason_ 
 ​def​ ​get_readable_time​(​seconds​: ​int​) ​->​ ​int​: 
 ​    ​count​ ​=​ ​0 
 ​    ​ping_time​ ​=​ ​"" 
 ​    ​time_list​ ​=​ [] 
 ​    ​time_suffix_list​ ​=​ [​"s"​, ​"m"​, ​"h"​, ​"days"​] 
 ​    ​while​ ​count​ ​<​ ​4​: 
 ​        ​count​ ​+=​ ​1 
 ​        ​remainder​, ​result​ ​=​ ​divmod​(​seconds​, ​60​) ​if​ ​count​ ​<​ ​3​ ​else​ ​divmod​(​seconds​, ​24​) 
 ​        ​if​ ​seconds​ ​==​ ​0​ ​and​ ​remainder​ ​==​ ​0​: 
 ​            ​break 
 ​        ​time_list​.​append​(​int​(​result​)) 
 ​        ​seconds​ ​=​ ​int​(​remainder​) 
 ​    ​for​ ​x​ ​in​ ​range​(​len​(​time_list​)): 
 ​        ​time_list​[​x​] ​=​ ​str​(​time_list​[​x​]) ​+​ ​time_suffix_list​[​x​] 
 ​    ​if​ ​len​(​time_list​) ​==​ ​4​: 
 ​        ​ping_time​ ​+=​ ​time_list​.​pop​() ​+​ ​", " 
 ​    ​time_list​.​reverse​() 
 ​    ​ping_time​ ​+=​ ​":"​.​join​(​time_list​) 
 ​    ​return​ ​ping_time 
 ​def​ ​time_formatter​(​milliseconds​: ​int​) ​->​ ​str​: 
 ​    ​seconds​, ​milliseconds​ ​=​ ​divmod​(​int​(​milliseconds​), ​1000​) 
 ​    ​minutes​, ​seconds​ ​=​ ​divmod​(​seconds​, ​60​) 
 ​    ​hours​, ​minutes​ ​=​ ​divmod​(​minutes​, ​60​) 
 ​    ​days​, ​hours​ ​=​ ​divmod​(​hours​, ​24​) 
 ​    ​tmp​ ​=​ (        ((​str​(​days​) ​+​ ​" يوم(s), "​) ​if​ ​days​ ​else​ ​""​)        ​+​ ((​str​(​hours​) ​+​ ​" ساعه(s), "​) ​if​ ​hours​ ​else​ ​""​)        ​+​ ((​str​(​minutes​) ​+​ ​" دقائق(s), "​) ​if​ ​minutes​ ​else​ ​""​)        ​+​ ((​str​(​seconds​) ​+​ ​" ثواني(s), "​) ​if​ ​seconds​ ​else​ ​""​)        ​+​ ((​str​(​milliseconds​) ​+​ ​" ميل ثانيه(s), "​) ​if​ ​milliseconds​ ​else​ ​""​)    ) 
 ​    ​return​ ​tmp​[:​-​2​] 
 ​def​ ​get_file_extension_from_url​(​url​): 
 ​    ​url_path​ ​=​ ​urlparse​(​url​).​path 
 ​    ​basename​ ​=​ ​os​.​path​.​basename​(​url_path​) 
 ​    ​return​ ​basename​.​split​(​"."​)[​-​1​] 
 ​async​ ​def​ ​download_song​(​url​): 
 ​    ​song_name​ ​=​ ​f"​{​randint​(​6969​, ​6999​)​}​.mp3" 
 ​    ​async​ ​with​ ​aiohttp​.​ClientSession​() ​as​ ​session​: 
 ​        ​async​ ​with​ ​session​.​get​(​url​) ​as​ ​resp​: 
 ​            ​if​ ​resp​.​status​ ​==​ ​200​: 
 ​                ​f​ ​=​ ​await​ ​aiofiles​.​open​(​song_name​, ​mode​=​"wb"​) 
 ​                ​await​ ​f​.​write​(​await​ ​resp​.​read​()) 
 ​                ​await​ ​f​.​close​() 
 ​    ​return​ ​song_name 
  
 ​is_downloading​ ​=​ ​False 
 ​def​ ​time_to_seconds​(​time​): 
 ​    ​stringt​ ​=​ ​str​(​time​) 
 ​    ​return​ ​sum​(​int​(​x​) ​*​ ​60​ ​**​ ​i​ ​for​ ​i​, ​x​ ​in​ ​enumerate​(​reversed​(​stringt​.​split​(​":"​)))) 
 ​@​Client​.​on_message​(​filters​.​command​([​"تنزيل_فيديو"​, ​"تحميل_فيديو"​], ​prefixes​=​f"​{​HNDLR​}​"​)) 
 ​async​ ​def​ ​vsong​(​client​, ​message​: ​Message​): 
 ​    ​urlissed​ ​=​ ​get_text​(​message​) 
  
 ​    ​pablo​ ​=​ ​await​ ​client​.​send_message​(​message​.​chat​.​id​, ​f"**🔎 يبحث عن** `​{​urlissed​}​`"​) 
 ​    ​if​ ​not​ ​urlissed​: 
 ​        ​await​ ​pablo​.​edit​(            ​"صيغة الأمر غير صالحة!"​        ) 
 ​        ​return 
  
 ​    ​search​ ​=​ ​SearchVideos​(​f"​{​urlissed​}​"​, ​offset​=​1​, ​mode​=​"dict"​, ​max_results​=​1​) 
 ​    ​mi​ ​=​ ​search​.​result​() 
 ​    ​mio​ ​=​ ​mi​[​"search_result"​] 
 ​    ​mo​ ​=​ ​mio​[​0​][​"link"​] 
 ​    ​thum​ ​=​ ​mio​[​0​][​"title"​] 
 ​    ​fridayz​ ​=​ ​mio​[​0​][​"id"​] 
 ​    ​mio​[​0​][​"channel"​] 
 ​    ​kekme​ ​=​ ​f"https://img.youtube.com/vi/​{​fridayz​}​/hqdefault.jpg" 
 ​    ​await​ ​asyncio​.​sleep​(​0.6​) 
 ​    ​url​ ​=​ ​mo 
 ​    ​sedlyf​ ​=​ ​wget​.​download​(​kekme​) 
 ​    ​opts​ ​=​ {        ​"format"​: ​"best"​,        ​"addmetadata"​: ​True​,        ​"key"​: ​"FFmpegMetadata"​,        ​"prefer_ffmpeg"​: ​True​,        ​"geo_bypass"​: ​True​,        ​"nocheckcertificate"​: ​True​,        ​"postprocessors"​: [{​"key"​: ​"FFmpegVideoConvertor"​, ​"preferedformat"​: ​"mp4"​}],        ​"outtmpl"​: ​"%(id)s.mp4"​,        ​"logtostderr"​: ​False​,        ​"quiet"​: ​True​,    } 
 ​    ​try​: 
 ​        ​with​ ​YoutubeDL​(​opts​) ​as​ ​ytdl​: 
 ​            ​ytdl_data​ ​=​ ​ytdl​.​extract_info​(​url​, ​download​=​True​) 
 ​    ​except​ ​Exception​ ​as​ ​e​: 
 ​        ​await​ ​event​.​edit​(​event​, ​f"**التحميل فشل** ​\n​ `​{​str​(​e​)​}​`"​) 
 ​        ​return 
 ​    ​c_time​ ​=​ ​time​.​time​() 
 ​    ​file_stark​ ​=​ ​f"​{​ytdl_data​[​'id'​]​}​.mp4" 
 ​    ​capy​ ​=​ ​f""" 
 ​**🏷️ اسم الفيديو :** [​{​thum​}​](​{​mo​}​) 
 ​**🎧 طلب من :** ​{​message​.​from_user​.​mention​} 
 ​""" 
 ​    ​await​ ​client​.​send_video​(        ​message​.​chat​.​id​,        ​video​=​open​(​file_stark​, ​"rb"​),        ​duration​=​int​(​ytdl_data​[​"duration"​]),        ​file_name​=​str​(​ytdl_data​[​"title"​]),        ​thumb​=​sedlyf​,        ​caption​=​capy​,        ​supports_streaming​=​True​,        ​progress​=​progress​,        ​progress_args​=​(            ​pablo​,            ​c_time​,            ​f"**📥 تحميل** `​{​urlissed​}​`"​,            ​file_stark​,        ),    ) 
 ​    ​await​ ​pablo​.​delete​() 
 ​    ​for​ ​files​ ​in​ (​sedlyf​, ​file_stark​): 
 ​        ​if​ ​files​ ​and​ ​os​.​path​.​exists​(​files​):