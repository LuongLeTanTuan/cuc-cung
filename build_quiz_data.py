import json

# Verified MCQ answers (0-based indices)
# Câu 1 -> Câu 45
mcq_answers = {
    1: 3,   # D. Tất cả các phương án đều đúng
    2: 2,   # C. Phương pháp lịch sử; phương pháp logic; phương pháp tổng kết thực tiễn lịch sử; phương pháp so sánh
    3: 0,   # A. Chức năng nhận thức; chức năng giáo dục; chức năng dự báo và phê phán
    4: 3,   # D. Tất cả các phương án đều đúng
    5: 2,   # C. Nguyễn Ái Quốc
    6: 0,   # A. Ngày 03 tháng 2 năm 1930
    7: 0,   # A. Tư sản dân quyền cách mạng và thổ địa cách mạng để đi tới xã hội cộng sản
    8: 1,   # B. Trần Phú
    9: 3,   # D. Năm 1930 (Đảng Cộng sản Việt Nam ra đời)
    10: 0,  # A. Trần Phú
    11: 0,  # A. Sự lãnh đạo của Đảng là điều kiện cốt yếu cho thắng lợi của cách mạng Việt Nam
    12: 3,  # D. Tất cả các phương án đều đúng
    13: 3,  # D. Tất cả các phương án đều đúng
    14: 0,  # A. Hồ Chí Minh
    15: 3,  # D. Ngày 22 tháng 12 năm 1944
    16: 2,  # C. Thực dân Pháp xâm lược
    17: 1,  # B. Ngày 19 tháng 12 năm 1946
    18: 3,  # D. Tất cả các phương án đều đúng
    19: 3,  # D. Tất cả các phương án đều đúng
    20: 3,  # D. Nguyễn Văn Tố
    21: 3,  # D. Tất cả các phương án đều đúng
    22: 0,  # A. Hàn gắn vết thương chiến tranh, phục hồi kinh tế quốc dân
    23: 3,  # D. Tất cả các phương án đều đúng
    24: 3,  # D. Nguyễn Hữu Thọ
    25: 1,  # B. Tháng 9 năm 1960
    26: 0,  # A. Từ 18 đến ngày 30 tháng 12 năm 1972
    27: 0,  # A. Ngày 27 tháng 1 năm 1973
    28: 2,  # C. Chiến dịch Tây Nguyên
    29: 1,  # B. Ngày 26 tháng 4 năm 1975
    30: 3,  # D. Ngày 30 tháng 4 năm 1975
    31: 3,  # D. Tất cả các phương án đều đúng
    32: 0,  # A. Đại hội lần thứ IV
    33: 1,  # B. Đại hội lần thứ V
    34: 1,  # B. Đại hội lần thứ X
    35: 2,  # C. Chăm lo xây dựng con người có nhân cách, lối sống tốt đẹp, với các đặc tính cơ bản: yêu nước, nhân ái, nghĩa tình, trung thực, đoàn kết, cần cù, sáng tạo
    36: 0,  # A. Văn hóa Tiên tiến là yêu nước và tiến bộ với nội dung cốt lõi là lý tưởng độc lập dân tộc và chủ nghĩa xã hội theo chủ nghĩa Mác - Lênin, tư tưởng Hồ Chí Minh, nhằm mục tiêu tất cả vì con người
    37: 2,  # C. Đi đầu trong xây dựng và phát triển văn hóa, con người Việt Nam
    38: 0,  # A. Nắm vững hai mặt hợp tác và đấu tranh trong quan hệ quốc tế
    39: 3,  # D. Tất cả các phương án đều đúng
    40: 2,  # C. Khoa học, công nghệ, tri thức và nguồn nhân lực chất lượng cao
    41: 1,  # B. Nhằm thực hiện "dân giàu, nước mạnh, dân chủ, công bằng, văn minh“; giải phóng mạnh mẽ lực lượng sản xuất, không ngừng nâng cao đời sống nhân dân
    42: 0,  # A. Là một động lực quan trọng của nền kinh tế
    43: 0,  # A. Đại hội XII
    44: 3,  # D. Tất cả đều đúng
    45: 1   # B. Kinh tế
}

with open('parsed_data.json', 'r', encoding='utf-8') as f:
    raw = json.load(f)

final_mcq = []
for item in raw['mcq']:
    qid = item['id']
    final_mcq.append({
        'id': f'mcq_{qid}',
        'num': qid,
        'q': item['q'],
        'opts': item['opts'],
        'ans': mcq_answers[qid]
    })

