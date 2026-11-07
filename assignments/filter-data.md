# Lọc dữ liệu:

- Dữ liệu ban đầu có nhiều trường chỉ hỏi để lấy ý kiến / quan điểm của cá nhân nên cần được loại bỏ.
- VD: Quan điểm của bạn về một công nghệ / Bạn thích làm gì khi vào Stack Overflow / Điều gì làm bạn hài lòng với công việc...

---

- Do chỉ dự đoán mức thu nhập hằng năm của lập trình viên, những người ngành khác (sinh viên, người code cho vui,...) nên cần được loại bỏ do lương của nhóm này có thể rất thấp hoặc chênh lệch lớn.
- Cột CompTotal sẽ dùng để làm nhãn, cột Currency (Đơn vị tiền tệ) cũng cần dùng để chuyển đơn vị tiền tệ trong nhãn. (CompTotal theo đơn vị USD)

## Những việc cần làm

- Đọc hiểu data
- Loại bỏ tất cả các NaN tại cột CompTotal & Currency (các giá trị \<= 0). Nếu số hàng còn lại \>10k thì vẫn oke.
- Lọc lấy lập trình viên & người có việc làm.
- Bỏ các cột không cần thiết (đã nói ở trên).
- Bỏ các cột chứa số giá trị NaN \>=50% số lượng hàng ban đầu. (Nếu cột này quan trọng thì tạm thời note lại để t xem xét)
- Lọc outlier trong cột CompTotal (nhưng người có lương cực hiếm: vài triệu USD \/ vài chục hoặc trăm đô 1 năm).
  - Cần lọc vì có thể có người gõ bừa lương / gõ thừa số 0.

# Phân công

> Ở mỗi bước lọc cần ghi số hàng / cột còn lại.

- PVTA
  - Giải thích ý nghĩa các cột 2 đến 85 (tiếng Việt, ngắn gọn) → tạo file trong docs/
  - Đề xuất cột loại bỏ + lý do (bảng: cột, giữ/bỏ, lý do) → docs/
- TH
  - Giải thích ý nghĩa của tất cả các cột từ cột 87 đến cột cuối cùng bằng tiếng việt. Viết ngắn gọn rồi tạo file trong thư mục /docs.
  - Đề xuất loại bỏ các cột không cần thiết, giải thích lý do nên bỏ những cột đó (ngắn gọn, tạo file trong /docs), và code để loại bỏ các cột đó khỏi data ban đầu.
- TA
  - Gộp hai danh sách, chốt danh sách cột loại bỏ cuối cùng.
  - Gộp các code trên & viết một script lọc duy nhất, theo thứ tự: lọc đối tượng → quy đổi USD → bỏ usd < 1000 → cắt outlier 1%-99% → tạo nhãn → bỏ hàng thiếu nhãn
  - Xử lý NaN: "None"/"Missing" cho cột phân loại, có thể xóa hàng; bỏ cột NaN > 50%

> Thời gian làm: 8/11 đến 10/11

# Note: Những việc còn lại (chưa giao)

- Liệt kê các giá trị / tần số các giá trị trong các cột sau khi lọc. Chuẩn hóa về 1 giá trị duy nhất nếu hai giá trị khác nhau có ý nghĩa giống nhau. (Text)
- Sau đó, chuyển text sang số bằng ordinal / one-hot / multi-hot encoding
