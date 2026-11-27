> Cột Currency & CompTotal k cần thiết vì đã có cột ConvertedCompYearly ở cuối (Lương quy đổi sang USD)

# Ba kịch bản lọc outlier lương

## Mục đích

- Dữ liệu lương tự khai có nhiều giá trị nhập sai, nhưng mọi cách lọc đều là giả định và có thể làm thay đổi kết quả mô hình. Vì vậy ta chạy cùng bộ mô hình trên ba cách lọc, từ ít can thiệp đến nhiều can thiệp, để kiểm tra kết luận có vững hay không.

## Bảng tổng quan

| Kịch bản | Cách lọc                                                   | Mức can thiệp | Vai trò                                    |
| -------- | ---------------------------------------------------------- | ------------- | ------------------------------------------ |
| A        | (chính) Giữ 1.000 ≤ usd ≤ 2.000.000                        | Thấp          | Kịch bản chính, ít định hướng nhất         |
| B        | A, rồi cắt phân vị 1%-99% toàn cục                         | Trung bình    | Kiểm tra độ nhạy với đuôi phân phối        |
| C        | A, rồi IQR (k = 1,5) trên log10 theo từng nước (≥ 30 dòng) | Cao           | Đối chứng, đo mức “làm đẹp” kết quả do lọc |

## Chi tiết từng kịch bản

### A: Ngưỡng tuyệt đối

```python
dA = d0[d0["usd"].between(1_000, 2_000_000)].copy()
```

- Cơ sở: dưới 1.000 USD/năm (nhập lương tháng, nhập bừa) và trên 2 triệu USD (UAH, IRR, INR nhầm đơn vị) gần như chắc chắn là lỗi.
- Ưu điểm: chỉ dựa vào chính biến lương và không dùng đặc trưng đầu vào, nên không gây thiên lệch chọn mẫu.
- Hạn chế: còn sót một số lỗi nằm trong khoảng (ví dụ người Ấn Độ chọn nhầm USD với 1,5 triệu).

### B: A + cắt 1%-99%

```python
lo, hi = dA["usd"].quantile([0.01, 0.99])
dB = dA[dA["usd"].between(lo, hi)].copy()
```

- Cơ sở: loại thêm 1% thấp nhất và 1% cao nhất, không phụ thuộc quốc gia hay đặc trưng nào.
- Ưu điểm: đơn giản, ngưỡng cố định, dễ giải thích.
- Hạn chế: luôn bỏ khoảng 2% dữ liệu dù có lỗi thật hay không.

### C: A + IQR log10 theo từng nước

- C1: lương quá cao so với kinh nghiệm, ngoài Mỹ. Loại nếu thỏa đồng thời:

```
usd > 1.000.000
ngoài Mỹ
WorkExp < 10
```

Lý do: lương trên 1 triệu USD rất hiếm. Ở Mỹ, Big Tech trả total comp (gồm cổ phiếu) cho kỹ sư cấp cao nên còn có thể thật. Ngoài Mỹ mà dưới 10 năm kinh nghiệm thì khó tin; ví dụ Ấn Độ chọn nhầm USD (1,5 và 2,5 triệu), Đức 1 triệu EUR với 4 năm kinh nghiệm.

- C2: junior lương quá cao. Loại nếu thỏa đồng thời:

```
usd > 300.000
không phải Mỹ hay Thụy Sĩ
WorkExp < 3
```

Lý do: người mới vào nghề mà lương trên 300k là rất bất thường, trừ hai nơi lương cao nhất.

- C3: IQR (k = 1,5) trên log10 theo từng nước có ≥ 30 dòng, như đã mô tả ở trên.

```python
def iqr_filter(g, k=1.5):
x = np.log10(g["usd"])
q1, q3 = x.quantile([0.25, 0.75])
iqr = q3 - q1
return g[(x >= q1 - k*iqr) & (x <= q3 + k*iqr)]

cnt = dA["Country"].value_counts()
big = cnt[cnt >= 30].index
dC = pd.concat([
dA[dA["Country"].isin(big)].groupby("Country", group_keys=False).apply(iqr_filter),
dA[~dA["Country"].isin(big)],
]).copy()
```

- Cơ sở: loại giá trị bất thường so với người cùng nước.
- Rủi ro: cắt hai đầu phân phối của từng nước nên các lớp thu nhập “sạch” hơn thực tế, accuracy có thể cao giả tạo.
- Vai trò: không dùng làm kết quả chính mà dùng để đối chứng.
