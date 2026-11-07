# Mục tiêu

- Bài toán chính là bài toán phân loại, các phương pháp dự kiến dùng: NB, logistic/softmax, svm.
- Phân loại lương của Dev mức: thấp / tb / cao.

# Cấu trúc thư mục

- code và db nằm trong thư mục src
- data: src/datasets
  - Do file gốc ~134MB nên k thể tải lên github được, mn hãy tự tải data về máy theo nguồn ở dưới.
  - link repo: [Click here](https://github.com/StackExchange/Survey/tree/main/packages/archive/2025)
  - cách tải, chạy lệnh sau, data sẽ nằm trong packages/archive/2025, lấy 2 file result vs schema ra rồi xóa hết đống file còn lại nếu muốn:

  ```
  git clone --filter=blob:none --no-checkout https://github.com/StackExchange/Survey.git
  cd Survey
  git sparse-checkout set packages/archive/2025
  git checkout main
  ```

  - result.csv file data gốc, sẽ làm việc trên file này.
  - schema.csv giải thích ý nghĩa các trường trong data.

- code: src/code
  - Code của nhóm sẽ ở trong thư mục này

- note: src/notes
  - Ghi note vào trong đây để cho mn đọc nếu cần (có thể sẽ dùng khi làm báo cáo)

- file tom_tat_du_an.md do em Claude tạo, chỉ mang tính chất định hướng tham khảo. Trong quá trình làm chắc chắn sẽ có thay đổi.
