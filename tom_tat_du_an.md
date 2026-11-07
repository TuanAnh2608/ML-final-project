# Tóm tắt ngữ cảnh: Bài tập lớn môn Machine Learning

Ngày tạo: 31/10/2026. Dùng làm ngữ cảnh để tiếp tục ở đoạn chat khác.

---

## 1. Yêu cầu của bài tập lớn (theo thông báo của giảng viên)

### Đăng ký

- **Hạn chót đăng ký: 23:59 ngày 31/10/2026.**
- Chỉ **trưởng nhóm** đăng ký (qua Google Sheet của lớp), các thành viên khác chỉ được comment trong topic.
- Nội dung đăng ký: (1) danh sách tên thành viên, (2) link lấy dữ liệu và mô tả bài toán.
- Mỗi nhóm tối đa **3 thành viên**.
- Các nhóm phải có **dữ liệu khác nhau** và ít nhất **2 mô hình khác nhau**. Nhóm đăng ký sau bị trùng sẽ phải đổi.
- Mốc thời gian: thi giữa kỳ khoảng đầu đến giữa tháng 12/2026, thi cuối kỳ theo lịch trường.

### Sản phẩm cần nộp

1. Báo cáo (bản mềm) trình bày như một tiểu luận: đặt vấn đề, dữ liệu (mô tả, trực quan hóa, đánh giá), các phương pháp, kết quả thực nghiệm và so sánh, kết luận (tổng kết, nhận xét, khả năng cải tiến).
2. Toàn bộ chương trình thực nghiệm kèm hướng dẫn cài đặt, thiết lập dữ liệu để người đọc chạy lại được (nếu đặt trên mạng thì phải chia sẻ link đầy đủ).
3. Bản trình chiếu.
4. Tài liệu bổ sung nếu cần.

### Yêu cầu về công việc

- Thể hiện đúng quy trình dự án: xác định vấn đề, chọn dữ liệu, xử lý dữ liệu, mô hình hóa, đánh giá kết quả. Mô tả chi tiết từng bước trong báo cáo.
- Bước xử lý dữ liệu cần có: tiền xử lý (tăng cường/bổ sung, chuẩn hóa), trích xuất đặc trưng, giảm chiều, trực quan hóa.
- Bài toán chính dùng **ít nhất 3 phương pháp** khác nhau, thực nghiệm để đánh giá, so sánh, giải thích.
- Dữ liệu: không dùng lại dataset trong bài thực hành. Khuyến khích dữ liệu dạng bảng, công khai, tạo hoặc cập nhật từ **2024 trở lại**.
- Cần có phân tích, thống kê và các tham số thống kê sơ bộ của dữ liệu.
- Mô hình cho phân tích trực quan, **phân loại** (nếu được thì cả **phân cụm**).
- Thực nghiệm với **nhiều kịch bản khác nhau** (ví dụ khác tỉ lệ train/test, khác khoảng giá trị của một biến...) rồi phân tích.

---

## 2. Quyết định đã chốt

**Dataset: Stack Overflow Annual Developer Survey 2025** (Stack Exchange Inc., giấy phép ODbL 1.0, cần ghi nguồn và giữ giấy phép nếu chia sẻ lại dữ liệu phái sinh).

- Nguồn chính thức: repo `https://github.com/StackExchange/Survey` (được trang `survey.stackoverflow.co` trỏ tới). Thư mục dữ liệu: `packages/archive/2025/`, gồm `results.csv`, `schema.csv`, `survey.pdf`.
- Link tải trực tiếp: `https://github.com/StackExchange/Survey/raw/refs/heads/main/packages/archive/2025/results.csv`
- Chọn bản **2025** (không dùng thư mục 2026 vì repo ghi khảo sát 2026 đang được xây dựng, dữ liệu có thể chưa hoàn chỉnh và tên file khác).
- Lý do chọn: nhiều đặc trưng, nhiều cột đa lựa chọn và dữ liệu thiếu để làm tiền xử lý, giảm chiều; dữ liệu đủ lớn; có cả phân loại và phân cụm.
- `survey.stackoverflow.co`

### Kết quả kiểm tra dữ liệu thực tế (đã chạy)

- File `results.csv`: **49.191 dòng × 172 cột**.
- `CompTotal` là `float64`, có **24.866 dòng** không trống.
- `MainBranch` có giá trị "I am a developer by profession" (37.467 dòng). `Employment` có giá trị "Employed" (33.750 dòng). Không có nhãn "professional" hay "full-time" như dự đoán ban đầu.
- Bộ lọc đã dùng: `CompTotal > 0`, `Currency` không trống, `MainBranch == "I am a developer by profession"`, `Employment == "Employed"` → còn **16.991 dòng**.
- Phân bố mã tiền tệ sau lọc (top): EUR 4.822; USD 4.470; GBP 1.126; INR 877; CAD 654; BRL 416; AUD 399; SEK 358; PLN 335; CHF 303; UAH 275; CZK 189; DKK 173; NOK 154; ILS 132.
- Cảnh báo `DtypeWarning` khi đọc file là vô hại; dùng `low_memory=False`.

