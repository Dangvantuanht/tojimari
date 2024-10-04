⚡ Username: Tojimari
⚡ Password: H3C
    Câu Trả Lời: Quá Đẹp

<h1align="center">📡 Công cụ DoS</h1>
<div căn chỉnh="trung tâm">

<img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"> <img src="https://img.shields.io/github/forks/7zx/overload ?style=social"> <img src="https://img.shields.io/github/stars/7zx/overload?style=social">

</div>

<p căn chỉnh="trung tâm">
 <img src="img/logo.png" width="250" chiều cao="250">
</p>

<div căn chỉnh="trung tâm">
 <h1>💻 Xem trước</h1>
</div>
<p căn chỉnh="trung tâm">
 <img src="img/preview.gif">
</p>

<div căn chỉnh="trung tâm">
 <h1>Cài đặt</h1>
 <img src="img/windows.png" width="80" Height="80">
 <h2>Windows</h2><br>
</div>

Tải xuống Python 3.10 [tại đây](https://www.python.org/downloads/), mở trình cài đặt và nhấp vào `thêm python vào PATH`. Tiếp theo, tải xuống `overload` <a href="https://github.com/7zx/overload/archive/refs/heads/main.zip" target="blank">tại đây</a> và mở CMD hoặc PowerShell trong thư mục của nó. Bây giờ bạn cần tạo Môi trường ảo cho ứng dụng; nếu bạn có tiện ích `make` trên hệ thống của mình, chỉ cần thực thi:

 ```
 thực hiện thiết lập
 chạy đi
 ```

Nếu bạn không có nó, thì hãy thực hiện:

 ```
 cuộn tròn -sSL https://install.python-poetry.org | trăn3
 cài đặt thơ --không có dev
 thơ chạy python3 quá tải.py
 ```

 ---
<div căn chỉnh="trung tâm">
 <br>
 <img src="img/linux.png" width="100" Height="80"><h2>Linux</h2><br>
</div>

```
cập nhật sudo apt
sudo apt cài đặt python3 python3-pip git -y
bản sao git https://github.com/7zx/overload
quá tải cd/

thực hiện thiết lập
chạy đi
```

---
<div căn chỉnh="trung tâm">
 <br>
 <img src="img/termux.png" width="50" chiều cao="50">
 <h2>Termux</h2><br>
</div>

```
cập nhật pkg
pkg cài đặt python3 python3-pip git -y

bản sao git https://github.com/7zx/overload
quá tải cd/

cài đặt pip -r require.txt
python3 quá tải.py
```

---
<br>

<div căn chỉnh="trung tâm">
 <h2>Các cuộc tấn công có sẵn</h2><br>
</div>

`HTTP`: Cuộc tấn công này bao gồm việc làm nạn nhân kiệt sức bằng cách gửi một lượng lớn yêu cầu HTTP GET, cuối cùng gỡ bỏ nó và ngăn người khác truy cập vào tài nguyên của nó.

```
├─── CÔNG CỤ DOS
├─── CÁC PHƯƠNG PHÁP CÓ SẴN
├─── LỚP 7: HTTP | HTTP-PROXY | CHẬM | SLOWLORIS-PROXY
├───┐
│ ├───PHƯƠNG PHÁP: HTTP
│ ├───THỜI GIAN: 600
│ ├───CHỦ ĐỀ: 800
│ └───URL: https://github.com/7zx/overload
```

`Slowloris`: Giống như một cuộc tấn công HTTP, Slowloris cũng nhằm mục đích chặn người dùng khác truy cập vào một tài nguyên nhất định, nhưng nó thực hiện điều đó bằng cách kết nối các máy chủ ảo có kết nối chậm với nạn nhân. Nạn nhân cuối cùng sẽ mở rất nhiều kết nối chậm và sẽ chặn người dùng mới truy cập vào tài nguyên của nó.

```
...
├───┐
│ ├───PHƯƠNG PHÁP: CHẬM LẠI
│ ├───THỜI GIAN: 300
│ ├───CHỦ ĐỀ: 200
│ ├───THỜI GIAN NGỦ: 15
│ └───URL: https://github.com/7zx/overload
```

Cả hai cuộc tấn công `HTTP` và `Slowloris` đều có phiên bản proxy. Nếu bạn chọn sử dụng proxy thì các chuỗi sẽ khởi tạo và kết nối với các proxy công cộng ẩn danh ưu tú và nếu không, IP của bạn sẽ được sử dụng cho các yêu cầu. Chúng tôi không sở hữu máy chủ proxy và không phản hồi bất kỳ điều gì họ có thể làm (như rò rỉ IP thực của bạn); chúng được các tình nguyện viên lưu trữ và địa chỉ của chúng được truy xuất thông qua [API Proxy Scrape](https://docs.proxyscrape.com/).

<br>

## Chỉ tấn công POSIX

Để thực hiện các cuộc tấn công sau, bạn sẽ cần một máy chạy hệ thống POSIX, như Ubuntu.
<br><br>

`SYN-Flood`: Cuộc tấn công này dựa vào cách thiết kế các kết nối Giao thức kiểm soát truyền tải (TCP). Nó lợi dụng cơ chế bắt tay 3 chiều TCP (SYN, SYN-ACK và ACK) bằng cách gửi nhiều gói có cờ SYN, nhưng không bao giờ phản hồi các gói SYN-ACK do nạn nhân gửi, khiến nó phải chờ mãi mãi. với một kết nối mở. Nếu nạn nhân bằng cách nào đó không đóng kết nối được mở bởi các gói SYN thì cuối cùng nó sẽ chặn các kết nối mới.

```
...
├─── LỚP 4: ĐỒNG LŨ
├───┐
│ ├───PHƯƠNG PHÁP: SYN-FLOOD
│ ├───THỜI GIAN: 40
│ ├───CHỦ ĐỀ: 10
│ └───URL: 192.168.0.1
```

`ARP-Spoof`: Cuộc tấn công này hoạt động trên lớp 2 của mô hình OSI, cụ thể là trên Giao thức phân giải địa chỉ (ARP). Nó bao gồm việc gửi một gói giả đến nạn nhân và nói rằng chúng tôi là cổng của mạng cục bộ, vì vậy nạn nhân phải gửi tất cả các gói của nó đến máy của chúng tôi. Chúng tôi cũng nói với cổng rằng chúng tôi là nạn nhân; bằng cách đó, chúng tôi trở thành người đứng giữa kết nối và có thể kiểm tra tất cả các gói tin của nạn nhân bằng máy phân tích.

```
...
├─── LỚP 2: ARP-SPOOF | NGẮT KẾT NỐI
├───┐
│ ├─── PHƯƠNG PHÁP: ARP-SPOOF
│ │
│ ├─── [!] Đang quét mạng cục bộ...
│ │
│ ├─── Máy chủ có sẵn:
│ │
│ │ 192.168.0.102
│ │ 192.168.0.105
│ │
│ ├─── IP: 192.168.0.102
│ ├─── THỜI GIAN: 100
```

`Ngắt kết nối`: Nó chặn nạn nhân truy cập internet trên mạng cục bộ trong thời gian cuộc tấn công đang diễn ra.

```
...
├─── LỚP 2: ARP-SPOOF | NGẮT KẾT NỐI
├───┐
│ ├─── PHƯƠNG PHÁP: NGẮT KẾT NỐI
│ │
│ ├─── [!] Đang quét mạng cục bộ...
│ │
│ ├─── Máy chủ có sẵn:
│ │
│ │ 192.168.0.100
│ │ 192.168.0.103
│ │ 192.168.0.105
│ │
│ ├─── IP: 192.168.0.100
│ ├─── THỜI GIAN: 600