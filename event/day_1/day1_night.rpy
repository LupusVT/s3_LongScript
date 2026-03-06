label day1_night:
    scene bg bg_living_3
    with fade

    show Leyla Leyla_Expr305_Pose1_Action0_ClothPajama1010__POV011_LivingRoom_0 at left
    show Hannah Hannah_Expr1_Pose1_Action0_ClothWhiteSatin1010__POV011_LivingRoom_0 at right

    "Buổi tối Day 1. Căn phòng khách sáng ấm, mùi lẩu Thái thơm lan khắp nhà."

    "Leyla" "Lẩu xong rồi nè! Hannah thử đi, cay vừa thôi để còn ngủ ngon."
    "Hannah" "Mùi thơm thật đó... cay giống tình bạn nhà mình luôn, càng ăn càng nghiện."
    "John" "Anh nghe câu này là biết tối nay vui rồi."

    $ INTI_HJ += 1
    $ INTI_LH += 1

    scene bg bg_living_4
    with dissolve

    "Sau bữa tối, John và Hannah mang hai lon bia nhẹ ra ban công. Gió đêm lướt qua, thành phố rực đèn phía xa."

    show Hannah Hannah_Expr27_Pose1_Action0_ClothWhiteSatin1021__POV011_LivingRoom_0 at right
    "Hannah" "Ở Seoul em cũng hay đứng như vầy mỗi khi stress."
    "Hannah" "Nhưng hôm nay cảm giác khác... yên tâm hơn."
    "John" "Vì em đã có nhà thứ hai ở đây."

    scene bg bg_living_2
    with dissolve

    show Leyla Leyla_Expr1_Pose1_Action0_ClothPajama9910__POV011_LivingRoom_0 at left
    show Hannah Hannah_Expr25_Pose1_Action0_ClothWhiteSatin1010__POV011_LivingRoom_0 at right

    "Một lúc sau, cả ba tụ lại phòng khách chơi Uno."
    "Leyla" "Luật nhà này: ai thua sẽ uống trà đào!"
    "Hannah" "Em vừa rút +4 lần thứ ba luôn á?!"
    "John" "Không sao, trà đào của Leyla ngon mà."
    "Leyla" "Chuẩn! Thua vui là được, không quạu nha."

    scene bg bg_living_1
    with dissolve

    show Leyla Leyla_Expr23_Pose1_Action0_ClothPajama1010__POV011_LivingRoom_0 at left
    show Hannah Hannah_Expr23_Pose1_Action0_ClothWhiteSatin1010__POV011_LivingRoom_0 at right

    "Khuya dần, Leyla giúp Hannah xếp nốt vài món đồ vào tủ trước cửa phòng."
    "Leyla" "Xong hết rồi đó. Từ mai phòng này chính thức là của bạn."
    "Hannah" "Cảm ơn Leyla... thật sự cảm ơn vì đã làm em thấy mình thuộc về nơi này."
    "Hai cô gái ôm nhẹ nhau, nụ cười lặng mà ấm."

    $ INTI_LH += 2

    scene bg bg_living_5
    with dissolve

    show Leyla Leyla_Expr27_Pose1_Action0_ClothPajama1010__POV011_LivingRoom_0 at left

    "Trong phòng ngủ chính, John và Leyla nói nhỏ trước khi tắt đèn."
    "Leyla" "Có thêm Hannah, nhà mình vui hẳn lên anh ha."
    "John" "Ừ, tự nhiên thấy mọi thứ đủ đầy hơn."

    $ curLewdness = fCalcutlating_Lewdless()

    scene black
    with fade
    "Đêm đầu tiên có Hannah, cả nhà đều ngủ ngon hơn thường lệ..."

    return