# Format Short-Answers
# List of 30 short-answer questions
sa_data_cleaned = [
    {
        "num": 46,
        "q": "Đối tượng nghiên cứu của khoa học Lịch sử Đảng Cộng sản Việt Nam là gì?",
        "a": "Sự ra đời, phát triển và hoạt động lãnh đạo của Đảng qua các thời kỳ lịch sử."
    },
    {
        "num": 47,
        "q": "Thời gian, địa điểm, thành phần dự Hội nghị thành lập Đảng Cộng sản Việt Nam?",
        "a": "• Thời gian: Từ ngày 06/01 đến 07/02/1930.\n• Địa điểm: Cửu Long (Hồng Kông, Trung Quốc).\n• Thành phần: Dưới sự chủ trì của đồng chí Nguyễn Ái Quốc (đại biểu Quốc tế Cộng sản), gồm:\n  - 02 đại biểu của Đông Dương Cộng sản Đảng (Trịnh Đình Cửu và Nguyễn Đức Cảnh).\n  - 02 đại biểu của An Nam Cộng sản Đảng (Châu Văn Liêm và Nguyễn Thiệu)."
    },
    {
        "num": 48,
        "q": "Cương lĩnh chính trị đầu tiên xác định nhiệm vụ chủ yếu trước mắt của cách mạng Việt Nam là gì?",
        "a": "Đánh đổ đế quốc chủ nghĩa Pháp và bọn phong kiến, làm cho nước Nam hoàn toàn độc lập."
    },
    {
        "num": 49,
        "q": "Cương lĩnh chính trị đầu tiên xác định lực lượng cách mạng gồm những ai?",
        "a": "Công nhân và nông dân là lực lượng cơ bản (gốc cách mạng), trong đó giai cấp công nhân giữ vai trò lãnh đạo; đồng thời chủ trương đoàn kết tất cả các giai cấp, các lực lượng tiến bộ yêu nước (tiểu tư sản, trí thức, phú nông, trung tiểu địa chủ, tư sản dân tộc), tập trung chống đế quốc và tay sai."
    },
    {
        "num": 50,
        "q": "Quy luật ra đời của Đảng Cộng sản Việt Nam là gì?",
        "a": "Là sự kết hợp nhuần nhuyễn của 3 yếu tố: Chủ nghĩa Mác - Lênin + Phong trào công nhân + Phong trào yêu nước Việt Nam."
    },
    {
        "num": 51,
        "q": "Vai trò lãnh đạo của Đảng Cộng sản Đông Dương trong Luận cương Chính trị tháng 10 năm 1930 được xác định như thế nào?",
        "a": "Sự lãnh đạo của Đảng là điều kiện cốt yếu cho thắng lợi của cách mạng."
    },
    {
        "num": 52,
        "q": "Trong nội dung chuyển hướng chỉ đạo chiến lược của Đảng (1939-1945) xác định nhiệm vụ trung tâm của Đảng và nhân dân ta là gì?",
        "a": "Nhiệm vụ trung tâm là xúc tiến chuẩn bị khởi nghĩa vũ trang giành chính quyền."
    },
    {
        "num": 53,
        "q": "Ý nghĩa chủ trương chuyển hướng chiến lược của Đảng ta giai đoạn 1939-1945 là gì?",
        "a": "Là ngọn cờ dẫn đường cho nhân dân ta tiến lên giành thắng lợi trong sự nghiệp đánh Pháp, đuổi Nhật, giành độc lập cho dân tộc và tự do cho nhân dân (đỉnh cao là Cách mạng Tháng Tám năm 1945)."
    },
    {
        "num": 54,
        "q": "Năm 1943, trong Đề cương văn hóa Việt Nam của đồng chí Trường Chinh đề ra 3 nguyên tắc xây dựng nền văn hóa mới là gì?",
        "a": "Ba nguyên tắc vận động cuộc vận động văn hóa mới:\n1. Dân tộc hóa (chống mọi ảnh hưởng nô dịch, thuộc địa).\n2. Khoa học hóa (chống lại những gì phản tiến bộ, mê tín, phản khoa học).\n3. Đại chúng hóa (chống mọi chủ trương, hành động xa rời quần chúng, phục vụ lợi ích đại đa số nhân dân)."
    },
    {
        "num": 55,
        "q": "Ý nghĩa Tuyên ngôn Độc lập ngày 2-9-1945 do Chủ tịch Hồ Chí Minh đọc tại quảng trường Ba Đình?",
        "a": "Đó là một văn kiện lịch sử vô giá, một thiên anh hùng ca chiến đấu và chiến thắng; kết tinh sức mạnh và niềm tin, tràn đầy lòng tự hào và ý chí đấu tranh bất khuất của nhân dân Việt Nam trong sự nghiệp giành và giữ vững nền độc lập, tự do."
    },
    {
        "num": 56,
        "q": "Ngày 3-9-1945, trong phiên họp đầu tiên của Chính phủ lâm thời, Hồ Chí Minh đề nghị nhiệm vụ đầu tiên về xây dựng văn hoá là gì?",
        "a": "Chống nạn mù chữ (diệt giặc dốt) và giáo dục lại tinh thần nhân dân theo tinh thần dân chủ mới."
    },
    {
        "num": 57,
        "q": "Ngày 25-11-1945, BCH Trung ương Đảng ra chỉ thị “Kháng chiến, kiến quốc” đã nêu bốn nhiệm vụ chủ yếu và cấp bách nào?",
        "a": "Bốn nhiệm vụ chủ yếu và cấp bách:\n1. Củng cố chính quyền cách mạng.\n2. Chống thực dân Pháp xâm lược.\n3. Bài trừ nội phản.\n4. Cải thiện đời sống nhân dân."
    },
    {
        "num": 58,
        "q": "Thời gian, địa điểm diễn ra Đại hội đại biểu toàn quốc lần thứ II của Đảng?",
        "a": "• Thời gian: Từ ngày 11 đến ngày 19/02/1951.\n• Địa điểm: Tại xã Vinh Quang, huyện Chiêm Hóa, tỉnh Tuyên Quang (Chiến khu Việt Bắc)."
    },
    {
        "num": 59,
        "q": "Thế nào là đường lối kháng chiến toàn dân?",
        "a": "Là đem toàn bộ sức dân, tài dân, của dân; động viên, tổ chức toàn thể nhân dân tích cực tham gia kháng chiến. \"Mỗi người dân là một chiến sĩ, mỗi làng xóm là một pháo đài\"."
    },
    {
        "num": 60,
        "q": "Hội nghị Geneve (Giơnevơ, Thụy Sĩ) năm 1954 kết thúc thắng lợi có ý nghĩa gì đối với cách mạng Việt Nam?",
        "a": "Chấm dứt cuộc chiến tranh xâm lược của thực dân Pháp có Mỹ giúp sức; Pháp và các nước tham dự công nhận độc lập, chủ quyền, thống nhất và toàn vẹn lãnh thổ của 3 nước Đông Dương; mở ra trang sử mới cho dân tộc, tạo cơ sở pháp lý quốc tế cho sự nghiệp giải phóng miền Nam, thống nhất đất nước."
    },
    {
        "num": 61,
        "q": "Hội nghị Trung ương lần thứ 15 (tháng 1-1959) của Đảng đã ra nghị quyết về cách mạng miền Nam với tinh thần cơ bản là gì?",
        "a": "Tiếp tục cuộc cách mạng dân tộc dân chủ nhân dân, sử dụng bạo lực cách mạng kết hợp 2 lực lượng (chính trị và vũ trang), kết hợp đấu tranh chính trị với đấu tranh quân sự, khởi nghĩa giành chính quyền về tay nhân dân."
    },
    {
        "num": 62,
        "q": "Tháng 9 năm 1960, Đại hội đại biểu toàn quốc lần thứ III của Đảng xác định đường lối chung của cách mạng Việt Nam là gì?",
        "a": "Đồng thời tiến hành hai chiến lược cách mạng:\n1. Đẩy mạnh cách mạng XHCN ở miền Bắc (đóng vai trò quyết định nhất đối với sự phát triển của toàn bộ cách mạng cả nước).\n2. Tiến hành cách mạng dân tộc dân chủ nhân dân ở miền Nam (đóng vai trò quyết định trực tiếp đối với sự nghiệp giải phóng miền Nam).\nNhằm hoàn thành độc lập và dân chủ trong cả nước, thực hiện hòa bình thống nhất nước nhà."
    },
    {
        "num": 63,
        "q": "Tại Đại hội III (9/1960), Đảng nhận định triển vọng của cuộc kháng chiến chống Mỹ cứu nước như thế nào?",
        "a": "Đó là một quá trình đấu tranh gian khổ, trường kỳ, phức tạp nhưng thắng lợi cuối cùng nhất định thuộc về nhân dân ta; Nam - Bắc nhất định sum họp một nhà."
    },
    {
        "num": 64,
        "q": "Ngày 15-2-1961, các lực lượng vũ trang ở miền Nam được thống nhất với tên gọi là gì?",
        "a": "Quân giải phóng miền Nam Việt Nam."
    },
    {
        "num": 65,
        "q": "Cuộc Tổng tiến công và nổi dậy Xuân 1975 diễn ra trong thời gian nào và dấu mốc kết thúc?",
        "a": "Diễn ra trong 55 ngày đêm thần tốc từ ngày 10/3 đến ngày 30/4/1975 qua 3 chiến dịch lớn (Tây Nguyên, Huế - Đà Nẵng, Chiến dịch Hồ Chí Minh). Vào lúc 11 giờ 30 phút ngày 30/4/1975, lá cờ cách mạng cắm trên nóc Dinh Độc Lập, kết thúc thắng lợi trọn vẹn cuộc kháng chiến chống Mỹ cứu nước."
    },
    {
        "num": 66,
        "q": "Nền kinh tế thị trường định hướng xã hội chủ nghĩa ở nước ta hiện nay nhằm mục tiêu gì?",
        "a": "Nhằm thực hiện mục tiêu: \"Dân giàu, nước mạnh, dân chủ, công bằng, văn minh\"; giải phóng mạnh mẽ sức sản xuất, không ngừng nâng cao đời sống vật chất và tinh thần của nhân dân."
    },
    {
        "num": 67,
        "q": "Theo quan điểm của Đảng trong CNH, HĐH hiện nay để tăng trưởng kinh tế cần những yếu tố chủ yếu nào và yếu tố nào quyết định?",
        "a": "Cần 5 yếu tố chủ yếu: Vốn, Khoa học và công nghệ, Con người, Cơ cấu kinh tế, Thể chế chính trị và quản lý nhà nước.\nTrong đó: Yếu tố con người giữ vai trò quyết định."
    },
    {
        "num": 68,
        "q": "Nghị quyết Trung ương 8 (khóa XI) xác định đối tác trong chính sách đối ngoại của nước ta là gì?",
        "a": "Những ai tôn trọng độc lập, chủ quyền, thiết lập và mở rộng quan hệ hữu nghị, hợp tác bình đẳng, cùng có lợi với Việt Nam đều là đối tác của chúng ta."
    },
    {
        "num": 69,
        "q": "Quan điểm về xây dựng văn hóa trong Nghị quyết Trung ương 9 (khóa XI) xác định trọng tâm là gì?",
        "a": "Chăm lo xây dựng con người có nhân cách, lối sống tốt đẹp với các đặc tính cơ bản: Yêu nước, nhân ái, nghĩa tình, trung thực, đoàn kết, cần cù, sáng tạo."
    },
    {
        "num": 70,
        "q": "Văn hóa có vai trò gì đối với sự phát triển xã hội theo quan điểm của Đảng?",
        "a": "Văn hóa là nền tảng tinh thần của xã hội, vừa là mục tiêu, vừa là sức mạnh nội sinh và động lực to lớn thúc đẩy sự phát triển bền vững của đất nước."
    },
    {
        "num": 71,
        "q": "Cương lĩnh năm 2011 (Đại hội XI) bổ sung 2 đặc trưng mới nào về xã hội XHCN mà nhân dân ta xây dựng?",
        "a": "Bổ sung 2 đặc trưng bao trùm, tổng quát:\n1. \"Dân giàu, nước mạnh, dân chủ, công bằng, văn minh\" (được đưa lên làm đặc trưng đầu tiên).\n2. \"Có Nhà nước pháp quyền xã hội chủ nghĩa của nhân dân, do nhân dân, vì nhân dân do Đảng Cộng sản lãnh đạo\"."
    },
    {
        "num": 72,
        "q": "Đại hội XII của Đảng xác định trong nền kinh tế thị trường định hướng XHCN có những thành phần kinh tế nào?",
        "a": "Bao gồm 4 thành phần kinh tế:\n1. Kinh tế nhà nước (giữ vai trò chủ đạo).\n2. Kinh tế tập thể.\n3. Kinh tế tư nhân (là một động lực quan trọng).\n4. Kinh tế có vốn đầu tư nước ngoài."
    },
    {
        "num": 73,
        "q": "Theo Đại hội XII, để tiếp tục đẩy mạnh mô hình CNH, HĐH gắn với kinh tế tri thức cần lấy những yếu tố nào làm động lực chủ yếu?",
        "a": "Lấy khoa học, công nghệ, tri thức và nguồn nhân lực chất lượng cao làm động lực chủ yếu."
    },
    {
        "num": 74,
        "q": "Mối quan hệ giữa hội nhập kinh tế và các lĩnh vực khác được Đại hội XII xác định như thế nào?",
        "a": "Hội nhập kinh tế là trọng tâm; hội nhập trong các lĩnh vực khác (chính trị, an ninh - quốc phòng, văn hóa, xã hội...) phải tạo thuận lợi và hỗ trợ đắc lực cho hội nhập kinh tế quốc tế."
    },
    {
        "num": 75,
        "q": "Ba thắng lợi vĩ đại nhất mà Đảng lãnh đạo nhân dân ta giành được từ năm 1930 đến nay là gì?",
        "a": "1. Thắng lợi của Cách mạng Tháng Tám năm 1945, thành lập nước Việt Nam Dân chủ Cộng hòa.\n2. Thắng lợi oanh liệt của các cuộc kháng chiến giải phóng dân tộc và bảo vệ Tổ quốc (kháng chiến chống Pháp và chống Mỹ).\n3. Thắng lợi to lớn, có ý nghĩa lịch sử của công cuộc đổi mới và từng bước đưa đất nước quá độ lên chủ nghĩa xã hội."
    }
]

