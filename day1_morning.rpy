label day1_morning:
    scene black
    with fade

    "Tiếng chuông báo thức vang lên trong căn hộ nhỏ, kéo cả ba người ra khỏi giấc ngủ ngắn ngủi."
    "Ánh nắng sớm chạm vào rèm cửa, tạo thành những vệt sáng vàng nhạt trên sàn nhà."

    "John là người dậy đầu tiên. Anh ngáp dài, bước ra bếp và bắt đầu đun nước."

    "Vài phút sau, Hannah xuất hiện ở cửa bếp, tóc vẫn còn rối vì ngủ dậy."
    "Hannah" "Sáng nay anh dậy sớm ghê. Em còn tưởng mình là người đầu tiên."
    "John" "Anh muốn chuẩn bị bữa sáng tử tế một chút. Hôm nay mình có nhiều việc phải bàn mà."

    "Leyla" "Nếu có cà phê thì em sẵn sàng bàn mọi thứ trên đời."
    "Leyla vừa nói vừa bước vào, kéo ghế ngồi xuống như thể đã tỉnh táo hoàn toàn."

    menu:
        "Bạn muốn John làm gì cho bữa sáng?":
            "Nấu bữa sáng đơn giản và ấm cúng":
                $ INTI_HJ += 1
                $ INTI_LJ += 1
                "John" "Bánh mì nướng với trứng thôi, nhưng đủ ấm bụng."
                "Hannah mỉm cười, đưa đĩa cho Leyla trước."
                "Leyla" "Đơn giản mà ngon thật. Có cảm giác như một gia đình nhỏ vậy."
            "Pha cà phê thật đậm cho Leyla":
                $ INTI_LJ += 2
                $ leyla_horny += 1
                "John" "Anh có cà phê đậm cho em đây, đúng kiểu em thích."
                "Leyla" "Ôi, được chiều thế này thì em sẽ ngoan cả ngày."
                "Hannah" "Nghe câu đó mà chị chưa chắc đâu nhé."
            "Rủ cả hai cùng nấu để vui hơn":
                $ INTI_HJ += 1
                $ INTI_LJ += 1
                $ INTI_LH += 2
                "John" "Mỗi người một tay đi, làm chung sẽ nhanh hơn."
                "Hannah và Leyla nhìn nhau rồi bật cười, nhanh chóng chia việc rất ăn ý."

    "Bữa sáng kết thúc bằng những câu chuyện vụn vặt: lịch làm việc, danh sách mua đồ, và kế hoạch cuối tuần."

    "Khi dọn bàn xong, không khí trong phòng trở nên yên tĩnh hơn một chút."
    "Hannah" "Thật ra... dạo này em thấy mọi người ít có thời gian ngồi lại cùng nhau."
    "Leyla" "Đúng đó. Toàn ai cũng bận, nói chuyện thì toàn qua loa."

    menu:
        "John phản hồi thế nào?":
            "Hứa sẽ dành thời gian buổi tối cho cả ba":
                $ INTI_HJ += 2
                $ INTI_LJ += 2
                "John" "Tối nay mình để điện thoại sang một bên, chỉ nói chuyện với nhau thôi."
                "Hannah" "Nghe vậy là em thấy nhẹ lòng rồi."
                "Leyla" "Chốt nhé, ai phá kèo thì rửa bát một tuần."
            "Đề nghị làm một chuyến đi ngắn cuối tuần":
                $ INTI_HJ += 1
                $ INTI_LJ += 1
                $ INTI_LH += 1
                "John" "Hay cuối tuần này mình đi đâu gần gần? Đổi không khí một chút."
                "Hannah" "Em thích ý đó. Chỉ cần đi cùng nhau là được."
                "Leyla" "Em sẽ lo danh sách đồ ăn vặt!"
            "Thành thật nói mình đang áp lực công việc":
                $ INTI_HJ += 1
                $ INTI_LJ += 1
                $ john_horny -= 1
                "John" "Anh xin lỗi, gần đây anh căng thẳng quá nên hơi xa cách."
                "Hannah" "Cảm ơn anh vì đã nói thật."
                "Leyla" "Lần sau mệt thì nói bọn em biết, đừng ôm một mình."

    "Sau cuộc trò chuyện, Hannah đứng dậy kéo rèm cửa ra hẳn để căn phòng sáng hơn."
    "Nắng tràn vào, làm bầu không khí cũng nhẹ nhàng theo."

    "Hannah" "Được rồi, bắt đầu ngày mới thôi."
    "Leyla" "Nhưng trước đó... một cái ôm khởi động tinh thần?"

    "Cả ba bật cười rồi ôm nhau một lúc ngắn, đủ để thấy gần gũi hơn so với buổi sáng hôm qua."

    "Buổi sáng khép lại với cảm giác bình yên hiếm có."
    "Dù còn nhiều chuyện phải giải quyết, ít nhất họ biết mình đang cùng một phía."

    jump day1_afternoon


label day1_afternoon:
    scene black
    with dissolve

    "Buổi chiều sẽ tiếp tục trong bản cập nhật kế tiếp."
    return
