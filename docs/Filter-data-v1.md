# Lọc dữ liệu

> Quá trình lọc nằm trong 4 file (Đánh số từ 1-4) tại /src/share. Thư mục này chứa code chung cả nhóm.

**Cần đọc kỹ file này để xem đã làm những gì**

1. Xóa các cột cần thiết. (File 1)

- Xóa các cột trong đề xuất.
- Xóa 2 cột: Currency và CompTotal (Lương và loại tiền tệ) do đã có cột ConvertedCompYearly ở cuối (Đã chuyển sang USD).

2. Xóa NaN cột ConvertedCompYearly, lọc Developer, lọc Employed. (File 2)
3. Lọc outlier cột ConvertedCompYearly

- Loại cột lương < 3000 và > 1.000.000

4. Loại bỏ các dòng 'Prefer not to say' trong Age (8 mẫu) (File 3)
5. Lọc outlier cho cột WorkExp

- Quy tắc: Trong code 3_outlier.py

6. Lọc outliler cho YearsCode

- Quy tắc: Trong code 3_outlier.py

7. Clip số lượng tool đã dùng xuống còn max 50.
8. Kiểm tra tỷ lệ Na ở các cột.

- Không có cột nào tỷ lệ hơn 50%. Không cần xóa cột nào nữa.

9. Xử lý các giá trị Na (File 4)

```
Số lượng mẫu:  16090
Số lượng giá trị NaN trong từng cột:
Age                                  0
EdLevel                             10
WorkExp                            125
YearsCode                           48
DevType                              0
OrgSize                             11
ICorPM                             226
RemoteWork                          76
PurchaseInfluence                   26
Industry                            21
ToolCountWork                     2393
Country                              0
LanguageHaveWorkedWith            1001
DatabaseHaveWorkedWith            3297
PlatformHaveWorkedWith            3501
WebframeHaveWorkedWith            4418
DevEnvsHaveWorkedWith             3001
OpSysPersonal use                 1105
OpSysProfessional use             1824
OfficeStackAsyncHaveWorkedWith    1428
AIModelsHaveWorkedWith            7829
AISelect                           384
AIAgents                           895
ConvertedCompYearly                  0
```

- Các cột: \*HaveWorkedWith và OpSys\* thay Na thành "" (Chuỗi rỗng).
  - Lý do: Chuỗi rỗng = danh sách rỗng. Khi multi-hot sẽ thành 0

- Xử lý cột số WorkExp: WorkExp và YearsCode: Có 11 dòng cả 2 cột đều Na, 114 dòng có WorkExp là Na.
  - Xử lý: Điền Na WorkExp bằng 0 tại cột từ 18-24 tuổi - 0 năm kinh nghiệm. Tần suất xuất hiện độ tuổi 18-24 là 85. (Do những người mới ra trường / <1 kinh nghiệm thường k điền cột này.)
  - Còn lại: Xóa hết dòng Na trong WorkExp do không có căn cứ rõ ràng để điền.

- Xử lý Na cột AISelect và AIAgents bằng cách điền bằng "Unknown"
  - Giúp giữ được thông tin: Không trả lời - có thể được coi là một nhóm riêng

- Các cột còn lại chưa xử lý Na. Cần chia train test trước, xử lý Na bằng phương pháp thống kê.

```
EdLevel                             10
YearsCode                           39
OrgSize                             10
ICorPM                             223
RemoteWork                          75
PurchaseInfluence                   24
Industry                            20
ToolCountWork                     2379
```

---

- Chạy lần lượt các file đã đánh số để lấy được dataset cuối cùng. (Nhớ sửa đường dẫn)
- Dữ liệu cuối cùng sau lọc:
  - 16050 x 24 (Hàng x Cột)
  - 4 cột dạng số (1 cột để tạo nhãn), 20 cột còn lại dạng chữ - lựa chọn.
  - Số trường đặc trưng: 23. Do đó, tập dữ liệu đã đạt đủ điều kiện. (Đọc kỹ lại điều kiện tại file đề xuất dự án nếu k biết)