### Tỉ giá quy đổi sang USD (trung bình 2025, nguồn ECB)

1 EUR = 1,1300 USD, 0,85687 GBP, 11,0671 SEK, 24,686 CZK, 7,4634 DKK, 4,2397 PLN, 0,9370 CHF, 11,7182 NOK, 1,7517 AUD, 1,5788 CAD (bảng trung bình năm 2025 do Ngân hàng Phần Lan đăng lại số liệu ECB).

Quy đổi "USD cho 1 đơn vị tiền" (= 1,1300 / tỉ giá EUR→tiền đó): EUR 1,1300; GBP 1,3188; CAD 0,7157; AUD 0,6451; CHF 1,2060; SEK 0,1021; NOK 0,0964; DKK 0,1514; PLN 0,2665; CZK 0,0458; ILS ~0,2903 (cần kiểm tra lại).

- **INR, BRL: chưa có số**, sẽ tính bằng code từ file `eurofxref-hist.csv` của ECB (lấy trung bình năm 2025).
- **UAH**: ECB không công bố, dự kiến loại (275 dòng, khoảng 1,6%) và ghi trong phần hạn chế.

---

## 3. Mục tiêu

### Bài toán chính (phân loại)

Dự đoán **mức thu nhập hằng năm** của lập trình viên (Low / Medium / High, chia tertile sau khi quy đổi USD và lọc outlier 1%–99%) dựa trên đặc trưng như quốc gia, kinh nghiệm (`WorkExp`, `YearsCode`), loại công việc (`DevType`), quy mô công ty (`OrgSize`), học vấn (`EdLevel`), `ICorPM`, `Industry`, `RemoteWork`, `Age`, và các công nghệ sử dụng (ngôn ngữ, cơ sở dữ liệu, nền tảng, framework, công cụ AI...).

### Bài toán phụ (phân cụm)

Phân cụm lập trình viên theo công nghệ sử dụng (cột ma trận như `Language`, `Database`, `Platform`, `Webframe`, `DevEnvs`, `AIModels`), rồi phân tích lương trung bình của từng cụm.

### Phương pháp dự kiến

- Phân loại (≥ 3): Logistic Regression (hoặc KNN), Random Forest, XGBoost (hoặc SVM).
- Phân cụm: K-Means (có thể thêm DBSCAN).
- Giảm chiều và trực quan hóa: PCA, t-SNE/UMAP.

### Kế hoạch tiền xử lý dự kiến

- Phân loại ít giá trị (`RemoteWork`, `ICorPM`, `Industry`...): one-hot.
- Có thứ tự (`Age`, `OrgSize`, `EdLevel`, `JobSat`, `SOVisitFreq`...): ordinal encoding.
- Nhiều giá trị (`Country`, `DevType`): gộp nhóm hiếm thành "Other" rồi one-hot hoặc frequency/target encoding.
- Cột chọn nhiều, ngăn bởi `;` (`Language`, `Database`, `LearnCode`...): multi-hot, giữ top 15–20 mục phổ biến.
- Số lưu dạng chữ (`WorkExp`, `YearsCode`, `ToolCount*`): ép sang số, xử lý các giá trị như "Less than 1 year".
- Bỏ: các cột xếp hạng (`TechEndorse_*`, `TechOppose_*`, `JobSatPoints_*`, `SO_Actions_*`), cột văn bản tự do (`*_TEXT`, `*Entry`, `AIExplain`, `AIOpen`).
- **Không dùng `CompTotal` và `Currency` làm đặc trưng** (rò rỉ nhãn).
- Chia train/test **trước** khi fit encoder/scaler. Chuẩn hóa cho LR, KNN, K-Means; không cần cho Random Forest/XGBoost.
- Loại freelancer (`Employment` khác "Employed") để lương ổn định hơn; ghi vào phần hạn chế.

### Kịch bản thực nghiệm đề xuất

- Tỉ lệ train/test: 70/30 và 80/20.
- Có và không giảm chiều (PCA).
- Có và không cân bằng lớp (nếu lớp lệch).
- Toàn bộ dữ liệu so với một nhóm nước (ví dụ chỉ Mỹ, hoặc loại biến `Country`) để xem ảnh hưởng của quốc gia.

### Điểm nên viết trong báo cáo

- Hạn chế dữ liệu: người trả lời là nhóm tự chọn, thiên về người dùng Stack Overflow tích cực, không đại diện toàn bộ lập trình viên.
- Giả định tỉ giá trung bình năm 2025 và việc loại UAH, freelancer, outlier.
- `Country` có thể dự đoán rất mạnh nên nên phân tích riêng.
- Sau one-hot/multi-hot có thể lên hàng trăm đến hơn 1.000 cột, đây là lý do chính đáng cho giảm chiều.
- Ghi nguồn và giấy phép ODbL.

