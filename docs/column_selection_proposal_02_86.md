# Đề xuất giữ / bỏ cột 2–86 (PhanLab)
 
**Quy ước:** *Giữ* = dùng làm đặc trưng; *Bỏ* = loại; *Giữ tạm* = cần để lọc đối tượng hoặc tạo nhãn, sau bước đó bỏ khỏi tập đặc trưng.
 
 
**Tiêu chí:** (1) bỏ cột quan điểm / xếp hạng / sở thích cá nhân; (2) bỏ văn bản tự do; (3) bỏ cột thông tin yếu hoặc trùng lặp; (4) quy tắc NaN ≥ 50% theo hàng gốc (49.191) chỉ để tham khảo, vì sau lọc còn 16.991 dòng tỉ lệ NaN giảm nhiều.
 
**Tổng kết:** Giữ 16 cột, Giữ tạm 4 cột, Bỏ 65 cột (tổng 85).
 
**Tuấn Anh đọc kỹ dòng này nhé (quy tắc NaN ≥ 50%):** `PlatformHaveWorkedWith` (51% NaN gốc) và `WebframeHaveWorkedWith` (53%) vượt ngưỡng ở dữ liệu gốc nhưng chỉ còn 22% và 28% sau lọc, và là đặc trưng công nghệ quan trọng. Đề xuất giữ và tính ngưỡng NaN sau khi lọc đối tượng. Khi điền NaN bằng "None" cần lưu ý: ô trống ở các cột `*HaveWorkedWith` gồm cả người chọn `No` ở cột `*Choice` lẫn người không trả lời / không được hỏi, nên "None" không hẳn là "không dùng" (xem `column_selection_proposal_02_86.md`).
 
Tỉ lệ tương quan nêu ở bảng là Spearman với `CompTotal` trên mẫu dùng USD (khoảng 4.300 dòng), chỉ để tham khảo.
 
