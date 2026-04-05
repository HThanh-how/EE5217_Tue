# Kịch bản Thuyết trình - Chương 03: Chèn Điểm Kiểm Thử

## Slide 20: Mở đầu Chương 3 (03_00_chapter.html)
- **Hành động:** 
  Dừng lại vài giây để chuyển ý, giọng điệu thay đổi rành mạch.
- **Lời thoại tham khảo:**
  "Chương 3: Tìm hiểu khái niệm Khả năng điều khiển và Quan sát."

***

## Slide 21: Chèn Điểm Quan Sát (03_01_insertion.html)
- **Hành động:** 
  Chỉ tay vào cột bên trái (Cải thiện), sau đó trỏ sang cột dồn kênh MUX (Chia sẻ).
- **Lời thoại tham khảo:**
  "Bước đầu tiên là Chèn Điểm Quan sát (hay Observability Insertion). 
  Thứ nhất, về lý thuyết, ta chủ động gắn thêm đường mạch ra ngoài làm Test Points để theo dõi các node logic ẩn.
  Thứ hai, nếu cứ mang từng dây một gắn ra chân vi mạch mãi thì sẽ hết mất chân I O. Do đó, người ta dùng bộ Dồn kênh MUX. Bằng cách dùng chân Chọn Địa chỉ Address, ta chỉ cần tốn 1 chân râu cho hàng vạn tín hiệu được quan sát."

***

## Slide 22: Chèn Điểm Điều Khiển (03_02_muxdemux.html)
- **Hành động:** 
  Chỉ tay vào hình cổng AND/OR, chuyển sang hình DeMUX.
- **Lời thoại tham khảo:**
  "Tương tự như Quan sát, ta có khái niệm Chèn Điểm Điều khiển.
  Thay vì chỉ dòm ngó, ta chèn thêm cổng logic để ép cục dây dẫn về mức 0 hoặc mức 1 khi cần. Sức mạnh này vô cùng quyền lực.
  Tuy nhiên, vẫn làm sao thiếu hụt chân trên vỏ. Ta xài bộ phân nhánh demux để chia luồng kích đến vô số các điểm test thông qua cài đặt chân địa chỉ."

***

## Slide 23: Kỹ thuật Scan Nối Tiếp Cách Ly (03_03_isolated_scan.html)
- **Hành động:** 
  Nhìn sơ đồ cấu trúc Shift Register đẩy bit từng phần tử.
- **Lời thoại tham khảo:**
  "Tuy nhiên, nếu mạch quá lớn thì 2 bộ chia kênh kia sẽ khổng lồ vô tận. Rất tốn kém diện tích. Từ đó, ý tưởng Mạng quét nối tiếp ra đời. Ta quăng bỏ mạng lưới song song cồng kềnh kia, đi sài dây chuyền dịch bit. 
  Thay vì cấp vector ồ ạt, Virtual Tester sẽ thong thả đẩy dần dần từng bit một vào cổng đi Serial. Đây là nghệ thuật hi sinh tốc độ thời gian để lấy lại khoảng không gian vàng ngọc thiết kế."

***

## Slide 24: Giảm chân điều khiển & Nạp Rút đồng thời (03_04_reduce_simul.html)
- **Hành động:** 
  Để hoạt ảnh chạy lúc minh họa dòng Token và lúc Push Down / Pull up dữ liệu.
- **Lời thoại tham khảo:**
  "Đối với bài toán khổng lồ, ta dùng luôn kỹ thuật Truyền Cờ qua các thanh ghi dịch. Máy sẽ cướp nhịp của đồng hồ để cứu cánh số lượng chân trên bo mạch.
  Hơn nữa thiết kế thanh ghi rất siêu việt đa nhiệm. Nó vừa có thể lấy tín hiệu nạp vào để kích song song. Lại vừa rất nhạy bén chụp ảnh trạng thái, đẩy dần dần ra đường hầm chui để kiểm tra."

***

## Slide 25: Khái niệm cơ bản của SCAN Design (03_05_basic_scan_concept.html)
- **Hành động:** 
  Quan sát và đợi hoạt ảnh Tool thay thế con D-FF thành SD-FF. Mỉm cười.
- **Lời thoại tham khảo:**
  "Đó chính là tiền thân của SCAN Design hiện nay! Thay vì nối những thanh ghi phụ bên ngoài mạch, ta dùng chính những con Flip-Flops nội bộ của hệ thống tạo thành Scan Chain.
  Khi vận hành, chip sẽ có 2 mode: Mode thường để xài mạch bình thường, và Mode Scan để Dịch/Kiểm thử.
  Các bạn đừng quá lo lắng về việc đấu dây thủ công cực khổ này. Ngày nay, các phần mềm xịn sò như Synopsys DFT Compiler sẽ hoàn toàn tự động nhổ Flip-Flop thường đi và cấy Flip-Flop SCAN (SD-FF) vào mạch chỉ trong chớp mắt chỉ qua vài dòng code."