### Bản nháp mô tả đăng ký

> **Dữ liệu:** Stack Overflow Annual Developer Survey 2025 (Stack Exchange Inc., giấy phép ODbL), ~49.000 phản hồi từ 177 quốc gia. Link: https://github.com/StackExchange/Survey/tree/main/packages/archive/2025
> **Bài toán:** Phân loại mức thu nhập hằng năm của lập trình viên (thấp / trung bình / cao) dựa trên kinh nghiệm, quốc gia, công nghệ sử dụng và trình độ. Phân cụm các nhóm lập trình viên theo công nghệ họ dùng.
> **Phương pháp:** Logistic Regression, Random Forest, XGBoost (phân loại); K-Means (phân cụm); PCA/t-SNE (giảm chiều).

(Cần cập nhật số dòng thực tế sau khi quy đổi và lọc outlier.)

---

## 4. Những điều cần xác nhận, làm rõ

### Gấp (trước 23:59 hôm nay)

1. **Kiểm tra file đăng ký của lớp** xem nhóm khác đã chọn dataset này, hoặc cùng mô hình chưa. Nếu trùng: đổi biến mục tiêu (gợi ý `JobSat`, `RemoteWork`, `AIThreat`, `DevType`) và/hoặc đổi bộ mô hình.
2. **Danh sách thành viên nhóm** (tối đa 3) và ai là trưởng nhóm để đăng ký.
3. **Chốt biến mục tiêu và bộ ≥ 3 mô hình** để ghi vào đăng ký.

### Về dữ liệu

4. Vì sao bạn từng thấy "khoảng 29k bản ghi" trong khi file có 49.191 dòng (có thể do xem trên công cụ lọc/xem trước)? Cần xác nhận đang dùng đúng file `results.csv` 2025.
5. Schema đã dán có khoảng 139 mục nhưng file có 172 cột. Cần chạy `df.columns.tolist()` xem 33 cột còn lại là gì, và **có cột lương đã quy đổi USD sẵn không** (kiểu `ConvertedComp...`). Nếu có thì khỏi tự quy đổi.
6. Cột có thứ tự và cách mã hóa các giá trị đặc biệt (`WorkExp`, `YearsCode`, `Age`, `OrgSize`...) cần xem `value_counts` để lập bảng ánh xạ.

### Về quy đổi lương và nhãn

7. Lấy tỉ giá trung bình 2025 cho **INR, BRL, ILS** từ file ECB `eurofxref-hist.csv` (và xác nhận lại ILS ~0,2903).
8. Xác nhận loại **UAH** và các mã tiền tệ không có tỉ giá.
9. Sau quy đổi và lọc 1%–99%: số dòng còn lại, phân bố ba lớp `income_class`, kết quả `describe()` của `usd`.
10. Có loại thêm lương rất thấp (dưới khoảng 1.000 USD/năm) không.
11. Giữ hay bỏ freelancer (hiện đề xuất bỏ; nếu số dòng quá ít mới thêm).
12. Xử lý ảnh hưởng của `Country` (giữ nguyên, chia nhãn theo nhóm nước, hay làm kịch bản riêng).

### Về mô hình và báo cáo

13. Chọn cụ thể bộ 3 phương pháp phân loại và có làm phân cụm không (đề bài là "nếu được").
14. Chốt các kịch bản thực nghiệm sẽ so sánh.
15. Công cụ và môi trường (Python, notebook, thư viện) và cách đóng gói hướng dẫn cài đặt để người chấm chạy lại.

---

## 5. Ghi chú kỹ thuật đã dùng

Đọc và lọc:

```python
import pandas as pd

df = pd.read_csv("Survey/packages/archive/2025/results.csv", low_memory=False)

d = df[
    df["CompTotal"].notna() & (df["CompTotal"] > 0)
    & df["Currency"].notna()
    & (df["MainBranch"] == "I am a developer by profession")
    & (df["Employment"] == "Employed")
].copy()
d["CurrencyCode"] = d["Currency"].str[:3]
print(len(d))  # 16991
```

Quy đổi USD từ ECB (cần file `eurofxref-hist.csv`):

```python
fx = pd.read_csv("eurofxref-hist.csv")
fx["Date"] = pd.to_datetime(fx["Date"])
fx25 = fx[fx["Date"].dt.year == 2025].drop(columns="Date")
eur_per = fx25.mean(numeric_only=True)
usd_per_unit = (eur_per["USD"] / eur_per).to_dict()
usd_per_unit["EUR"] = eur_per["USD"]
usd_per_unit["USD"] = 1.0

d["usd"] = d["CompTotal"] * d["CurrencyCode"].map(usd_per_unit)
d = d[d["usd"].notna()]

lo, hi = d["usd"].quantile([0.01, 0.99])
d = d[(d["usd"] >= lo) & (d["usd"] <= hi)]
d["income_class"] = pd.qcut(d["usd"], q=3, labels=["Low", "Medium", "High"])
```
