
   
init python:
    import time, os
    import random
    import datetime
    import re  
    RENPY_IMG_PATH = "images/characters/"
    RENPY_IMG_PATH_011 = "images/01_Leyla_sprite/011_Pajama_EXPR/"

    def fLogging(message, level="INFO", show_in_console=True):
        log_file_path = "log/game_log.txt" 
        debug_log_enabled = True
        
        if not debug_log_enabled:
            return

        # Thời gian hiện tại
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Tạo dòng log
        log_line = f"[{timestamp}] [{level}] {message}\n"

        # In ra console Ren'Py (Shift+O để xem)
        if show_in_console:
            # renpy.notify(f"LOG: {message}")  # Hiện thông báo nhỏ trên màn hình (tùy chọn)
            print(log_line.strip())           # In vào console dev

        # Ghi vào file (append mode)
        try:
            # Tạo thư mục nếu chưa có
            os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
            
            with open(renpy.fsdecode(log_file_path), "a", encoding="utf-8") as f:
                f.write(log_line)
        except Exception as e:
            print(f"Không thể ghi log: {e}")

    
    def fCalling_Name(speaker, target):
        key = f"{speaker}_to_{target}"
        if (speaker == "Hannah" and target == "John") or (speaker == "John" and target == "Hannah"):
            intimacy = INTI_HJ
        
        if (speaker == "Hannah" and target == "Leyla") or (speaker == "Leyla" and target == "Hannah"):
            intimacy = INTI_LH
        
        if (speaker == "John" and target == "Leyla") or (speaker == "Leyla" and target == "John"):
            intimacy = INTI_LJ

        levels = sorted(Calling_Others_Dict[key].keys(), reverse=True)
        for level in levels:
            if intimacy >= level:
                return Calling_Others_Dict[key][level]
        return Calling_Others_Dict[key][0]  # Default thấp nhất


    def fCalcutlating_3sIntimacy(INTI_HJ, INTI_LJ, INTI_LH):      
        if INTI_HJ >= 10 and INTI_LJ >= 10 and INTI_LH >= 10:
            return 1
        elif INTI_HJ > 20 and INTI_LJ >= 20 and INTI_LH >= 20:
            return 2
        elif INTI_HJ > 30 and INTI_LJ >= 30 and INTI_LH >= 30:
            return 3
        elif INTI_HJ > 40 and INTI_LJ >= 40 and INTI_LH >= 40:
            return 4
        else:
            return 0

    def fFetching_Images_Character(sCharName):
        RENPY_ALL_IMAGES_LIST = renpy.list_images()    
        s3_prefix = sCharName + " "
        
        return [img for img in RENPY_ALL_IMAGES_LIST if img.startswith(s3_prefix)]

    def fCalcutlating_Lewdless():
        s3_INTI_AVG = (INTI_HJ + INTI_LJ + INTI_LH) / 3
        return min(10, max(0, int(s3_INTI_AVG * 1.5))) 

    def fRandomnizing_Sprite(character, ts3_intimacy, outfit=None):
        t3s_SpriteCharacter_List = fFetching_Images_Character(character)
        if not t3s_SpriteCharacter_List:
            return None  

        s3_sList = []
        for s3_nameIMG in t3s_SpriteCharacter_List: 
            ts3_match = re.search(r'([HLJ]_[a-z]+)_s(\d)_([a-z]+(?:_[a-z]+)?)_?(\d)?', s3_nameIMG)
            if not ts3_match:
                continue
            outfit_base, sexy_level_int, pose, num = ts3_match.groups()
            sexy_level_int = int(sexy_level_int)
            # fLogging(outfit_base, "INFO") # H_satin
            # fLogging(sexy_level_int, "INFO") # 0 
            # fLogging(pose, "INFO") # nor
            # fLogging(num, "INFO") # 1

            if sexy_level_int != ts3_intimacy:
                continue
            
            if outfit and not s3_nameIMG.startswith(character + " " + outfit):
                continue 

            

            s3_sList.append(s3_nameIMG)
            fLogging(s3_sList, "INFO") # 1


        sSprite = random.choice(s3_sList)
        return sSprite

    def fRandomnizing_Hannah(ts3_intimacy):
        
        return fRandomnizing_Sprite("Hannah", ts3_intimacy, outfit="H_pajama")

    def fRandomnizing_Leyla(ts3_intimacy):
        
        return fRandomnizing_Sprite("Leyla", ts3_intimacy, outfit="L_babydoll")
    
    def fRandomnizing_John(ts3_intimacy):
        return fRandomnizing_Sprite("John", ts3_intimacy, outfit="J_tshirt") 

        
screen INTI_STAT_UI:
    frame:
        xalign 0.02 yalign 0.02          # Góc trên trái màn hình
        background "#0008"               # Nền đen mờ để dễ đọc (tùy chọn)
        padding (10, 10)
        vbox:
            text "Hannah - John: [INTI_HJ]" size 22 color "#ffffff"
            text "Leyla - John: [INTI_LJ]"   size 22 color "#ffffff"
            text "Leyla - Hannah: [INTI_LH]" size 22 color "#ffffff"

    # Tùy chọn: thêm nút ẩn/hiện để không làm rối màn hình
    textbutton "Ẩn Stats" action Hide("INTI_STAT_UI") xalign 0.02 yalign 0.15


label start:
    show screen INTI_STAT_UI
    jump day1_morning
    jump day1_afternoon


# $ ts3_intimacy = fCalcutlating_3sIntimacy(INTI_HJ, INTI_LJ, INTI_LH)
# $ Hannah_sprite_List = fRandomnizing_Hannah(ts3_intimacy)
# $ John_sprite_List = fRandomnizing_John(ts3_intimacy)
# $ Leyla_sprite_List = fRandomnizing_Leyla(ts3_intimacy)