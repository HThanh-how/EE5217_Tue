import os, glob, re

sections_dir = 'd:/Phd/EE5217_Tue/sections'
images_dir = 'd:/Phd/EE5217_Tue/images'

# Generate placeholder images for latex
import urllib.request
def ensure_image(filename, text="Figure"):
    path = os.path.join(images_dir, filename)
    if not os.path.exists(path):
        url = f"https://fakeimg.pl/600x300/?text={text.replace(' ', '+')}&font=noto"
        try:
            urllib.request.urlretrieve(url, path)
        except:
            # Create a blank file if no internet
            with open(path, 'wb') as f:
                f.write(b"")

required_images = [
    "fig7_1.png", "fig7_2.png", "fig7_4.png", "fig7_5.png",
    "fig7_6.png", "fig7_7.png", "fig7_8.png", "fig7_9.png",
    "fig7_10.png", "fig7_12.png", "fig7_13.png", "fig7_14.png",
    "fig7_15.png", "fig7_16.png", "fig7_17.png", "fig7_18.png",
    "fig7_19.png", "fig7_20.png", "fig7_21.png", "fig7_22.png",
    "fig7_23.png", "fig7_24.png", "fig7_26.png", "fig7_28.png",
    "fig7_29.png", "fig7_31.png", "fig7_34.png", "fig7_35.png",
    "fig7_36.png", "fig7_40.png", "fig7_42.png", "fig7_45.png",
    "fig7_48.png", "fig7_50.png", "fig7_51.png", "fig7_53.png"
]
for img in required_images:
    ensure_image(img, "Figure " + img.replace(".png", "").replace("fig", ""))


# Clear old slides
for file in glob.glob(os.path.join(sections_dir, '*.html')):
    os.remove(file)