| # | Cột | Giữ/Bỏ | Lý do |
|---|---|---|---|
| 2 | `MainBranch` | Giữ tạm | Dùng để lọc "I am a developer by profession"; sau lọc chỉ còn 1 giá trị nên bỏ khỏi đặc trưng. |
| 3 | `Age` | Giữ | Liên quan tới kinh nghiệm và lương; ordinal encoding. |
| 4 | `EdLevel` | Giữ | Ảnh hưởng tới lương; ordinal encoding. |
| 5 | `Employment` | Giữ tạm | Dùng để lọc "Employed"; sau lọc hằng số nên bỏ. |
| 6 | `EmploymentAddl` | Bỏ | Chọn nhiều, 96 tổ hợp khác nhau, liên hệ với lương yếu; gánh nặng khi multi-hot. |
| 7 | `WorkExp` | Giữ | Đặc trưng quan trọng nhất (tương quan Spearman ~0,40 với lương trên mẫu USD). Cần ép sang số. |
| 8 | `LearnCodeChoose` | Bỏ | Hành vi học tập, không phản ánh mức lương; 95% trả lời cùng một vài giá trị. |
| 9 | `LearnCode` | Bỏ | Hành vi học tập, 1.673 tổ hợp, 29% NaN sau lọc, liên hệ lương yếu. |
| 10 | `LearnCodeAI` | Bỏ | Hành vi / sở thích cá nhân, không phải đặc điểm công việc. |
| 11 | `AILearnHow` | Bỏ | Chọn nhiều, 922 tổ hợp, 33% NaN sau lọc, liên hệ lương yếu. |
| 12 | `YearsCode` | Giữ | Tương quan mạnh với lương (~0,40); cần ép sang số ("Less than 1 year", "More than 50 years"). |
| 13 | `DevType` | Giữ | Vai trò ảnh hưởng rõ tới lương; gộp nhóm hiếm thành Other. |
| 14 | `OrgSize` | Giữ | Công ty lớn thường trả cao hơn; ordinal encoding. |
| 15 | `ICorPM` | Giữ | Quản lý thường lương cao hơn; ít giá trị, one-hot. |
| 16 | `RemoteWork` | Giữ | Liên quan tới lương; one-hot. |
| 17 | `PurchaseInfluence` | Giữ | Phản ánh cấp bậc / quyền hạn, là thông tin về công việc chứ không phải ý kiến. Xem xét lại nếu nhóm muốn bớt cột. |
| 18 | `TechEndorseIntro` | Bỏ | Câu dẫn cho khối ý kiến TechEndorse, không liên quan lương. |
| 19 | `TechEndorse_1` | Bỏ | Xếp hạng quan điểm cá nhân, không phải thông tin về công việc / lương. |
| 20 | `TechEndorse_2` | Bỏ | Xếp hạng quan điểm cá nhân, không phải thông tin về công việc / lương. |
| 21 | `TechEndorse_3` | Bỏ | Xếp hạng quan điểm cá nhân, không phải thông tin về công việc / lương. |
| 22 | `TechEndorse_4` | Bỏ | Xếp hạng quan điểm cá nhân, không phải thông tin về công việc / lương. |
| 23 | `TechEndorse_5` | Bỏ | Xếp hạng quan điểm cá nhân, không phải thông tin về công việc / lương. |
| 24 | `TechEndorse_6` | Bỏ | Xếp hạng quan điểm cá nhân, không phải thông tin về công việc / lương. |
| 25 | `TechEndorse_7` | Bỏ | Xếp hạng quan điểm cá nhân, không phải thông tin về công việc / lương. |
| 26 | `TechEndorse_8` | Bỏ | Xếp hạng quan điểm cá nhân, không phải thông tin về công việc / lương. |
| 27 | `TechEndorse_9` | Bỏ | Xếp hạng quan điểm cá nhân, không phải thông tin về công việc / lương. |
| 28 | `TechEndorse_13` | Bỏ | Xếp hạng quan điểm cá nhân, không phải thông tin về công việc / lương. |
| 29 | `TechEndorse_13_TEXT` | Bỏ | Văn bản tự do, 95% NaN (gốc 96%). |
| 30 | `TechOppose_1` | Bỏ | Xếp hạng quan điểm cá nhân, không liên quan lương. |
| 31 | `TechOppose_2` | Bỏ | Xếp hạng quan điểm cá nhân, không liên quan lương. |
| 32 | `TechOppose_3` | Bỏ | Xếp hạng quan điểm cá nhân, không liên quan lương. |
| 33 | `TechOppose_5` | Bỏ | Xếp hạng quan điểm cá nhân, không liên quan lương. |
| 34 | `TechOppose_7` | Bỏ | Xếp hạng quan điểm cá nhân, không liên quan lương. |
| 35 | `TechOppose_9` | Bỏ | Xếp hạng quan điểm cá nhân, không liên quan lương. |
| 36 | `TechOppose_11` | Bỏ | Xếp hạng quan điểm cá nhân, không liên quan lương. |
| 37 | `TechOppose_13` | Bỏ | Xếp hạng quan điểm cá nhân, không liên quan lương. |
| 38 | `TechOppose_16` | Bỏ | Xếp hạng quan điểm cá nhân, không liên quan lương. |
| 39 | `TechOppose_15` | Bỏ | Xếp hạng quan điểm cá nhân, không liên quan lương. |
| 40 | `TechOppose_15_TEXT` | Bỏ | Văn bản tự do, 96% NaN (gốc 97%). |
| 41 | `Industry` | Giữ | Ngành ảnh hưởng tới lương; one-hot. |
| 42 | `JobSatPoints_1` | Bỏ | Xếp hạng quan điểm / mức hài lòng; NaN gốc 49%. (JobSatPoints_11 nói về mong muốn lương cạnh tranh, không phải lương thật.) |
| 43 | `JobSatPoints_2` | Bỏ | Xếp hạng quan điểm / mức hài lòng; NaN gốc 49%. (JobSatPoints_11 nói về mong muốn lương cạnh tranh, không phải lương thật.) |
| 44 | `JobSatPoints_3` | Bỏ | Xếp hạng quan điểm / mức hài lòng; NaN gốc 49%. (JobSatPoints_11 nói về mong muốn lương cạnh tranh, không phải lương thật.) |
| 45 | `JobSatPoints_4` | Bỏ | Xếp hạng quan điểm / mức hài lòng; NaN gốc 49%. (JobSatPoints_11 nói về mong muốn lương cạnh tranh, không phải lương thật.) |
| 46 | `JobSatPoints_5` | Bỏ | Xếp hạng quan điểm / mức hài lòng; NaN gốc 49%. (JobSatPoints_11 nói về mong muốn lương cạnh tranh, không phải lương thật.) |
| 47 | `JobSatPoints_6` | Bỏ | Xếp hạng quan điểm / mức hài lòng; NaN gốc 49%. (JobSatPoints_11 nói về mong muốn lương cạnh tranh, không phải lương thật.) |
| 48 | `JobSatPoints_7` | Bỏ | Xếp hạng quan điểm / mức hài lòng; NaN gốc 49%. (JobSatPoints_11 nói về mong muốn lương cạnh tranh, không phải lương thật.) |
| 49 | `JobSatPoints_8` | Bỏ | Xếp hạng quan điểm / mức hài lòng; NaN gốc 49%. (JobSatPoints_11 nói về mong muốn lương cạnh tranh, không phải lương thật.) |
| 50 | `JobSatPoints_9` | Bỏ | Xếp hạng quan điểm / mức hài lòng; NaN gốc 49%. (JobSatPoints_11 nói về mong muốn lương cạnh tranh, không phải lương thật.) |
| 51 | `JobSatPoints_10` | Bỏ | Xếp hạng quan điểm / mức hài lòng; NaN gốc 49%. (JobSatPoints_11 nói về mong muốn lương cạnh tranh, không phải lương thật.) |
| 52 | `JobSatPoints_11` | Bỏ | Xếp hạng quan điểm / mức hài lòng; NaN gốc 49%. (JobSatPoints_11 nói về mong muốn lương cạnh tranh, không phải lương thật.) |
| 53 | `JobSatPoints_13` | Bỏ | Xếp hạng quan điểm / mức hài lòng; NaN gốc 49%. (JobSatPoints_11 nói về mong muốn lương cạnh tranh, không phải lương thật.) |
| 54 | `JobSatPoints_14` | Bỏ | Xếp hạng quan điểm / mức hài lòng; NaN gốc 49%. (JobSatPoints_11 nói về mong muốn lương cạnh tranh, không phải lương thật.) |
| 55 | `JobSatPoints_15` | Bỏ | Xếp hạng quan điểm / mức hài lòng; NaN gốc 49%. (JobSatPoints_11 nói về mong muốn lương cạnh tranh, không phải lương thật.) |
| 56 | `JobSatPoints_16` | Bỏ | Xếp hạng quan điểm / mức hài lòng; NaN gốc 49%. (JobSatPoints_11 nói về mong muốn lương cạnh tranh, không phải lương thật.) |
| 57 | `JobSatPoints_15_TEXT` | Bỏ | Văn bản tự do, 98% NaN (gốc 99%). |
| 58 | `AIThreat` | Bỏ | Quan điểm cá nhân. |
| 59 | `NewRole` | Bỏ | Ý định / hành vi cá nhân, liên hệ lương yếu. |
| 60 | `ToolCountWork` | Giữ | Tương quan Spearman ~0,14 với lương (mẫu USD); NaN 44% gốc, 15% sau lọc. Ép sang số. |
| 61 | `ToolCountPersonal` | Bỏ | Tương quan gần 0 (~0,01); NaN 25% sau lọc. |
| 62 | `Country` | Giữ | Yếu tố ảnh hưởng lương mạnh nhất; gộp nước hiếm thành Other. Nên phân tích riêng trong báo cáo. |
| 63 | `Currency` | Giữ tạm | Dùng quy đổi CompTotal sang USD; sau đó bỏ khỏi đặc trưng vì rò rỉ nhãn. |
| 64 | `CompTotal` | Giữ tạm | Là gốc để tạo nhãn thấp / trung bình / cao; không đưa vào đặc trưng. |
| 65 | `LanguageChoice` | Bỏ | Chỉ 2 giá trị (Yes/No); `No` luôn ứng với `HaveWorkedWith` trống, nên gần như trùng với cột HaveWorkedWith. |
| 66 | `LanguageHaveWorkedWith` | Giữ | Đặc trưng công nghệ thực tế; multi-hot top 15-20 mục. NaN 7% sau lọc. |
| 67 | `LanguageWantToWorkWith` | Bỏ | Nguyện vọng, không phải thực tế; NaN sau lọc cao. |
| 68 | `LanguageAdmired` | Bỏ | Bằng đúng giao của HaveWorkedWith và WantToWorkWith ở 100% dòng (trùng lặp, suy ra được); là quan điểm cá nhân; NaN gốc ≥50%. |
| 69 | `LanguagesHaveEntry` | Bỏ | Văn bản tự do, NaN gốc ≥92%. |
| 70 | `LanguagesWantEntry` | Bỏ | Văn bản tự do, NaN gốc ≥94%. |
| 71 | `DatabaseChoice` | Bỏ | Chỉ 2 giá trị (Yes/No); `No` luôn ứng với `HaveWorkedWith` trống, nên gần như trùng với cột HaveWorkedWith. |
| 72 | `DatabaseHaveWorkedWith` | Giữ | Đặc trưng công nghệ thực tế; multi-hot top 15-20 mục. NaN 21% sau lọc. |
| 73 | `DatabaseWantToWorkWith` | Bỏ | Nguyện vọng, không phải thực tế; NaN sau lọc cao. |
| 74 | `DatabaseAdmired` | Bỏ | Bằng đúng giao của HaveWorkedWith và WantToWorkWith ở 100% dòng (trùng lặp, suy ra được); là quan điểm cá nhân; NaN gốc ≥50%. |
| 75 | `DatabaseHaveEntry` | Bỏ | Văn bản tự do, NaN gốc ≥92%. |
| 76 | `DatabaseWantEntry` | Bỏ | Văn bản tự do, NaN gốc ≥94%. |
| 77 | `PlatformChoice` | Bỏ | Chỉ 2 giá trị (Yes/No); `No` luôn ứng với `HaveWorkedWith` trống, nên gần như trùng với cột HaveWorkedWith. |
| 78 | `PlatformHaveWorkedWith` | Giữ | Đặc trưng công nghệ thực tế; multi-hot top 15-20 mục. NaN gốc 51% (≥50%) nhưng chỉ 22% sau lọc; nên giữ, NaN xử lý ở bước sau. |
| 79 | `PlatformWantToWorkWith` | Bỏ | Nguyện vọng, không phải thực tế; NaN sau lọc cao. |
| 80 | `PlatformAdmired` | Bỏ | Bằng đúng giao của HaveWorkedWith và WantToWorkWith ở 100% dòng (trùng lặp, suy ra được); là quan điểm cá nhân; NaN gốc ≥50%. |
| 81 | `PlatformHaveEntry` | Bỏ | Văn bản tự do, NaN gốc ≥92%. |
| 82 | `PlatformWantEntry` | Bỏ | Văn bản tự do, NaN gốc ≥94%. |
| 83 | `WebframeChoice` | Bỏ | Chỉ 2 giá trị (Yes/No); `No` luôn ứng với `HaveWorkedWith` trống, nên gần như trùng với cột HaveWorkedWith. |
| 84 | `WebframeHaveWorkedWith` | Giữ | Đặc trưng công nghệ thực tế; multi-hot top 15-20 mục. NaN gốc 53% (≥50%) nhưng chỉ 28% sau lọc; nên giữ, NaN xử lý ở bước sau. |
| 85 | `WebframeWantToWorkWith` | Bỏ | Nguyện vọng, không phải thực tế; NaN sau lọc cao. |
| 86 | `WebframeAdmired` | Bỏ | Bằng đúng giao của HaveWorkedWith và WantToWorkWith ở 100% dòng (trùng lặp, suy ra được); là quan điểm cá nhân; NaN gốc ≥50%. |
 