# List of 6 Essay Questions with in-depth complete structured answers
essay_data_cleaned = [
    {
        "num": 76,
        "q": "Trình bày ý nghĩa lịch sử Cách mạng Tháng Tám năm 1945. Liên hệ trách nhiệm sinh viên trong việc góp phần xây dựng và bảo vệ Tổ quốc hiện nay.",
        "a": """I. Ý NGHĨA LỊCH SỬ CỦA CÁCH MẠNG THÁNG TÁM NĂM 1945:
1. Đối với dân tộc Việt Nam:
- Đập tan xiềng xích nô lệ của thực dân Pháp hơn 80 năm và ách thống trị của phát xít Nhật; lật đổ chế độ phong kiến ngót nghìn năm tồn tại.
- Khai sinh ra nước Việt Nam Dân chủ Cộng hòa - Nhà nước dân chủ nhân dân đầu tiên ở Đông Nam Á. Đưa dân tộc Việt Nam bước vào kỷ nguyên mới: Kỷ nguyên độc lập dân tộc gắn liền với chủ nghĩa xã hội.
- Đưa nhân dân ta từ thân phận nô lệ lầm than trở thành người làm chủ đất nước, làm chủ vận mệnh của mình.
- Đảng Cộng sản Đông Dương từ một Đảng hoạt động bí mật trở thành một Đảng cầm quyền lãnh đạo toàn dân tộc.

2. Đối với quốc tế:
- Là thắng lợi đầu tiên của một dân tộc thuộc địa tự giải phóng dưới sự lãnh đạo của Đảng Mác-xít; chọc thủng một khâu xung yếu trong hệ thống thuộc địa của chủ nghĩa đế quốc.
- Cổ vũ mạnh mẽ phong trào giải phóng dân tộc của các nước thuộc địa và phụ thuộc ở châu Á, châu Phi và khu vực Mỹ Latinh.
- Khẳng định tính đúng đắn và sáng tạo của chủ nghĩa Mác - Lênin, tư tưởng Hồ Chí Minh về con đường cách mạng giải phóng dân tộc ở các nước thuộc địa.

II. LIÊN HỆ TRÁCH NHIỆM CỦA SINH VIÊN HIỆN NAY:
1. Về tư tưởng, lập trường chính trị:
- Kiên định mục tiêu độc lập dân tộc gắn liền với chủ nghĩa xã hội; tự hào và trân trọng những hy sinh to lớn của các thế hệ cha anh.
- Nâng cao bản lĩnh chính trị, chủ động nhận diện và kiên quyết đấu tranh phản bác các luận điệu xuyên tạc, bôi nhọ lịch sử cách mạng trên không gian mạng.

2. Về học tập và nâng cao năng lực chuyên môn:
- Xác định nhiệm vụ học tập và nghiên cứu khoa học là ưu tiên hàng đầu; tích cực làm chủ tri thức khoa học, công nghệ hiện đại, nâng cao trình độ ngoại ngữ và kỹ năng số để trở thành nguồn nhân lực chất lượng cao.

3. Về rèn luyện đạo đức và phong cách sống:
- Tu dưỡng đạo đức cách mạng, sống trung thực, có hoài bão, ý thức kỷ luật và trách nhiệm cộng đồng; thực hiện tốt phương châm "Học để làm việc, làm người, phụng sự Tổ quốc".

4. Về hành động cống hiến thực tiễn:
- Nhiệt huyết tham gia các hoạt động tình nguyện xã hội (Chiến dịch Mùa hè xanh, Tiếp sức mùa thi, hoạt động đền ơn đáp nghĩa).
- Luôn nêu cao tinh thần cảnh giác cách mạng, sẵn sàng thực hiện nghĩa vụ quân sự và tham gia xây dựng thế trận an ninh nhân dân, bảo vệ vững chắc Tổ quốc."""
    },
    {
        "num": 77,
        "q": "Trình bày một số bài học kinh nghiệm trong cuộc kháng chiến chống Mĩ, cứu nước của nhân dân Việt Nam (1954-1975). Theo anh (chị) Đảng phải làm gì để tiếp tục kế thừa, phát huy những bài học đó trong bối cảnh hiện nay.",
        "a": """I. BÀI HỌC KINH NGHIỆM TRONG KHÁNG CHIẾN CHỐNG MỸ, CỨU NƯỚC (1954 - 1975):
1. Giương cao ngọn cờ độc lập dân tộc và chủ nghĩa xã hội:
- Kết hợp nhuần nhuyễn hai nhiệm vụ chiến lược: Xây dựng CNXH ở miền Bắc (hậu phương lớn vững chắc) và cách mạng dân tộc dân chủ nhân dân ở miền Nam (tiền tuyến lớn anh dũng).

2. Đường lối chiến tranh nhân dân sáng tạo, độc lập, tự chủ:
- Huy động sức mạnh toàn dân, đánh địch toàn diện trên cả 3 mặt trận (quân sự, chính trị, ngoại giao), kết hợp khởi nghĩa quần chúng với chiến tranh cách mạng, đánh địch trên cả 3 vùng chiến lược (rừng núi, nông thôn đồng bằng, thành thị).

3. Nghệ thuật chỉ đạo chiến lược tài tình, linh hoạt:
- Biết đánh bại từng chiến lược chiến tranh của Mỹ (Chiến tranh đơn phương, Đặc biệt, Cục bộ, Việt Nam hóa chiến tranh); biết tạo và chớp đúng thời cơ ngàn năm có một để mở cuộc Tổng tiến công và nổi dậy mùa Xuân 1975 đỉnh cao là Chiến dịch Hồ Chí Minh lịch sử.

4. Kết hợp chặt chẽ sức mạnh dân tộc với sức mạnh thời đại:
- Tranh thủ sự ủng hộ to lớn, chí tình của Liên Xô, Trung Quốc, các nước XHCN, phong trào độc lập dân tộc và nhân dân yêu chuộng hòa bình trên toàn thế giới, hình thành mặt trận quốc tế rộng lớn ủng hộ Việt Nam.

5. Coi trọng công tác xây dựng Đảng và hệ thống chính trị:
- Đảng giữ vững vai trò hạt nhân lãnh đạo tuyệt đối, giữ vững sự đoàn kết nhất trí trong nội bộ, gắn bó máu thịt với nhân dân.

II. ĐẢNG TA CẦN LÀM GÌ ĐỂ KẾ THỪA VÀ PHÁT HUY TRONG BỐI CẢNH HIỆN NAY:
1. Kiên định độc lập dân tộc và CNXH: Vận dụng sáng tạo chủ nghĩa Mác - Lênin, tư tưởng Hồ Chí Minh phù hợp với thực tiễn hội nhập quốc tế và CMCN 4.0.
2. Phát huy sức mạnh đại đoàn kết toàn dân tộc: Quán triệt sâu sắc bài học "Dân là gốc", củng cố niềm tin của nhân dân vào Đảng và Nhà nước, chăm lo thiết thực đời sống nhân dân.
3. Củng cố quốc phòng - an ninh: Xây dựng thế trận quốc phòng toàn dân gắn với thế trận an ninh nhân dân vững chắc, bảo vệ Tổ quốc từ sớm, từ xa, không để bị động bất ngờ.
4. Đẩy mạnh đường lối đối ngoại độc lập, tự chủ, đa phương hóa, đa dạng hóa: Phát huy trường phái ngoại giao "Cây tre Việt Nam" - kiên định về nguyên tắc, linh hoạt về sách lược, kết hợp nội lực và ngoại lực.
5. Tăng cường xây dựng, chỉnh đốn Đảng trong sạch, vững mạnh: Kiên quyết phòng chống tham nhũng, lãng phí, tiêu cực, suy thoái tư tưởng chính trị, đạo đức lối sống trong cán bộ, đảng viên."""
    },
    {
        "num": 78,
        "q": "Trình bày quan điểm của Đảng về công nghiệp hóa trong thời kì đổi mới được nêu ra tại Đại hội VIII (7/1996) của Đảng. Sinh viên có thể làm gì để đóng góp vào quá trình công nghiệp hóa, hiện đại hóa đất nước theo định hướng của Đảng?",
        "a": """I. QUAN ĐIỂM VỀ CÔNG NGHIỆP HÓA, HIỆN ĐẠI HÓA TẠI ĐẠI HỘI VIII (1996):
1. Giữ vững độc lập tự chủ đi đôi với mở rộng hợp tác quốc tế: Đa phương hóa, đa dạng hóa quan hệ kinh tế đối ngoại, kết hợp sức mạnh dân tộc với sức mạnh thời đại.
2. Công nghiệp hóa gắn liền với hiện đại hóa: Kết hợp các bước đi tuần tự với đi tắt đón đầu, tranh thủ công nghệ hiện đại ở những khâu then chốt nhằm rút ngắn khoảng cách phát triển.
3. Lấy phát huy nguồn lực con người làm yếu tố cơ bản: Con người vừa là mục tiêu, vừa là động lực to lớn nhất; coi giáo dục - đào tạo và khoa học - công nghệ là quốc sách hàng đầu.
4. Khoa học và công nghệ là nền tảng và động lực của CNH, HĐH: Ứng dụng nhanh chóng các thành tựu KH-CN tiên tiến vào mọi ngành kinh tế quốc dân.
5. Lấy hiệu quả kinh tế - xã hội làm tiêu chuẩn cơ bản: Đảm bảo tăng trưởng kinh tế nhanh, bền vững, gắn với công bằng xã hội và bảo vệ môi trường sinh thái.
6. CNH, HĐH là sự nghiệp của toàn dân, của mọi thành phần kinh tế: Trong đó kinh tế nhà nước giữ vai trò chủ đạo, huy động tối đa nguồn lực xã hội.
7. Kết hợp kinh tế với quốc phòng, an ninh: Phát triển kinh tế song song với củng cố tiềm lực quốc phòng, bảo vệ vững chắc Tổ quốc.

II. HÀNH ĐỘNG CỦA SINH VIÊN ĐÓNG GÓP VÀO CÔNG CUỘC CNH, HĐH:
1. Làm chủ tri thức và công nghệ số: Tích cực học tập, nghiên cứu khoa học chuyên sâu, tiếp cận các công nghệ mũi nhọn như Trí tuệ nhân tạo (AI), IoT, dữ liệu lớn (Big Data), tự động hóa.
2. Trau dồi tư duy đổi mới sáng tạo và khởi nghiệp: Tham gia các cuộc thi sáng tạo khởi nghiệp, đưa ra các giải pháp ứng dụng công nghệ giải quyết các bài toán thực tiễn của doanh nghiệp và cộng đồng.
3. Rèn luyện tác phong lao động công nghiệp và kỷ luật: Rèn luyện tính chuyên nghiệp, quản lý thời gian khoa học, kỹ năng làm việc nhóm và tuân thủ chuẩn mực đạo đức nghề nghiệp.
4. Nâng cao năng lực hội nhập: Chủ động học tập ngoại ngữ, tìm hiểu các tiêu chuẩn quốc tế để sẵn sàng làm việc trong môi trường đa quốc gia và chuỗi giá trị toàn cầu."""
    },
    {
        "num": 79,
        "q": "Trong bối cảnh quốc tế hiện nay Đảng ta cần phải làm gì để tăng cường hội nhập quốc tế, góp phần xây dựng và phát triển đất nước. Liên hệ trách nhiệm sinh viên.",
        "a": """I. GIẢI PHÁP CỦA ĐẢNG NHẰM TĂNG CƯỜNG HỘI NHẬP QUỐC TẾ HIỆN NAY:
1. Đảm bảo cao nhất lợi ích quốc gia - dân tộc: Kiên định mục tiêu độc lập, tự chủ trên cơ sở các nguyên tắc cơ bản của Hiến chương LHQ và luật pháp quốc tế, bình đẳng, cùng có lợi.
2. Thực hiện nhất quán đường lối đối ngoại độc lập, tự chủ, hòa bình, hợp tác: Đa phương hóa, đa dạng hóa quan hệ quốc tế; là bạn, là đối tác tin cậy, thành viên tích cực và có trách nhiệm của cộng đồng quốc tế.
3. Đẩy mạnh hội nhập toàn diện, sâu rộng: Lấy hội nhập kinh tế làm trọng tâm, hội nhập các lĩnh vực chính trị, an ninh - quốc phòng, văn hóa, giáo dục, KH-CN phải gắn kết chặt chẽ và phục vụ phát triển kinh tế.
4. Tận dụng tối đa các Hiệp định thương mại tự do (FTA) thế hệ mới: Thực thi hiệu quả CPTPP, EVFTA, RCEP... để mở rộng thị trường xuất khẩu, thu hút dòng vốn đầu tư FDI chất lượng cao.
5. Nâng cao năng lực tự chủ và sức cạnh tranh của nền kinh tế: Hoàn thiện hệ thống pháp luật, cơ chế chính sách, phát triển nguồn nhân lực chất lượng cao, chủ động phòng ngừa rủi ro tài chính, tiền tệ và an ninh mạng.
6. Giữ gìn và phát huy bản sắc văn hóa dân tộc: Trong quá trình hội nhập, tiếp thu có chọn lọc tinh hoa văn hóa nhân loại, tránh nguy cơ hòa tan hoặc xâm lăng văn hóa.

II. LIÊN HỆ TRÁCH NHIỆM CỦA SINH VIÊN:
1. Xây dựng phẩm chất \"Công dân toàn cầu\": Nâng cao trình độ ngoại ngữ, kỹ năng tin học và sự am hiểu về các nền văn hóa thế giới nhằm tự tin giao tiếp, hợp tác quốc tế.
2. Nỗ lực học tập để nâng cao năng lực cạnh tranh: Sinh viên phải chủ động học tập, không ngừng nâng cao tay nghề chuyên môn để cạnh tranh sòng phẳng trên thị trường lao động quốc tế.
3. Là đại sứ lan tỏa văn hóa Việt Nam: Tích cực giới thiệu lịch sử, truyền thống, vẻ đẹp con người và đất nước Việt Nam thân thiện, đổi mới tới bạn bè năm châu qua các chương trình giao lưu, mạng xã hội.
4. Cảnh giác với các nguy cơ ngoại lai độc hại: Tỉnh táo chọn lọc thông tin, không a dua theo những trào lưu phản cảm, giữ vững bản sắc dân tộc và lòng tự tôn văn hóa Việt Nam."""
    },
    {
        "num": 80,
        "q": "Phân tích nội dung đường lối đổi mới toàn diện đất nước được Đảng Cộng sản Việt Nam đề ra tại Đại hội VI (1986). Những bài học kinh nghiệm mà Đảng ta đã đúc kết cho công cuộc phát triển đất nước trong giai đoạn hiện nay.",
        "a": """I. NỘI DUNG ĐƯỜNG LỐI ĐỔI MỚI TOÀN DIỆN CỦA ĐẠI HỘI VI (12/1986):
1. Bối cảnh lịch sử:
Đất nước lâm vào khủng hoảng kinh tế - xã hội trầm trọng (lạm phát phi mã 774,7% năm 1986, đời sống nhân dân vô cùng khó khăn). Đại hội VI đã dũng cảm "nhìn thẳng vào sự thật, đánh giá đúng sự thật, nói rõ sự thật" để hoạch định đường lối đổi mới toàn diện.

2. Đổi mới về kinh tế (trọng tâm then chốt):
- Xóa bỏ triệt để cơ chế tập trung quan liêu, bao cấp; chuyển sang nền kinh tế nhiều thành phần vận hành theo cơ chế thị trường có sự quản lý của Nhà nước theo định hướng XHCN.
- Điều chỉnh lớn về cơ cấu đầu tư: Tập trung thực hiện Ba chương trình kinh tế lớn: Lương thực - thực phẩm, Hàng tiêu dùng và Hàng xuất khẩu.
- Khẳng định phát triển kinh tế hàng hóa nhiều thành phần có ý nghĩa chiến lược lâu dài.

3. Đổi mới về chính trị và xã hội:
- Đổi mới sự lãnh đạo của Đảng, nâng cao hiệu lực quản lý của Nhà nước pháp quyền XHCN; thực hiện nguyên tắc tập trung dân chủ.
- Phát huy quyền làm chủ của nhân dân theo phương châm: "Dân biết, dân bàn, dân làm, dân kiểm tra".
- Chú trọng giải quyết các vấn đề xã hội: Tạo việc làm, cải cách tiền lương, chăm lo y tế, giáo dục và công bằng xã hội.

4. Đổi mới về đối ngoại:
- Chuyển từ đối đầu sang đối thoại; chủ trương đa phương hóa, đa dạng hóa quan hệ đối ngoại; từng bước phá thế bao vây cấm vận, tạo môi trường quốc tế thuận lợi để xây dựng đất nước.

II. BỐN BÀI HỌC KINH NGHIỆM ĐÚC KẾT CHO CÔNG CUỘC PHÁT TRIỂN HIỆN NAY:
1. Một là: Luôn quán triệt tư tưởng "Dân là gốc", xây dựng và phát huy quyền làm chủ của nhân dân lao động.
2. Hai là: Xuất phát từ thực tế, tôn trọng và hành động theo quy luật khách quan (kiên quyết xóa bỏ bệnh duy ý chí, giáo điều, nóng vội).
3. Ba là: Biết kết hợp sức mạnh của dân tộc với sức mạnh của thời đại trong điều kiện mới.
4. Bốn là: Chăm lo xây dựng Đảng ngang tầm với nhiệm vụ chính trị của một Đảng cầm quyền lãnh đạo nhân dân tiến hành sự nghiệp đổi mới."""
    },
    {
        "num": 81,
        "q": "Trình bày những thành tựu cơ bản trong công cuộc đổi mới đất nước (1986-2021). Theo anh (chị) để phát huy những thành tựu đó trong thực hiện nghị quyết Đại hội XIII giai đoạn 2021 - 2026 Đảng ta cần phải làm gì?",
        "a": """I. THÀNH TỰU CƠ BẢN QUA 35 NĂM ĐỔI MỚI (1986 - 2021):
1. Về kinh tế:
- Đưa đất nước thoát khỏi khủng hoảng, gia nhập nhóm nước đang phát triển có thu nhập trung bình.
- Tốc độ tăng trưởng kinh tế duy trì ở mức cao; quy mô nền kinh tế tăng gần 12 lần (đạt hơn 343 tỷ USD năm 2020); kim ngạch xuất nhập khẩu vượt mốc 540 tỷ USD.
- Tỷ lệ hộ nghèo giảm ấn tượng từ 58% (1993) xuống còn dưới 3% theo chuẩn nghèo đa chiều.

2. Về chính trị - xã hội:
- Chính trị - xã hội ổn định vững chắc; khối đại đoàn kết toàn dân tộc không ngừng được củng cố.
- Nhà nước pháp quyền XHCN của nhân dân, do nhân dân, vì nhân dân ngày càng hoàn thiện. Nền dân chủ XHCN được mở rộng và phát huy.

3. Về văn hóa, giáo dục, y tế và phát triển con người:
- Đời sống vật chất và tinh thần của người dân được nâng cao rõ rệt; chỉ số phát triển con người (HDI) thuộc nhóm trung bình cao của thế giới.
- Mạng lưới y tế, giáo dục phát triển rộng khắp; phòng chống dịch bệnh hiệu quả.

4. Về quốc phòng, an ninh:
- Giữ vững độc lập, chủ quyền, thống nhất, toàn vẹn lãnh thổ; giữ vững môi trường hòa bình, ổn định để phát triển kinh tế.

5. Về đối ngoại và vị thế quốc tế:
- Thiết lập quan hệ ngoại giao với 189 quốc gia; có quan hệ Đối tác chiến lược và Toàn diện với các cường quốc; hội nhập quốc tế sâu rộng. Đúng như Tổng Bí thư Nguyễn Phú Trọng khẳng định: \"Đất nước ta chưa bao giờ có được cơ đồ, tiềm lực, vị thế và uy tín quốc tế như ngày nay\".

II. ĐẢNG TA CẦN LÀM GÌ ĐỂ PHÁT HUY THÀNH TỰU TRONG GIAI ĐOẠN 2021 - 2026 (ĐẠI HỘI XIII):
1. Đổi mới mô hình tăng trưởng, cơ cấu lại nền kinh tế: Đẩy mạnh chuyển đổi số quốc gia, phát triển kinh tế số, kinh tế xanh và kinh tế tuần hoàn, lấy đổi mới sáng tạo làm động lực cốt lõi.
2. Hoàn thiện đồng bộ thể chế phát triển: Tháo gỡ các rào cản, tạo môi trường đầu tư kinh doanh minh bạch, thông thoáng cho mọi thành phần kinh tế phát triển bình đẳng.
3. Tăng cường xây dựng, chỉnh đốn Đảng và hệ thống chính trị trong sạch, vững mạnh: Đẩy lùi tham nhũng, lãng phí, tiêu cực; xây dựng đội ngũ cán bộ năng động, sáng tạo, dám nghĩ, dám làm, dám chịu trách nhiệm vì lợi ích chung.
4. Phát huy giá trị văn hóa và sức mạnh con người Việt Nam: Khơi dậy mạnh mẽ tinh thần yêu nước, khát vọng phát triển đất nước phồn vinh, hạnh phúc; thực hiện tiến bộ và công bằng xã hội.
5. Kiên quyết bảo vệ Tổ quốc và nâng cao hiệu quả đối ngoại: Giữ vững độc lập, chủ quyền biên giới, biển đảo; chủ động hội nhập quốc tế toàn diện, nâng tầm ngoại giao đa phương."""
    }
]

quiz_data = {
    'mcq': final_mcq,
    'sa': sa_data_cleaned,
    'essay': essay_data_cleaned
}

with open('quiz_complete_data.json', 'w', encoding='utf-8') as f:
    json.dump(quiz_data, f, ensure_ascii=False, indent=2)

print(f"Generated complete quiz dataset:")
print(f"- {len(final_mcq)} MCQ questions")
print(f"- {len(sa_data_cleaned)} Short-Answer questions")
print(f"- {len(essay_data_cleaned)} Detailed Essay questions")
print("Total: 81 questions!")
