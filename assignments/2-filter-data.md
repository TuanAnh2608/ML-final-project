**Phân công nhiệm vụ lần 2**

> Hạn: 16h ngày 29/11/2026

# Lọc và xử lý dữ liệu lần 2

## Những việc đã làm

- Xóa các cột theo đề xuất. Nội dung chi tiết tại file: docs/filter-data-v1.md

## Những việc cần làm (Cần đọc file filter-data-v1.md trước)

- Dọn các giá trị lạ, chuẩn hóa, và đổi tên ngắn gọn các giá trị phục vụ cho việc trực quan.
  - VD: Cột Age 2-5 years old thì thu gọn lại thành 2-5y, 20 to 99 employees thu gọn thành 20-99y. Các cột khác tương tự và đổi tên sao cho khi encode thì tên cột hợp lệ dễ hiểu.
  - VD: Các cột chứa nhiều giá trị khác nhau thì thu gọn các giá trị có tần suất thấp lại thành nhóm other, ...
  - Thực hiện encode các cột theo phương pháp phù hợp.
  - Chuẩn hóa số.
- Xử lý Na các cột còn lại bằng phương pháp phù hợp.
- Tạo nhãn bằng phương pháp tertile.
- Chia train/test
- Giảm chiều dữ liệu sử dụng 2 phương pháp và trực quan.

## Phân công

- TH:
  - Dọn các giá trị lạ, chuẩn hóa, đổi tên ngắn gọn các giá trị của các cột từ 1 đến 12.
  - Đề xuất cách giải quyết giá trị lạ, ưu nhược điểm nếu có.
  - Thực hiện việc encode các cột: ordinal / one-hot .... Giải thích lý do.
- PVTA:
  - Dọn các giá trị lạ, chuẩn hóa, đổi tên ngắn gọn các giá trị của các cột từ 13 đến hết.
  - Đề xuất cách giải quyết giá trị lạ, ưu nhược điểm nếu có.
  - Thực hiện việc encode các cột: ordinal / one-hot .... Giải thích lý do.
- TA:
  - Tạo nhãn. Chia train test.
  - Xử lý Na tất cả các cột bằng phương pháp phù hợp.
  - Giảm chiều, trực quan dữ liệu. Bao gồm cả trực quan một số trường sau và trước khi lọc dữ liệu.

## Công việc cần làm tuần tới

- Thực hiện 2 mô hình phân loại.
- Làm báo cáo.
- Làm slide.

- 3 mô hình phân loại cần làm cho đến cuối kỳ: Softmax (Phân biệt, tuyến tính), Naive Bayes (Sinh) và SVM (Phân biệt, phi tuyến)
- 2 mô hình cần làm cho đến giữa kỳ: Softmax, NB.
  **Mn tự giác chọn mô hình mà mình sẽ làm bằng cách nhắn lên nhóm mình sẽ làm mô hình gì. Ai chọn trước sẽ có lợi hơn. Hiểu và nắm rõ phương pháp hoạt động của từng phương pháp. Khi thuyết trình, ai làm mô hình nào thì thầy sẽ hỏi kỹ mô hình đó.**