## Danh sách cột bỏ
 
```python
drop_cols = [
    "EmploymentAddl",
    "LearnCodeChoose",
    "LearnCode",
    "LearnCodeAI",
    "AILearnHow",
    "TechEndorseIntro",
    "TechEndorse_1",
    "TechEndorse_2",
    "TechEndorse_3",
    "TechEndorse_4",
    "TechEndorse_5",
    "TechEndorse_6",
    "TechEndorse_7",
    "TechEndorse_8",
    "TechEndorse_9",
    "TechEndorse_13",
    "TechEndorse_13_TEXT",
    "TechOppose_1",
    "TechOppose_2",
    "TechOppose_3",
    "TechOppose_5",
    "TechOppose_7",
    "TechOppose_9",
    "TechOppose_11",
    "TechOppose_13",
    "TechOppose_16",
    "TechOppose_15",
    "TechOppose_15_TEXT",
    "JobSatPoints_1",
    "JobSatPoints_2",
    "JobSatPoints_3",
    "JobSatPoints_4",
    "JobSatPoints_5",
    "JobSatPoints_6",
    "JobSatPoints_7",
    "JobSatPoints_8",
    "JobSatPoints_9",
    "JobSatPoints_10",
    "JobSatPoints_11",
    "JobSatPoints_13",
    "JobSatPoints_14",
    "JobSatPoints_15",
    "JobSatPoints_16",
    "JobSatPoints_15_TEXT",
    "AIThreat",
    "NewRole",
    "ToolCountPersonal",
    "LanguageChoice",
    "LanguageWantToWorkWith",
    "LanguageAdmired",
    "LanguagesHaveEntry",
    "LanguagesWantEntry",
    "DatabaseChoice",
    "DatabaseWantToWorkWith",
    "DatabaseAdmired",
    "DatabaseHaveEntry",
    "DatabaseWantEntry",
    "PlatformChoice",
    "PlatformWantToWorkWith",
    "PlatformAdmired",
    "PlatformHaveEntry",
    "PlatformWantEntry",
    "WebframeChoice",
    "WebframeWantToWorkWith",
    "WebframeAdmired",
]
```
 
## Danh sách cột giữ tạm (lọc / tạo nhãn rồi bỏ)
 
```python
drop_after_use = ["MainBranch", "Employment", "Currency", "CompTotal"]
```
 