slides_data = [
    ('00_cover.html', '''<div class="slide" style="text-align: center;">
    <h2>ĐẠI HỌC BÁCH KHOA - ĐHQG TP.HCM</h2>
    <h1 style="color: var(--primary-color);">BÁO CÁO MÔN HỌC EE5217</h1>
    <h2 style="color: #666;">ĐỀ TÀI: DESIGN FOR TEST BY MEANS OF SCAN</h2>
    <br><br>
    <p><b>Nhóm thực hiện:</b> Nhóm 7</p>
    <p>Nguyen Thai Thanh Binh (2570175)</p>
    <p>Vu Tien Giang (2570188)</p>
    <p>Pham Huy Thanh (2570317)</p>
    <br>
    <p style="font-size: 1rem; color: #888;">(Bấm phím Mũi Tên Phải [→] hoặc Nút [Play] bên dưới để bắt đầu)</p>
</div>'''),

    ('01_01_intro.html', '''<div class="slide">
    <h1 style="color: var(--primary-color);">Chương 1: Đặt Vấn Đề</h1>
    <ul>
        <li>Hàng tỷ bóng bán dẫn trên một chip gây ra thách thức khổng lồ về mặt kiểm thử (Testing).</li>
        <li>Việc đảm bảo không có lỗi vật lý (stuck-at faults, short, open) là yếu cầu sống còn.</li>
        <li>Với mạch tuần tự (Sequential Circuits), việc điều khiển (controllability) và quan sát (observability) là vô cùng khó khăn.</li>
        <li><b style="color:var(--primary-color)">Giải pháp:</b> DFT (Design For Test) - Thiết kế Khả kiểm bằng phương pháp Quét (Scan Chain).</li>
    </ul>
    <div style="text-align: center; margin-top:20px;">
        <img src="https://fakeimg.pl/800x250/?text=Testing+Complexity+in+VLSI&font=noto" style="border-radius:10px;box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    </div>
</div>'''),

    ('02_01_making_testable.html', '''<div class="slide">
    <h1 style="color: var(--primary-color);">Chương 2: Làm Mạch Khả Kiểm</h1>
    <h2>Making Circuits Testable</h2>
    <ul>
        <li>Một mạch dễ kiểm thử khi các test vectors sinh ra dễ dàng và đạt độ phủ lỗi (fault coverage) cao, tốn ít thời gian.</li>
        <li>Điều kiện cốt lõi: Tăng <b>Khả năng điều khiển (Controllability)</b> và <b>Khả năng quan sát (Observability)</b>.</li>
        <li><b>Tradeoffs:</b> Chèn hardware -> Tăng area, timing delay, power consumption... Bù lại giảm mạnh Test Time.</li>
    </ul>
    <div style="text-align: center; margin-top:20px;">
        <img src="images/mux_dff.png" style="max-height: 250px; border-radius:10px;" onerror="this.src='https://fakeimg.pl/600x250/?text=Controllability+%26+Observability+Tradeoffs&font=noto';">
    </div>
</div>'''),

    ('02_02_huffman.html', '''<div class="slide">
    <h1 style="color: var(--primary-color);">Kiểm Thử Mạch Tuần Tự</h1>
    <h2>Mô hình Huffman & Unfolding</h2>
    <div style="display:flex; gap: 20px; align-items:center;">
        <div style="flex: 1;">
            <ul>
                <li><b>Mô hình Huffman:</b> Tách mạch tuần tự thành Khối Tổ Hợp (Combinational) + Register Phản hồi.</li>
                <li><b>Mô hình Unfolding (Trải phẳng):</b> Áp dụng trọn vẹn thuật toán test mạch tổ hợp lấy từ thanh ghi (Pseudo I/O).</li>
            </ul>
        </div>
        <div style="flex: 1; text-align: center;">
            <img src="images/fig7_1.png" style="border-radius:8px; margin-bottom: 10px; max-height: 150px; max-width: 100%;"><br>
            <img src="images/fig7_2.png" style="border-radius:8px; max-height: 150px; max-width: 100%;">
        </div>
    </div>
</div>'''),

    ('03_01_insertion.html', '''<div class="slide">
    <h1 style="color: var(--primary-color);">Chương 3: Chèn Testability</h1>
    <h2>Cải thiện Khả năng Quan sát & Điều khiển</h2>
    <div style="display:flex; gap: 20px; align-items:center;">
        <div style="flex: 1.2;">
            <ul>
                <li><b>Observability:</b> Kéo các tín hiệu chìm (flags, MUX selects) ra cổng output chính.</li>
                <li><b>Controllability:</b> Dùng phần cứng (0-insertion, 1-insertion). Thêm MUX có cờ <code>NbarT</code> để can thiệp Data Path.</li>
            </ul>
        </div>
        <div style="flex: 0.8; text-align: center;">
            <img src="images/fig7_4.png" style="border-radius:8px; margin-bottom: 15px; max-width:100%;"><br>
            <img src="images/fig7_5.png" style="border-radius:8px; max-width:100%;">
        </div>
    </div>
</div>'''),

    ('03_02_muxdemux.html', '''<div class="slide">
    <h1 style="color: var(--primary-color);">Chia Sẻ Điểm Kiểm Thử</h1>
    <ul>
        <li>Quá nhiều chân (Pins) I/O Test là không thực tế.</li>
        <li>Giải pháp: Dùng <b>MUX</b> để dồn nhiều node quan sát vào 1 cổng; Dùng <b>DEMUX</b> để phân luồng.</li>
        <li>Tối ưu hóa hơn: Dùng <b>Counter/Shift Register</b> nội bộ thay thế chân chọn.</li>
    </ul>
    <div style="display:flex; justify-content: space-around; margin-top:20px;">
        <img src="images/fig7_6.png" style="max-height: 250px; border-radius:8px;">
        <img src="images/fig7_7.png" style="max-height: 250px; border-radius:8px;">
    </div>
</div>'''),

    ('03_03_isolated_scan.html', '''<div class="slide">
    <h1 style="color: var(--primary-color);">Isolated Serial Scan</h1>
    <div style="display:flex; gap: 20px; align-items:center;">
        <div style="flex: 1;">
            <ul>
                <li>Sử dụng thanh ghi dịch (Shift-register) tải nối tiếp dữ liệu Test, xuất nối tiếp kết quả ra.</li>
                <li>Mạch được "cô lập" khi cờ phân vùng <code>NbarT = 1</code>.</li>
                <li>Hạt nhân khởi sinh ra kỹ thuật cực kì quan trọng: <b>Scan Chain</b>.</li>
            </ul>
        </div>
        <div style="flex: 1; text-align: center;">
            <img src="images/fig7_14.png" style="border-radius:8px; margin-bottom: 10px;"><br>
            <img src="images/fig7_16.png" style="border-radius:8px;">
        </div>
    </div>
</div>'''),

    ('04_01_fullscan_intro.html', '''<div class="slide">
    <h1 style="color: var(--primary-color);">Chương 4: Full Scan DFT</h1>
    <h2>Kỹ Thuật Đỉnh Cao Biến Tuần Tự Thành Tổ Hợp</h2>
    <div style="display:flex; gap: 20px; align-items:center;">
        <div style="flex: 1;">
            <ul>
                <li>Tích hợp hẳn chức năng Shift Register vào tất cả các Flip-flops trạng thái.</li>
                <li>Mọi DFF đều nối thành chuỗi domino (Scan Chain).</li>
                <li>Chế độ kiểm thử nạp/xuất data nối tiếp với <b>Fault Coverage lên đến 100%</b>.</li>
            </ul>
        </div>
        <div style="flex: 1; text-align: center;">
            <img src="images/fig7_17.png" style="border-radius:8px; max-height:300px;">
        </div>
    </div>
</div>'''),

    ('04_02_ff_structures.html', '''<div class="slide">
    <h1 style="color: var(--primary-color);">Cấu Trúc Scan Flip-Flop</h1>
    <div style="display:flex; gap: 20px; align-items:center;">
        <div style="flex: 1;">
            <h3>Muxed Scan Element</h3>
            <ul><li>Dùng Mux 2-1 cắm ngay chân D. Chuyển đổi DataIn/SerialIn. Đơn giản phổ biến.</li></ul>
            <h3>Dual Clocking</h3>
            <ul><li>Dùng 2 xung nhịp riêng (DataClock, TestClock) không qua Mux, giảm delay logic.</li></ul>
            <h3>LSSD (Level Sensitive Scan Design)</h3>
            <ul><li>Thiết kế danh tiếng từ IBM gồm Master/Slave Latch tách biệt pha clock hoàn toàn.</li></ul>
        </div>
        <div style="flex: 1; text-align: center;">
            <img src="images/fig7_23.png" style="max-height: 120px; margin-bottom:10px;"><br>
            <img src="images/fig7_26.png" style="max-height: 120px; margin-bottom:10px;"><br>
            <img src="images/fig7_31.png" style="max-height: 120px;">
        </div>
    </div>
</div>'''),

    ('04_03_residue5.html', '''<div class="slide">
    <h1 style="color: var(--primary-color);">Quy trình: Mạch Đếm Residue-5</h1>
    <ul>
        <li><b>Post-synthesis -> Unfolded & ATPG:</b> Trải phẳng tạo Combinational model, phần mềm ATPG sinh 26 tests lấy 100% Coverage.</li>
        <li><b>Scan Insertion:</b> Móc nối ngõ <code>Si</code>-><code>So</code> làm liền mạch chuỗi Flip-Flop trong thiết kế RTL.</li>
    </ul>
    <div style="text-align: center; margin-top:20px; display:flex; justify-content:center; gap:20px;">
        <img src="images/fig7_34.png" style="max-height:250px; border-radius:8px; width:45%;">
        <img src="images/fig7_36.png" style="max-height:250px; border-radius:8px; width:45%;">
    </div>
</div>'''),

    ('04_04_virtual_tester.html', '''<div class="slide">
    <h1 style="color: var(--primary-color);">Virtual Tester (ATE)</h1>
    <div style="display:flex; gap: 20px;">
        <div style="flex: 1.2;">
            <ul>
                <li>Mô phỏng ATE nạp liên tục 26 vectors, tiêm lỗi tĩnh (Fault Injection).</li>
                <li>Toán định kì: Shift-in -> Phóng Clock -> Shift-out -> Check Expected Data.</li>
                <li>Khẳng định Fault Coverage hoàn hảo trước khi sản xuất IC.</li>
            </ul>
        </div>
        <div style="flex: 0.8; text-align: center;">
            <img src="images/fig7_42.png" style="max-width:100%; border-radius:8px;">
        </div>
    </div>
</div>'''),

    ('05_01_multiple_scan_intro.html', '''<div class="slide">
    <h1 style="color: var(--primary-color);">Chương 5: Quét Đa Luồng</h1>
    <h2>Giải Hạn Chế Của Chuỗi Dài</h2>
    <div style="display:flex; gap: 20px; align-items:center;">
        <div style="flex: 1;">
            <ul>
                <li>1 chuỗi Scan với hàng triệu Flip-Flop mất quá lâu cho việc Shift tín hiệu.</li>
                <li>Công thức: Thời gian Test Time ~ $O(N_{FF})$.</li>
                <li><b>Multiple Scans:</b> Chia cắt chuỗi lớn thành $k$ luồng song song chạy cùng lúc. $N_{FF}$ giảm mạnh, $T_{Test}$ giảm cực sâu.</li>
                <li>Chi Phí: Tốn IO Pins phụ.</li>
            </ul>
        </div>
        <div style="flex: 1; text-align: center;">
            <img src="images/fig7_51.png" style="max-height:300px; border-radius:8px;">
        </div>
    </div>
</div>'''),

    ('05_02_adding_machine.html', '''<div class="slide">
    <h1 style="color: var(--primary-color);">Multiple Scan Bài Toán Adding Machine</h1>
    <div style="display:flex; gap: 20px; align-items:center;">
        <div style="flex: 1;">
            <ul>
                <li>Vi xử lý Adding Machine phân rã 3 luồng hoạt hóa độc lập:</li>
                <li><b>IR Chain:</b> 8 FFs</li>
                <li><b>AC Chain:</b> 8 FFs</li>
                <li><b>PC Chain:</b> 8 FFs</li>
                <li>Test vector time giảm sút tận 3 lần, tiết kiệm lớn thời gian nạp test trên IC Tester ATE đắt tiền.</li>
            </ul>
        </div>
        <div style="flex: 1.2; text-align: center;">
            <img src="images/scan_chain.png" style="max-width:90%; border-radius:8px; box-shadow:0 4px 6px rgba(0,0,0,0.1);">
        </div>
    </div>
</div>'''),

    ('06_01_rtl_scan.html', '''<div class="slide">
    <h1 style="color: var(--primary-color);">Chương 6: RTL Scan Optimization</h1>
    <h2>Tối Ưu Hóa Tầm Kiến Trúc Gốc</h2>
    <div style="display:flex; gap: 20px; align-items:center;">
        <div style="flex: 1;">
            <ul>
                <li><b>Partial Scan:</b> Không chèn 100% ngây ngô Gate-Level. Chủ đích nhắm DataPath bỏ Control Path giúp giảm Area Routing Overheads.</li>
                <li><b>Independent Scans:</b> Mở rộng quy mô, điều động Controller đóng vai trò buffer cho Pipeline trong quá trình kiểm thử phần DataPath. Ràng buộc thiết kế kiến trúc thông minh.</li>
            </ul>
        </div>
        <div style="flex: 1; text-align: center;">
            <img src="images/fig7_48.png" style="max-height: 180px; margin-bottom:15px;"><br>
            <img src="images/fig7_50.png" style="max-height: 180px;">
        </div>
    </div>
</div>'''),

    ('07_01_summary.html', '''<div class="slide">
    <h1 style="color: var(--primary-color);">Chương 7: Tổng Kết</h1>
    <ul>
        <li>Khoa học <b>DFT</b> quyết định sống còn tỷ lệ lỗi (Yield) của nhà máy đúc Chip. Mạch nào cũng phải được gài Test Logic.</li>
        <li><b>Scan Design</b> mang lại hiệu suất kiểm tra đột phá (đến 100% fault coverage), biến mạch tuần tự hóc búa thành các tổ hợp lôgic cô lập để sinh ATPG Vector dễ dàng.</li>
        <li>Bắt đầu đi từ Partial Scan đến Memory BIST hay Boundary Scan 1149.1 đem lại nền tảng chip SoC hiện đại.</li>
    </ul>
    <h2 style="margin-top: 50px; color:#bb0000; text-align:center;">XIN CẢM ƠN THẦY VÀ CÁC CHIẾN HỮU ĐÃ LẮNG NGHE!</h2>
</div>''')
]

for name, content in slides_data:
    with open(os.path.join(sections_dir, name), 'w', encoding='utf-8') as f:
        f.write(content)

# Update js/presentation.js
pres_js_path = 'd:/Phd/EE5217_Tue/js/presentation.js'
with open(pres_js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

js_new_list = 'const slidesList = [\n' + ',\n'.join([f"    'sections/{name}'" for name, _ in slides_data]) + '\n];'
js_content = re.sub(r'const slidesList = \[.*?\];', js_new_list, js_content, flags=re.DOTALL)

with open(pres_js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Generated {len(slides_data)} slides successfully.")
