# Ý nghĩa các cột 2–86 (PhanLab)

Nguồn: `schema.csv` (lời dẫn câu hỏi) và `results.csv` (các giá trị thực tế, đếm trên toàn bộ 49.191 dòng, chưa lọc). Cột 1 là `ResponseId` (không nằm trong tài liệu này). Số thứ tự là vị trí cột trong `results.csv`.

**Cách đọc:** *chọn một* = mỗi dòng có đúng 1 giá trị; *chọn nhiều* = ô chứa nhiều lựa chọn nối bằng `;`; *xếp hạng* = giá trị là thứ hạng (1 = quan trọng nhất); *văn bản tự do* = người trả lời tự gõ. Ô trống (NaN) nghĩa là không trả lời hoặc không được hỏi câu đó. Giá trị liệt kê theo thứ tự từ nhiều đến ít người chọn (trừ các cột có thứ tự tự nhiên như tuổi, quy mô công ty). Các giá trị giữ nguyên tiếng Anh để khớp với dữ liệu khi code.

> `schema.csv` **không có** lời dẫn cho các cột `*HaveWorkedWith`, `*WantToWorkWith`, `*Admired` (cột 66–68, 72–74, 78–80, 84–86). Phần giải thích các cột này dựa trên tên cột và lời dẫn của cột `*Choice` / `*Entry` cùng nhóm, đã được kiểm tra bằng dữ liệu (xem từng mục).

---

## A. Thông tin cá nhân và công việc (cột 2–17)

### 2. `MainBranch` — Mô tả bản thân có viết code không

- **Lời dẫn (schema):** "Are you someone who writes code? Please select one of the following options that best describes you today."
  - Dịch: Bạn có phải người viết code không? Chọn mô tả đúng nhất với bạn hiện nay.
- **Kiểu:** chọn **một** đáp án · **6 giá trị**
- **Các giá trị:**
  1. `I am a developer by profession` — Là lập trình viên chuyên nghiệp
  2. `I am not primarily a developer, but I write code sometimes as part of my work/studies` — Không chủ yếu là dev, nhưng thỉnh thoảng viết code trong công việc/học tập
  3. `I am learning to code` — Đang học code
  4. `I code primarily as a hobby` — Code chủ yếu để giải trí
  5. `I used to be a developer by profession, but no longer am` — Từng là dev chuyên nghiệp, hiện không còn
  6. `I work with developers or my work supports developers but am not a developer by profession` — Làm việc cùng/hỗ trợ dev nhưng không phải dev
- **Lưu ý:** Dùng để lọc đối tượng: giữ `I am a developer by profession` (37.467 dòng).

### 3. `Age` — Nhóm tuổi

- **Lời dẫn (schema):** "What is your age?"
  - Dịch: Bạn bao nhiêu tuổi?
- **Kiểu:** chọn **một** đáp án · **7 giá trị**
- **Các giá trị:**
  1. `18-24 years old` — 18–24 tuổi
  2. `25-34 years old` — 25–34 tuổi
  3. `35-44 years old` — 35–44 tuổi
  4. `45-54 years old` — 45–54 tuổi
  5. `55-64 years old` — 55–64 tuổi
  6. `65 years or older` — từ 65 tuổi trở lên
  7. `Prefer not to say` — không muốn nói
- **Lưu ý:** Có thứ tự (6 mức đầu); `Prefer not to say` không có thứ tự, nên xử lý riêng khi ordinal encoding. Không có nhóm dưới 18 tuổi.

### 4. `EdLevel` — Trình độ học vấn cao nhất đã hoàn thành

- **Lời dẫn (schema):** "Which of the following best describes the highest level of formal education that you’ve completed?"
  - Dịch: Mô tả đúng nhất trình độ học vấn chính quy cao nhất bạn đã hoàn thành.
- **Kiểu:** chọn **một** đáp án · **8 giá trị**
- **Các giá trị:**
  1. `Primary/elementary school` — Tiểu học
  2. `Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)` — Trung học
  3. `Some college/university study without earning a degree` — Đã học đại học/cao đẳng nhưng chưa lấy bằng
  4. `Associate degree (A.A., A.S., etc.)` — Bằng cao đẳng (associate)
  5. `Bachelor’s degree (B.A., B.S., B.Eng., etc.)` — Cử nhân
  6. `Master’s degree (M.A., M.S., M.Eng., MBA, etc.)` — Thạc sĩ
  7. `Professional degree (JD, MD, Ph.D, Ed.D, etc.)` — Bằng chuyên môn / tiến sĩ
  8. `Other (please specify):` — Khác
- **Lưu ý:** Có thứ tự từ thấp lên cao (7 mức đầu); `Other` không có thứ tự.

### 5. `Employment` — Tình trạng việc làm

- **Lời dẫn (schema):** "Which of the following best describes your current employment status?"
  - Dịch: Mô tả đúng nhất tình trạng việc làm hiện tại của bạn.
- **Kiểu:** chọn **một** đáp án · **6 giá trị**
- **Các giá trị:**
  1. `Employed` — Đang đi làm (nhân viên)
  2. `Independent contractor, freelancer, or self-employed` — Làm tự do / thầu độc lập / tự kinh doanh
  3. `Student` — Sinh viên
  4. `Not employed` — Không có việc làm
  5. `Retired` — Đã nghỉ hưu
  6. `I prefer not to say` — Không muốn nói
- **Lưu ý:** Dùng để lọc: giữ `Employed` (33.750 dòng).

### 6. `EmploymentAddl` — Các hoạt động bổ sung đang tham gia

- **Lời dẫn (schema):** "Which of the following additional activities are you currently engaged in?"
  - Dịch: Bạn hiện đang tham gia các hoạt động bổ sung nào sau đây?
- **Kiểu:** chọn **nhiều** đáp án, trong ô nối nhau bằng dấu `;` · **9 lựa chọn**
- **Các lựa chọn:**
  1. `None of the above` — Không có hoạt động nào
  2. `Caring for dependents (children, elderly, etc.)` — Chăm sóc người phụ thuộc (con nhỏ, người già...)
  3. `Engaged in paid work (20-29 hours per week)` — Làm thêm có lương 20–29 giờ/tuần
  4. `Volunteering (regularly)` — Tình nguyện thường xuyên
  5. `Attending school (full-time)` — Đi học toàn thời gian
  6. `Engaged in paid work (less than 10 hours per week)` — Làm thêm có lương dưới 10 giờ/tuần
  7. `Attending school (part-time)` — Đi học bán thời gian
  8. `Engaged in paid work (10-19 hours per week)` — Làm thêm có lương 10–19 giờ/tuần
  9. `Transitioning to retirement (gradually reducing work hours)` — Đang chuyển dần sang nghỉ hưu (giảm giờ làm)

### 7. `WorkExp` — Số năm kinh nghiệm làm việc chuyên nghiệp

- **Lời dẫn (schema):** "How many years of professional work experience do you have? Please round to the nearest whole number, excluding any decimal points. If your answer is '0', please leave blank."
  - Dịch: Bạn có bao nhiêu năm kinh nghiệm làm việc chuyên nghiệp? Làm tròn số nguyên, không tính phần thập phân. Nếu là 0 thì để trống.
- **Kiểu:** số nguyên nhập tay (kiểu `TE`)
- **Giá trị:** số (thực tế lưu dạng float); 42.893 dòng có giá trị; 72 giá trị khác nhau; nhỏ nhất 1, lớn nhất 100, trung vị 10
- **Lưu ý:** Đáp án `0` được yêu cầu **để trống**, nên NaN ở cột này có thể là 0 năm chứ không chỉ là không trả lời.

### 8. `LearnCodeChoose` — Có học code / kỹ năng mới trong năm qua không

- **Lời dẫn (schema):** "Did you begin learning to code or learn a new coding skill/programming language in the last year?"
  - Dịch: Bạn có bắt đầu học code hoặc học một kỹ năng/ngôn ngữ lập trình mới trong năm qua không?
- **Kiểu:** chọn **một** đáp án · **3 giá trị**
- **Các giá trị:**
  1. `Yes, I am not new to coding but am learning new coding techniques or programming language` — Có, không mới với code nhưng học kỹ thuật/ngôn ngữ mới
  2. `No, I am not new to coding and did not learn new coding techniques or programming languages` — Không, không mới với code và không học thêm gì
  3. `Yes, I am new to coding or currently a student` — Có, mới học code hoặc đang là sinh viên

### 9. `LearnCode` — Cách học code trong năm qua

- **Lời dẫn (schema):** "How did you learn to code in the past year? Select all that apply."
  - Dịch: Bạn đã học code bằng cách nào trong năm qua? Chọn tất cả đáp án phù hợp.
- **Kiểu:** chọn **nhiều** đáp án, trong ô nối nhau bằng dấu `;` · **13 lựa chọn**
- **Các lựa chọn:**
  1. `Technical documentation (is generated for/by the tool or system)` — Tài liệu kỹ thuật
  2. `Other online resources (e.g. standard search, forum, online community)` — Nguồn online khác (tìm kiếm, diễn đàn, cộng đồng)
  3. `Stack Overflow or Stack Exchange` — Stack Overflow / Stack Exchange
  4. `Videos (not associated with specific online course or certification)` — Video (không thuộc khóa học cụ thể)
  5. `AI CodeGen tools or AI-enabled apps` — Công cụ AI sinh code / ứng dụng AI
  6. `Blogs or podcasts` — Blog hoặc podcast
  7. `Online Courses or Certification (includes all media types)` — Khóa học / chứng chỉ online
  8. `Books / Physical media` — Sách / tài liệu in
  9. `Colleague or on-the-job training` — Đồng nghiệp / đào tạo tại chỗ
  10. `School (i.e., University, College, etc)` — Trường học
  11. `Games or coding challenges` — Game / thử thách code
  12. `Coding Bootcamp` — Bootcamp
  13. `Other (please specify):` — Khác

### 10. `LearnCodeAI` — Có học AI / công cụ AI trong năm qua không

- **Lời dẫn (schema):** "Did you spend time in the last year learning AI programming or AI-enabled tooling on your own or at work?"
  - Dịch: Trong năm qua bạn có dành thời gian học lập trình AI hoặc công cụ AI, tự học hay ở chỗ làm?
- **Kiểu:** chọn **một** đáp án · **5 giá trị**
- **Các giá trị:**
  1. `Yes, I learned how to use AI-enabled tools required for my job or to benefit my career` — Có, học công cụ AI vì công việc / sự nghiệp
  2. `Yes, I learned how to use AI-enabled tools for my personal curiosity and/or hobbies` — Có, học công cụ AI vì tò mò / sở thích
  3. `No, I learned something that was not related to AI or AI enablement for my personal curiosity and/or hobbies` — Không, học thứ khác (không liên quan AI) vì sở thích
  4. `No, I didn't spend time learning in the past year` — Không, năm qua không học gì
  5. `No, I learned something that was not related to AI or AI enablement as required for my job or to benefit my career` — Không, học thứ khác (không liên quan AI) vì công việc

### 11. `AILearnHow` — Cách học code cho AI trong năm qua

- **Lời dẫn (schema):** "How did you learn to code for AI in the past year? Select all that apply."
  - Dịch: Bạn đã học code cho AI bằng cách nào trong năm qua? Chọn tất cả đáp án phù hợp.
- **Kiểu:** chọn **nhiều** đáp án, trong ô nối nhau bằng dấu `;` · **13 lựa chọn**
- **Các lựa chọn:**
  1. `AI CodeGen tools or AI-enabled apps` — Công cụ AI sinh code / ứng dụng AI
  2. `Other online resources (e.g. standard search, forum, online community)` — Nguồn online khác
  3. `Technical documentation (is generated for/by the tool or system)` — Tài liệu kỹ thuật
  4. `Videos (not associated with specific online course or certification)` — Video
  5. `Blogs or podcasts` — Blog hoặc podcast
  6. `Colleague or on-the-job training` — Đồng nghiệp / đào tạo tại chỗ
  7. `Stack Overflow or Stack Exchange` — Stack Overflow / Stack Exchange
  8. `Online Courses or Certification (includes all media types)` — Khóa học / chứng chỉ online
  9. `Books / Physical media` — Sách / tài liệu in
  10. `School (i.e., University, College, etc)` — Trường học
  11. `Other (please specify):` — Khác
  12. `Games or coding challenges` — Game / thử thách code
  13. `Coding Bootcamp` — Bootcamp
- **Lưu ý:** Cùng danh sách 13 lựa chọn với `LearnCode`.

### 12. `YearsCode` — Tổng số năm code (tính cả học tập)

- **Lời dẫn (schema):** "Including any education, how many years have you been coding in total? Please round to the nearest whole number, excluding any decimal points."
  - Dịch: Tính cả thời gian học, bạn đã code tổng cộng bao nhiêu năm? Làm tròn số nguyên.
- **Kiểu:** số nguyên nhập tay (kiểu `TE`)
- **Giá trị:** số (thực tế lưu dạng float); 43.042 dòng có giá trị; 78 giá trị khác nhau; nhỏ nhất 1, lớn nhất 100, trung vị 14

### 13. `DevType` — Loại công việc hiện tại

- **Lời dẫn (schema):** "Which of the following describes your current job or the job you had for the most time in the past year?"
  - Dịch: Mô tả công việc hiện tại, hoặc công việc bạn làm lâu nhất trong năm qua.
- **Kiểu:** chọn **một** đáp án · **32 giá trị**
- **Các giá trị:** `Developer, full-stack`; `Developer, back-end`; `Student`; `Architect, software or solutions`; `Developer, front-end`; `Developer, desktop or enterprise applications`; `Other (please specify):`; `Developer, mobile`; `Developer, embedded applications or devices`; `Academic researcher`; `Engineering manager`; `DevOps engineer or professional`; `Data engineer`; `AI/ML engineer`; `Data scientist`; `Senior executive (C-suite, VP, etc.)`; `System administrator`; `Retired`; `Developer, game or graphics`; `Cloud infrastructure engineer`; `Founder, technology or otherwise`; `Cybersecurity or InfoSec professional`; `Data or business analyst`; `Developer, QA or test`; `Project manager`; `Applied scientist`; `Support engineer or analyst`; `Developer, AI apps or physical AI`; `Product manager`; `Database administrator or engineer`; `UX, Research Ops or UI design professional`; `Financial analyst or engineer`
- **Lưu ý:** Trong 32 giá trị có cả `Student`, `Retired`, `Academic researcher` (không phải dev đi làm) và `Other (please specify):`.

### 14. `OrgSize` — Quy mô công ty

- **Lời dẫn (schema):** "Approximately how many people are employed by your employer? This should only include your primary company, and if there was more than one employer please consider the one you spent most of your time working for in the past year."
  - Dịch: Công ty bạn làm việc có khoảng bao nhiêu nhân viên? Chỉ tính công ty chính (nếu có nhiều nơi thì chọn nơi làm lâu nhất năm qua).
- **Kiểu:** chọn **một** đáp án · **9 giá trị**
- **Các giá trị:**
  1. `Just me - I am a freelancer, sole proprietor, etc.` — Chỉ mình tôi (freelancer, tự kinh doanh)
  2. `Less than 20 employees` — Dưới 20 người
  3. `20 to 99 employees` — 20–99 người
  4. `100 to 499 employees` — 100–499 người
  5. `500 to 999 employees` — 500–999 người
  6. `1,000 to 4,999 employees` — 1.000–4.999 người
  7. `5,000 to 9,999 employees` — 5.000–9.999 người
  8. `10,000 or more employees` — từ 10.000 người trở lên
  9. `I don’t know` — Không biết
- **Lưu ý:** Có thứ tự tăng dần theo quy mô (8 mức đầu); `I don’t know` không có thứ tự.

### 15. `ICorPM` — Cá nhân đóng góp hay quản lý

- **Lời dẫn (schema):** "Are you an individual contributor or people manager?"
  - Dịch: Bạn là cá nhân đóng góp (IC) hay quản lý nhân sự?
- **Kiểu:** chọn **một** đáp án · **2 giá trị**
- **Các giá trị:**
  1. `Individual contributor` — Cá nhân đóng góp (không quản lý người)
  2. `People manager` — Quản lý nhân sự

### 16. `RemoteWork` — Hình thức làm việc

- **Lời dẫn (schema):** "Which best describes your current work situation?"
  - Dịch: Mô tả đúng nhất tình hình làm việc hiện tại của bạn.
- **Kiểu:** chọn **một** đáp án · **5 giá trị**
- **Các giá trị:**
  1. `Remote` — Làm từ xa hoàn toàn
  2. `Hybrid (some remote, leans heavy to in-person)` — Hybrid, nghiêng về đến văn phòng
  3. `In-person` — Làm tại văn phòng
  4. `Hybrid (some in-person, leans heavy to flexibility)` — Hybrid, nghiêng về linh hoạt
  5. `Your choice (very flexible, you can come in when you want or just as needed)` — Tự chọn (rất linh hoạt, đến khi muốn/cần)

### 17. `PurchaseInfluence` — Mức ảnh hưởng tới việc mua công nghệ

- **Lời dẫn (schema):** "Have you influenced or endorsed a new technology purchase at your organization or sole proprietor job in the past year?"
  - Dịch: Trong năm qua bạn có tác động hoặc ủng hộ việc mua một công nghệ mới ở tổ chức (hoặc công việc tự kinh doanh) của mình không?
- **Kiểu:** chọn **một** đáp án · **5 giá trị**
- **Các giá trị:**
  1. `No` — Không
  2. `Yes, I influenced the purchase of a substantial addition to the tech stack` — Có, tác động tới việc mua một bổ sung đáng kể cho tech stack
  3. `Yes, I endorsed a tool that was open-source and is currently used by more than just myself but no purchase was made` — Có, ủng hộ một công cụ mã nguồn mở đang được nhiều người dùng (không phát sinh mua)
  4. `Yes, I influenced the purchase of a tool that more than five colleagues use but it is not a substantial addition to the tech stack` — Có, tác động tới việc mua công cụ >5 đồng nghiệp dùng (không phải bổ sung lớn)
  5. `Yes, I endorsed a tool that was ultimately not purchased or used at my organization` — Có, ủng hộ một công cụ nhưng cuối cùng không được mua/dùng

---

## B. Khối xếp hạng về công nghệ (cột 18–40)

### 18. `TechEndorseIntro` — Bối cảnh khi chọn / ủng hộ công nghệ

- **Lời dẫn (schema):** "When you’re in a position to influence or endorse a technology , whether at work, for school, or for a personal project you’re responsible for, what features or attributes matter most when deciding to support a tool? What factors would be deal-breakers? First, select the context (work, school, personal project). Then, rank the following features in order of importance.​​​​​​"
  - Dịch: Khi bạn ở vị trí có thể tác động hoặc ủng hộ một công nghệ (ở chỗ làm, trường học hoặc dự án cá nhân), những tính năng nào quan trọng nhất? Điều gì là "điểm chặn"? Trước hết chọn bối cảnh (công việc, trường học, dự án cá nhân), sau đó xếp hạng các tính năng theo mức quan trọng.
- **Kiểu:** chọn **một** đáp án · **3 giá trị**
- **Các giá trị:**
  1. `Work` — Công việc
  2. `Personal Project` — Dự án cá nhân
  3. `School` — Trường học
- **Lưu ý:** Đây là câu chọn bối cảnh cho khối `TechEndorse_*` và `TechOppose_*` bên dưới.

### 19–28. `TechEndorse_1` … `TechEndorse_13` — Điều thu hút / khiến ủng hộ một công nghệ

- **Lời dẫn (schema):** "What attracts you to a technology or causes you to endorse it (most to least important)?"
  - Dịch: Điều gì thu hút bạn tới một công nghệ hoặc khiến bạn ủng hộ nó (từ quan trọng nhất đến ít quan trọng nhất)?
- **Kiểu:** xếp hạng · mỗi cột là một mục trong danh sách; giá trị là thứ hạng của mục đó. **14 giá trị** (số nguyên từ 1 đến 14, 1 = quan trọng nhất, lưu dạng float như `3.0`).
- **Số dòng có trả lời:** 35.975
- **Lưu ý:** Schema chỉ liệt kê 10 mục nhưng thứ hạng quan sát được lên tới 14, nghĩa là danh sách gốc có nhiều mục hơn số cột trong file. Ở `TechEndorse_13` (mục "Khác"), hầu hết người trả lời để nguyên thứ hạng 10, nên mục này gần như không mang thông tin.

| # | Cột | Mục được xếp hạng (EN) | Tiếng Việt |
|---|---|---|---|
| 19 | `TechEndorse_1` | AI integration or AI Agent capabilities | Tích hợp AI / AI Agent |
| 20 | `TechEndorse_2` | Easy-to-use API | API dễ dùng |
| 21 | `TechEndorse_3` | Robust and complete API | API đầy đủ, mạnh |
| 22 | `TechEndorse_4` | Customizable and manageable codebase | Mã nguồn dễ tùy chỉnh, dễ quản lý |
| 23 | `TechEndorse_5` | Reputation for quality | Uy tín về chất lượng |
| 24 | `TechEndorse_6` | Connected to an open-source project | Gắn với dự án mã nguồn mở |
| 25 | `TechEndorse_7` | Good brand and public image | Thương hiệu và hình ảnh tốt |
| 26 | `TechEndorse_8` | Reliability and low latency | Độ tin cậy và độ trễ thấp |
| 27 | `TechEndorse_9` | Costs are manageable | Chi phí hợp lý |
| 28 | `TechEndorse_13` | Other (please specify): | Lý do khác |

### 29. `TechEndorse_13_TEXT` — Nội dung gõ tay cho mục "Khác" của TechEndorse

- **Lời dẫn (schema):** "What attracts you to a technology or causes you to endorse it (most to least important)?"
  - Dịch: Điều bạn gõ vào khi chọn "Other (please specify)".
- **Kiểu:** văn bản tự do
- **Giá trị:** 2.009 dòng có nội dung (1.575 chuỗi khác nhau); các ví dụ phổ biến: `Good documentation`, `Documentation`, `Security`, `good documentation`
- **Lưu ý:** Lời dẫn trong schema trùng với nhóm xếp hạng phía trên (đây là ô điền chữ của mục "Other").

### 30–39. `TechOppose_1` … `TechOppose_15` — Điều khiến từ chối một công nghệ

- **Lời dẫn (schema):** "What would turn you off or cause you to reject it (most to least important)?"
  - Dịch: Điều gì khiến bạn quay lưng hoặc từ chối một công nghệ (từ quan trọng nhất đến ít quan trọng nhất)?
- **Kiểu:** xếp hạng · mỗi cột là một mục trong danh sách; giá trị là thứ hạng của mục đó. **16 giá trị** (số nguyên từ 1 đến 16, 1 = quan trọng nhất, lưu dạng float như `3.0`).
- **Số dòng có trả lời:** 34.259
- **Lưu ý:** Schema liệt kê 10 mục nhưng thứ hạng quan sát được lên tới 15–16, nên danh sách gốc dài hơn số cột trong file. Cột `TechOppose_15` ("Khác") cũng hầu hết bị để nguyên hạng 10. Tên cột không liên tục (1, 2, 3, 5, 7, ...) vì các mã mục bị lược bớt.

| # | Cột | Mục được xếp hạng (EN) | Tiếng Việt |
|---|---|---|---|
| 30 | `TechOppose_1` | Lack of AI or AI agents | Thiếu AI / AI agent |
| 31 | `TechOppose_2` | Poor usability | Khó sử dụng |
| 32 | `TechOppose_3` | Lack of or sub-par API | API thiếu hoặc kém |
| 33 | `TechOppose_5` | Inefficient or time-costly | Kém hiệu quả, tốn thời gian |
| 34 | `TechOppose_7` | Prohibitive pricing | Giá quá cao |
| 35 | `TechOppose_9` | Security or privacy concerns | Lo ngại bảo mật / riêng tư |
| 36 | `TechOppose_11` | Availability of better alternatives | Có lựa chọn thay thế tốt hơn |
| 37 | `TechOppose_13` | Outdated or obsolete technology or features | Công nghệ / tính năng lỗi thời |
| 38 | `TechOppose_16` | Ethical concerns | Lo ngại đạo đức |
| 39 | `TechOppose_15` | Other (please specify): | Lý do khác |

### 40. `TechOppose_15_TEXT` — Nội dung gõ tay cho mục "Khác" của TechOppose

- **Lời dẫn (schema):** "What would turn you off or cause you to reject it (most to least important)?"
  - Dịch: Điều bạn gõ vào khi chọn "Other (please specify)".
- **Kiểu:** văn bản tự do
- **Giá trị:** 1.647 dòng có nội dung (1.212 chuỗi khác nhau); các ví dụ phổ biến: `AI`, `Presence of AI or AI agents`, `Poor documentation`, `Use of AI`
- **Lưu ý:** Lời dẫn trong schema trùng với nhóm xếp hạng phía trên (đây là ô điền chữ của mục "Other").

---

## C. Ngành và mức hài lòng công việc (cột 41–59)

### 41. `Industry` — Ngành của công ty

- **Lời dẫn (schema):** "What industry do you work for in?"
  - Dịch: Bạn làm việc trong ngành nào?
- **Kiểu:** chọn **một** đáp án · **15 giá trị**
- **Các giá trị:** `Software Development`; `Other:`; `Internet, Telecomm or Information Services`; `Fintech`; `Banking/Financial Services`; `Healthcare`; `Manufacturing`; `Government`; `Higher Education`; `Retail and Consumer Services`; `Transportation, or Supply Chain`; `Computer Systems Design and Services`; `Media & Advertising Services`; `Energy`; `Insurance`
- **Lưu ý:** `Other:` là mục "Khác" (không ghi rõ).

### 42–56. `JobSatPoints_1` … `JobSatPoints_16` — Yếu tố làm hài lòng công việc

- **Lời dẫn (schema):** "Rank the following attributes of your current professional job in technology according to those that contribute your job satisfaction so that the first is the most important, last is least important (if you just started a new job, consider the job you spent the most time at in the past year):"
  - Dịch: Xếp hạng các yếu tố của công việc chuyên môn hiện tại theo mức đóng góp cho sự hài lòng với công việc: hạng nhất là quan trọng nhất, hạng cuối là ít quan trọng nhất (nếu mới đổi việc thì xét công việc làm lâu nhất năm qua).
- **Kiểu:** xếp hạng · mỗi cột là một mục trong danh sách; giá trị là thứ hạng của mục đó. **15 giá trị** (số nguyên từ 1 đến 15, 1 = quan trọng nhất, lưu dạng float như `3.0`).
- **Số dòng có trả lời:** 24.943
- **Lưu ý:** 15 mục, thứ hạng từ 1 đến 15, khớp với số mục trong schema. Với `JobSatPoints_15` ("Khác"), đa số để nguyên hạng 15. `JobSatPoints_11` hỏi mức quan trọng của lương, **không** phải mức lương thực.

| # | Cột | Mục được xếp hạng (EN) | Tiếng Việt |
|---|---|---|---|
| 42 | `JobSatPoints_1` | Control over the level of quality in projects | Kiểm soát chất lượng dự án |
| 43 | `JobSatPoints_2` | Autonomy and trust to manage your own tasks | Tự chủ và được tin tưởng quản lý công việc |
| 44 | `JobSatPoints_3` | Collaboration and support from a team | Hợp tác và hỗ trợ từ nhóm |
| 45 | `JobSatPoints_4` | Expert mentors | Có người cố vấn giỏi |
| 46 | `JobSatPoints_5` | Opportunities to mentor and lead junior-level coworkers | Cơ hội dìu dắt đồng nghiệp trẻ |
| 47 | `JobSatPoints_6` | Developing specialized expertise | Phát triển chuyên môn sâu |
| 48 | `JobSatPoints_7` | Solving real-world problems | Giải quyết vấn đề thực tế |
| 49 | `JobSatPoints_8` | Job stability and career growth with a single employer | Ổn định và thăng tiến ở một công ty |
| 50 | `JobSatPoints_9` | Innovation through solving challenging and complex problems | Đổi mới qua việc giải bài toán khó, phức tạp |
| 51 | `JobSatPoints_10` | Working with new technologies and tools | Làm việc với công nghệ / công cụ mới |
| 52 | `JobSatPoints_11` | Competitive pay and benefits | Lương và phúc lợi cạnh tranh |
| 53 | `JobSatPoints_13` | Recognition from peers for your work | Được đồng nghiệp công nhận |
| 54 | `JobSatPoints_14` | Recognition from leadership for your work | Được lãnh đạo công nhận |
| 55 | `JobSatPoints_15` | Other (please specify): | Lý do khác |
| 56 | `JobSatPoints_16` | You like your manager | Thích quản lý của mình |

### 57. `JobSatPoints_15_TEXT` — Nội dung gõ tay cho mục "Khác" của JobSatPoints

- **Lời dẫn (schema):** "Rank the following attributes of your current professional job in technology according to those that contribute your job satisfaction so that the first is the most important, last is least important (if you just started a new job, consider the job you spent the most time at in the past year):"
  - Dịch: Điều bạn gõ vào khi chọn "Other (please specify)".
- **Kiểu:** văn bản tự do
- **Giá trị:** 664 dòng có nội dung (571 chuỗi khác nhau); các ví dụ phổ biến: `Remote work`, `Remote`, `Remote working`, `work life balance`
- **Lưu ý:** Lời dẫn trong schema trùng với nhóm xếp hạng phía trên (đây là ô điền chữ của mục "Other").

### 58. `AIThreat` — AI có đe dọa công việc không

- **Lời dẫn (schema):** "Do you believe AI is a threat to your current job?"
  - Dịch: Bạn có tin AI là mối đe dọa đối với công việc hiện tại của mình không?
- **Kiểu:** chọn **một** đáp án · **3 giá trị**
- **Các giá trị:**
  1. `No` — Không
  2. `I'm not sure` — Không chắc
  3. `Yes` — Có

### 59. `NewRole` — Cân nhắc / chuyển đổi nghề trong năm qua

- **Lời dẫn (schema):** "Have you considered a career change or transitioned into a new role in the past year?"
  - Dịch: Trong năm qua bạn có cân nhắc đổi nghề hoặc chuyển sang vai trò mới không?
- **Kiểu:** chọn **một** đáp án · **5 giá trị**
- **Các giá trị:**
  1. `I have neither consider or transitioned into a new career or industry` — Chưa từng cân nhắc hay chuyển đổi
  2. `I have somewhat considered changing my career and/or the industry I work in` — Có cân nhắc đổi nghề / ngành ở mức nhẹ
  3. `I have strongly considered changing my career and/or the industry I work in` — Cân nhắc đổi nghề / ngành rất nghiêm túc
  4. `I have transitioned into a new career and/or industry voluntarily` — Đã chủ động chuyển nghề / ngành
  5. `I have transitioned into a new career and/or industry involuntarily` — Bị buộc phải chuyển nghề / ngành

---

## D. Số công cụ, vị trí, thu nhập (cột 60–64)

### 60. `ToolCountWork` — Số công cụ dùng cho công việc chính

- **Lời dẫn (schema):** "For your primary work role (student, developer, or technologist) over the past year: Excluding general operating systems (like Windows or macOS) and web browsers, how many distinct software applications or platforms did you regularly use to create, analyze, manage, or share information in order to do your job? Please enter a whole number below with no punctuation, or leave blank."
  - Dịch: Với vai trò công việc chính (sinh viên, dev hoặc kỹ thuật viên) trong năm qua: không tính hệ điều hành và trình duyệt, bạn thường xuyên dùng bao nhiêu phần mềm / nền tảng riêng biệt để tạo, phân tích, quản lý hoặc chia sẻ thông tin phục vụ công việc? Nhập số nguyên.
- **Kiểu:** số nguyên nhập tay (kiểu `TE`)
- **Giá trị:** số (thực tế lưu dạng float); 27.611 dòng có giá trị; 114 giá trị khác nhau; nhỏ nhất 0, lớn nhất 10000, trung vị 6

### 61. `ToolCountPersonal` — Số công cụ dùng cho dự án cá nhân

- **Lời dẫn (schema):** "For your side projects or other personal work over the past year (focus on the project you spent the most time on if applicable): Excluding general operating systems and web browsers, how many distinct software applications or platforms did you regularly use to do your job? Please enter a whole number below with no punctuation, or leave blank."
  - Dịch: Với dự án phụ / công việc cá nhân trong năm qua (chọn dự án bạn dành nhiều thời gian nhất): không tính hệ điều hành và trình duyệt, bạn thường xuyên dùng bao nhiêu phần mềm / nền tảng riêng biệt? Nhập số nguyên.
- **Kiểu:** số nguyên nhập tay (kiểu `TE`)
- **Giá trị:** số (thực tế lưu dạng float); 25.582 dòng có giá trị; 87 giá trị khác nhau; nhỏ nhất 0, lớn nhất 1000, trung vị 5
- **Lưu ý:** Lời dẫn trong schema ghi "to do your job" (làm công việc), dù đây là phần dự án cá nhân.

### 62. `Country` — Quốc gia đang sống

- **Lời dẫn (schema):** "Where do you live?"
  - Dịch: Bạn sống ở đâu?
- **Kiểu:** chọn **một** đáp án · **177 giá trị**
- **Các giá trị:** xem Phụ lục 1 (danh sách đầy đủ). Top 5: `United States of America`, `Germany`, `India`, `United Kingdom of Great Britain and Northern Ireland`, `France`.

### 63. `Currency` — Đơn vị tiền tệ dùng hằng ngày

- **Lời dẫn (schema):** "Which currency do you use day-to-day? If your answer is complicated, please pick the one you're most comfortable estimating in."
  - Dịch: Bạn dùng loại tiền nào hằng ngày? Nếu phức tạp, chọn loại bạn quen ước lượng nhất.
- **Kiểu:** chọn **một** đáp án · **142 giá trị**
- **Các giá trị:** dạng `<mã 3 chữ> <tên tiền>`, ví dụ `EUR European Euro`, `USD United States dollar`; xem Phụ lục 2. Top 5: `EUR European Euro`, `USD United States dollar`, `INR Indian rupee`, `GBP Pound sterling`, `CAD Canadian dollar`.
- **Lưu ý:** Giá trị `AUD	Australian dollar` dùng ký tự tab thay vì dấu cách; nên lấy 3 ký tự đầu (`str[:3]`) làm mã tiền.

### 64. `CompTotal` — Tổng thu nhập hằng năm

- **Lời dẫn (schema):** "What is your current total annual compensation (salary, bonuses, and perks, before taxes and deductions) in terms of your day-to-day currency? Please enter a whole number in the box below, without any punctuation. If you are paid hourly, please estimate an equivalent yearly salary. If you prefer not to answer, please leave the box empty."
  - Dịch: Tổng thu nhập **hằng năm** hiện tại (lương, thưởng, phúc lợi, trước thuế và các khoản trừ) tính bằng đơn vị tiền bạn dùng hằng ngày. Nhập số nguyên, không dấu câu. Nếu trả theo giờ thì ước tính ra cả năm. Không muốn trả lời thì để trống.
- **Kiểu:** số nhập tay (kiểu `TE`)
- **Giá trị:** số (thực tế lưu dạng float); 24.866 dòng có giá trị; 2.678 giá trị khác nhau; nhỏ nhất 0, lớn nhất khoảng 5,6×10^74 (số vô lý, chắc chắn nhập sai), trung vị 105.000
- **Lưu ý:** Tính theo đơn vị tiền ở cột `Currency` nên **chưa so sánh được giữa các nước**, cần quy đổi USD. Có 751 dòng bằng 0 và các giá trị cực lớn không thể là thu nhập thật (cần lọc outlier).

---

## E. Ngôn ngữ, cơ sở dữ liệu, nền tảng, web framework (cột 65–86)

Mỗi nhóm công nghệ gồm các cột cùng khuôn: `*Choice` (có dùng nhóm này không), `*HaveWorkedWith` (đã dùng), `*WantToWorkWith` (muốn dùng), `*Admired` (được ngưỡng mộ), `*HaveEntry` / `*WantEntry` (gõ tay mục không có trong danh sách). Ba cột `HaveWorkedWith`, `WantToWorkWith`, `Admired` của cùng nhóm **dùng chung một danh sách lựa chọn** (đã kiểm tra bằng dữ liệu).

**Quan hệ đã kiểm tra bằng dữ liệu:**
- `Admired` = giao của `HaveWorkedWith` và `WantToWorkWith`: đúng ở **100% dòng** cho cả 4 nhóm. Tức là mỗi mục "được ngưỡng mộ" là mục người đó đã dùng **và** muốn dùng tiếp. Cột `Admired` do đó **trùng lặp**, suy ra được từ hai cột kia.
- Nếu `*Choice` = `No` thì `*HaveWorkedWith` luôn trống (100%). Nhưng ô trống ở `HaveWorkedWith` còn đến từ người không được hỏi / bỏ qua phần này (`*Choice` cũng trống) và một số ít chọn `Yes` rồi không chọn mục nào. Vì vậy **NaN ở `HaveWorkedWith` không đồng nghĩa với "không dùng"**.

### Ngôn ngữ lập trình / script / markup (cột 65–70)

### 65. `LanguageChoice` — Có làm việc / dự định dùng ngôn ngữ không

- **Lời dẫn (schema):** "Did you work with programming, scripting and markup languages in the last year or do you plan to in the year to come? Here, we are referring to anything you use that is conventionally referred to as code."
- **Kiểu:** chọn **một** đáp án · **2 giá trị**
- **Các giá trị:**
  1. `Yes` — Có
  2. `No` — Không

### 66. `LanguageHaveWorkedWith` — Ngôn ngữ đã dùng

- **Lời dẫn (schema):** *(không có trong schema.csv)*
  - Diễn giải: Danh sách ngôn ngữ bạn đã dùng nhiều trong năm qua.
- **Kiểu:** chọn **nhiều**, nối bằng `;` · **42 lựa chọn**
- **Các lựa chọn:** `JavaScript`; `HTML/CSS`; `SQL`; `Python`; `Bash/Shell (all shells)`; `TypeScript`; `Java`; `C#`; `C++`; `PowerShell`; `C`; `PHP`; `Go`; `Rust`; `Kotlin`; `Lua`; `Assembly`; `Ruby`; `Dart`; `Swift`; `R`; `Groovy`; `Visual Basic (.Net)`; `VBA`; `MATLAB`; `Perl`; `GDScript`; `Elixir`; `Scala`; `Delphi`; `Lisp`; `MicroPython`; `Zig`; `Erlang`; `Fortran`; `Ada`; `F#`; `OCaml`; `Gleam`; `Prolog`; `COBOL`; `Mojo`
- **Lưu ý:** `LanguageChoice`=`Yes` nhưng không chọn mục nào: 522 dòng; `LanguageChoice` trống: 16.337 dòng NaN.

### 67. `LanguageWantToWorkWith` — Ngôn ngữ muốn dùng trong năm tới

- **Lời dẫn (schema):** *(không có trong schema.csv)*
  - Dịch: Danh sách ngôn ngữ bạn muốn dùng trong năm tới.
- **Kiểu:** chọn **nhiều**, nối bằng `;` · **42 lựa chọn** (cùng danh sách với `LanguageHaveWorkedWith`)
- Xem danh sách ở cột `HaveWorkedWith` của nhóm này.

### 68. `LanguageAdmired` — Ngôn ngữ được ngưỡng mộ

- **Lời dẫn (schema):** *(không có trong schema.csv)*
  - Dịch: Danh sách ngôn ngữ vừa đã dùng vừa muốn tiếp tục dùng.
- **Kiểu:** chọn **nhiều**, nối bằng `;` · **42 lựa chọn** (cùng danh sách)
- Xem danh sách ở cột `HaveWorkedWith`. Bằng đúng `HaveWorkedWith ∩ WantToWorkWith` ở 100% dòng.

### 69. `LanguagesHaveEntry` — Gõ tay: ngôn ngữ đã dùng nhưng không có trong danh sách

- **Lời dẫn (schema):** "Was the programming language you use not listed above? List below, separated by a comma and a space for each, the programming language(s) you used in the past year ."
- **Kiểu:** văn bản tự do (nhiều mục cách nhau bằng dấu phẩy)
- **Giá trị:** 3.982 dòng có nội dung (1.896 chuỗi khác nhau); phổ biến: `Haskell`, `Julia`, `Clojure`, `Objective-C`

### 70. `LanguagesWantEntry` — Gõ tay: ngôn ngữ muốn dùng nhưng không có trong danh sách

- **Lời dẫn (schema):** "Was the programming language you want to use not listed above? List below, separated by a comma and a space for each, the programming language(s) you want to use next year ."
- **Kiểu:** văn bản tự do (nhiều mục cách nhau bằng dấu phẩy)
- **Giá trị:** 3.150 dòng có nội dung (1.413 chuỗi khác nhau); phổ biến: `Haskell`, `Julia`, `Clojure`, `Nix`

### Cơ sở dữ liệu (cột 71–76)

### 71. `DatabaseChoice` — Có làm việc / dự định dùng cơ sở dữ liệu không

- **Lời dẫn (schema):** "Did you work with database environments in the last year or do you plan to in the year to come? Here, we are referring to a system of managing structured data, mostly outside of your local machine."
- **Kiểu:** chọn **một** đáp án · **2 giá trị**
- **Các giá trị:**
  1. `Yes` — Có
  2. `No` — Không

### 72. `DatabaseHaveWorkedWith` — Cơ sở dữ liệu đã dùng

- **Lời dẫn (schema):** *(không có trong schema.csv)*
  - Diễn giải: Danh sách cơ sở dữ liệu bạn đã dùng nhiều trong năm qua.
- **Kiểu:** chọn **nhiều**, nối bằng `;` · **30 lựa chọn**
- **Các lựa chọn:** `PostgreSQL`; `MySQL`; `SQLite`; `Microsoft SQL Server`; `Redis`; `MongoDB`; `MariaDB`; `Elasticsearch`; `Oracle`; `Dynamodb`; `BigQuery`; `Supabase`; `Cloud Firestore`; `H2`; `Firebase Realtime Database`; `Microsoft Access`; `Cosmos DB`; `Snowflake`; `InfluxDB`; `Databricks SQL`; `DuckDB`; `Cassandra`; `Neo4J`; `Valkey`; `Clickhouse`; `IBM DB2`; `Amazon Redshift`; `Cockroachdb`; `Pocketbase`; `Datomic`
- **Lưu ý:** `DatabaseChoice`=`Yes` nhưng không chọn mục nào: 1.145 dòng; `DatabaseChoice` trống: 17.073 dòng NaN.

### 73. `DatabaseWantToWorkWith` — Cơ sở dữ liệu muốn dùng trong năm tới

- **Lời dẫn (schema):** *(không có trong schema.csv)*
  - Dịch: Danh sách cơ sở dữ liệu bạn muốn dùng trong năm tới.
- **Kiểu:** chọn **nhiều**, nối bằng `;` · **30 lựa chọn** (cùng danh sách với `DatabaseHaveWorkedWith`)
- Xem danh sách ở cột `HaveWorkedWith` của nhóm này.

### 74. `DatabaseAdmired` — Cơ sở dữ liệu được ngưỡng mộ

- **Lời dẫn (schema):** *(không có trong schema.csv)*
  - Dịch: Danh sách cơ sở dữ liệu vừa đã dùng vừa muốn tiếp tục dùng.
- **Kiểu:** chọn **nhiều**, nối bằng `;` · **30 lựa chọn** (cùng danh sách)
- Xem danh sách ở cột `HaveWorkedWith`. Bằng đúng `HaveWorkedWith ∩ WantToWorkWith` ở 100% dòng.

### 75. `DatabaseHaveEntry` — Gõ tay: cơ sở dữ liệu đã dùng nhưng không có trong danh sách

- **Lời dẫn (schema):** "Was the database environment you use not listed above? List below, separated by a comma and a space for each, what you used in the past year ."
- **Kiểu:** văn bản tự do (nhiều mục cách nhau bằng dấu phẩy)
- **Giá trị:** 2.150 dòng có nội dung (1.128 chuỗi khác nhau); phổ biến: `Firebird`, `CouchDB`, `OpenSearch`, `Spanner`

### 76. `DatabaseWantEntry` — Gõ tay: cơ sở dữ liệu muốn dùng nhưng không có trong danh sách

- **Lời dẫn (schema):** "Was the database environment you want to use not listed above? List below, separated by a comma and a space for each, what you want to use next year ."
- **Kiểu:** văn bản tự do (nhiều mục cách nhau bằng dấu phẩy)
- **Giá trị:** 1.533 dòng có nội dung (837 chuỗi khác nhau); phổ biến: `SurrealDB`, `Firebird`, `CouchDB`, `SpacetimeDB`

### Nền tảng cloud, container, trình quản lý gói, công cụ build, hạ tầng (cột 77–82)

### 77. `PlatformChoice` — Có làm việc / dự định dùng nền tảng / công cụ không

- **Lời dẫn (schema):** "Did you work with cloud platforms, containerization/orchestration tools, package managers, build tools or infrastructure as code solutions in the last year or do you plan to in the year to come? Here, we are referring to tooling that automates, manages, and scales the entire application lifecycle, often leveraging remote, virtualized resources."
- **Kiểu:** chọn **một** đáp án · **2 giá trị**
- **Các giá trị:**
  1. `Yes` — Có
  2. `No` — Không

### 78. `PlatformHaveWorkedWith` — Nền tảng / công cụ đã dùng

- **Lời dẫn (schema):** *(không có trong schema.csv)*
  - Diễn giải: Danh sách nền tảng / công cụ bạn đã dùng nhiều trong năm qua.
- **Kiểu:** chọn **nhiều**, nối bằng `;` · **42 lựa chọn**
- **Các lựa chọn:** `Docker`; `npm`; `Amazon Web Services (AWS)`; `Pip`; `Kubernetes`; `Microsoft Azure`; `Homebrew`; `Vite`; `Google Cloud`; `Make`; `Yarn`; `Cloudflare`; `NuGet`; `APT`; `Webpack`; `Terraform`; `Maven (build tool)`; `Gradle`; `Cargo`; `pnpm`; `Firebase`; `Prometheus`; `Ansible`; `Podman`; `Chocolatey`; `Composer`; `MSBuild`; `Digital Ocean`; `Vercel`; `Poetry`; `Datadog`; `Pacman`; `Netlify`; `Bun`; `Supabase`; `Heroku`; `Ninja`; `Splunk`; `New Relic`; `Railway`; `IBM Cloud`; `Yandex Cloud`
- **Lưu ý:** `PlatformChoice`=`Yes` nhưng không chọn mục nào: 603 dòng; `PlatformChoice` trống: 17.240 dòng NaN.

### 79. `PlatformWantToWorkWith` — Nền tảng / công cụ muốn dùng trong năm tới

- **Lời dẫn (schema):** *(không có trong schema.csv)*
  - Dịch: Danh sách nền tảng / công cụ bạn muốn dùng trong năm tới.
- **Kiểu:** chọn **nhiều**, nối bằng `;` · **42 lựa chọn** (cùng danh sách với `PlatformHaveWorkedWith`)
- Xem danh sách ở cột `HaveWorkedWith` của nhóm này.

### 80. `PlatformAdmired` — Nền tảng / công cụ được ngưỡng mộ

- **Lời dẫn (schema):** *(không có trong schema.csv)*
  - Dịch: Danh sách nền tảng / công cụ vừa đã dùng vừa muốn tiếp tục dùng.
- **Kiểu:** chọn **nhiều**, nối bằng `;` · **42 lựa chọn** (cùng danh sách)
- Xem danh sách ở cột `HaveWorkedWith`. Bằng đúng `HaveWorkedWith ∩ WantToWorkWith` ở 100% dòng.

### 81. `PlatformHaveEntry` — Gõ tay: nền tảng / công cụ đã dùng nhưng không có trong danh sách

- **Lời dẫn (schema):** "Was the cloud platforms, containerization/orchestration tools, package managers, build tools, and infrastructure as code solutions you use not listed above? List below, separated by a comma and a space for each, what you used in the past year ."
- **Kiểu:** văn bản tự do (nhiều mục cách nhau bằng dấu phẩy)
- **Giá trị:** 3.957 dòng có nội dung (1.838 chuỗi khác nhau); phổ biến: `uv`, `Nix`, `CMake`, `nix`

### 82. `PlatformWantEntry` — Gõ tay: nền tảng / công cụ muốn dùng nhưng không có trong danh sách

- **Lời dẫn (schema):** "Was the cloud platforms, containerization/orchestration tools, package managers, build tools, and infrastructure as code solutions you want to use not listed above? List below, separated by a comma and a space for each, what you want to use next year ."
- **Kiểu:** văn bản tự do (nhiều mục cách nhau bằng dấu phẩy)
- **Giá trị:** 3.100 dòng có nội dung (1.391 chuỗi khác nhau); phổ biến: `uv`, `Nix`, `nix`, `CMake`

### Web framework (cột 83–86)

### 83. `WebframeChoice` — Có làm việc / dự định dùng web framework không

- **Lời dẫn (schema):** "Did you work with web frameworks and web technologies in the last year or do you plan to in the year to come? Here, we are referring to technology that helps website and web apps materialize."
- **Kiểu:** chọn **một** đáp án · **2 giá trị**
- **Các giá trị:**
  1. `Yes` — Có
  2. `No` — Không

### 84. `WebframeHaveWorkedWith` — Web framework đã dùng

- **Lời dẫn (schema):** *(không có trong schema.csv)*
  - Diễn giải: Danh sách web framework / công nghệ web bạn đã dùng trong năm qua.
- **Kiểu:** chọn **nhiều**, nối bằng `;` · **28 lựa chọn**
- **Các lựa chọn:** `Node.js`; `React`; `jQuery`; `Next.js`; `Express`; `ASP.NET Core`; `Angular`; `Vue.js`; `FastAPI`; `Spring Boot`; `Flask`; `ASP.NET`; `WordPress`; `Django`; `Laravel`; `AngularJS`; `Svelte`; `Blazor`; `NestJS`; `Ruby on Rails`; `Astro`; `Deno`; `Symfony`; `Nuxt.js`; `Fastify`; `Axum`; `Phoenix`; `Drupal`

### 85. `WebframeWantToWorkWith` — Web framework muốn dùng trong năm tới

- **Lời dẫn (schema):** *(không có trong schema.csv)*
  - Dịch: Danh sách web framework bạn muốn dùng trong năm tới.
- **Kiểu:** chọn **nhiều**, nối bằng `;` · **28 lựa chọn** (cùng danh sách)
- Xem danh sách ở cột `WebframeHaveWorkedWith`.

### 86. `WebframeAdmired` — Web framework được ngưỡng mộ

- **Lời dẫn (schema):** *(không có trong schema.csv)*
  - Dịch: Danh sách web framework vừa đã dùng vừa muốn tiếp tục dùng.
- **Kiểu:** chọn **nhiều**, nối bằng `;` · **28 lựa chọn** (cùng danh sách)
- Xem danh sách ở cột `WebframeHaveWorkedWith`. Bằng đúng `HaveWorkedWith ∩ WantToWorkWith` ở 100% dòng.

---

## Phụ lục 1. Danh sách 177 giá trị của `Country`

Afghanistan; Albania; Algeria; Andorra; Angola; Antigua and Barbuda; Argentina; Armenia; Australia; Austria; Azerbaijan; Bahrain; Bangladesh; Barbados; Belarus; Belgium; Belize; Benin; Bhutan; Bolivia; Bosnia and Herzegovina; Botswana; Brazil; Brunei Darussalam; Bulgaria; Burundi; Cambodia; Cameroon; Canada; Cape Verde; Chile; China; Colombia; Congo, Republic of the...; Costa Rica; Croatia; Cuba; Cyprus; Czech Republic; Côte d'Ivoire; Democratic People's Republic of Korea; Democratic Republic of the Congo; Denmark; Djibouti; Dominican Republic; Ecuador; Egypt; El Salvador; Estonia; Ethiopia; Fiji; Finland; France; Gabon; Gambia; Georgia; Germany; Ghana; Greece; Guatemala; Guinea; Guinea-Bissau; Guyana; Haiti; Honduras; Hong Kong (S.A.R.); Hungary; Iceland; India; Indonesia; Iran, Islamic Republic of...; Iraq; Ireland; Isle of Man; Israel; Italy; Jamaica; Japan; Jordan; Kazakhstan; Kenya; Kosovo; Kuwait; Kyrgyzstan; Lao People's Democratic Republic; Latvia; Lebanon; Lesotho; Libyan Arab Jamahiriya; Lithuania; Luxembourg; Madagascar; Malawi; Malaysia; Maldives; Mali; Malta; Mauritania; Mauritius; Mexico; Micronesia, Federated States of...; Moldova; Mongolia; Montenegro; Morocco; Mozambique; Myanmar; Namibia; Nepal; Netherlands; New Zealand; Nicaragua; Niger; Nigeria; Nomadic; North Korea; Norway; Oman; Pakistan; Palau; Palestine; Panama; Papua New Guinea; Paraguay; Peru; Philippines; Poland; Portugal; Qatar; Republic of Korea; Republic of Moldova; Republic of North Macedonia; Romania; Russian Federation; Rwanda; Saint Lucia; San Marino; Saudi Arabia; Senegal; Serbia; Sierra Leone; Singapore; Slovakia; Slovenia; Somalia; South Africa; South Korea; Spain; Sri Lanka; Sudan; Suriname; Swaziland; Sweden; Switzerland; Syrian Arab Republic; Taiwan; Tajikistan; Thailand; Timor-Leste; Togo; Trinidad and Tobago; Tunisia; Turkey; Turkmenistan; Uganda; Ukraine; United Arab Emirates; United Kingdom of Great Britain and Northern Ireland; United Republic of Tanzania; United States of America; Uruguay; Uzbekistan; Venezuela, Bolivarian Republic of...; Viet Nam; Yemen; Zambia; Zimbabwe

## Phụ lục 2. Danh sách 142 giá trị của `Currency`

AED United Arab Emirates dirham; AFN Afghan afghani; ALL Albanian lek; AMD Armenian dram; ANG Netherlands Antillean guilder; AOA Angolan kwanza; ARS Argentine peso; AUD Australian dollar; AZN Azerbaijan manat; BAM Bosnia and Herzegovina convertible mark; BBD Barbadian dollar; BDT Bangladeshi taka; BGN Bulgarian lev; BHD Bahraini dinar; BIF Burundi franc; BND Brunei dollar; BOB Bolivian boliviano; BRL Brazilian real; BSD Bahamian dollar; BTN Bhutanese ngultrum; BWP Botswana pula; BYN Belarusian ruble; BZD Belize dollar; CAD Canadian dollar; CDF Congolese franc; CHF Swiss franc; CLP Chilean peso; CNY Chinese Yuan Renminbi; COP Colombian peso; CRC Costa Rican colon; CUP Cuban peso; CVE Cape Verdean escudo; CZK Czech koruna; DJF Djiboutian franc; DKK Danish krone; DOP Dominican peso; DZD Algerian dinar; EGP Egyptian pound; ETB Ethiopian birr; EUR European Euro; FJD Fijian dollar; GBP Pound sterling; GEL Georgian lari; GHS Ghanaian cedi; GIP Gibraltar pound; GMD Gambian dalasi; GNF Guinean franc; GTQ Guatemalan quetzal; GYD Guyanese dollar; HKD Hong Kong dollar; HNL Honduran lempira; HRK Croatian kuna; HTG Haitian gourde; HUF Hungarian forint; IDR Indonesian rupiah; ILS Israeli new shekel; IMP Manx pound; INR Indian rupee; IQD Iraqi dinar; IRR Iranian rial; ISK Icelandic krona; JMD Jamaican dollar; JOD Jordanian dinar; JPY Japanese yen; KES Kenyan shilling; KGS Kyrgyzstani som; KHR Cambodian riel; KPW North Korean won; KRW South Korean won; KWD Kuwaiti dinar; KYD Cayman Islands dollar; KZT Kazakhstani tenge; LAK Lao kip; LBP Lebanese pound; LKR Sri Lankan rupee; LSL Lesotho loti; LYD Libyan dinar; MAD Moroccan dirham; MDL Moldovan leu; MGA Malagasy ariary; MKD Macedonian denar; MMK Myanmar kyat; MNT Mongolian tugrik; MOP Macanese pataca; MRU Mauritanian ouguiya; MUR Mauritian rupee; MVR Maldivian rufiyaa; MWK Malawian kwacha; MXN Mexican peso; MYR Malaysian ringgit; MZN Mozambican metical; NAD Namibian dollar; NGN Nigerian naira; NIO Nicaraguan cordoba; NOK Norwegian krone; NPR Nepalese rupee; NZD New Zealand dollar; OMR Omani rial; PEN Peruvian sol; PGK Papua New Guinean kina; PHP Philippine peso; PKR Pakistani rupee; PLN Polish zloty; PYG Paraguayan guarani; QAR Qatari riyal; RON Romanian leu; RSD Serbian dinar; RUB Russian ruble; RWF Rwandan franc; SAR Saudi Arabian riyal; SDG Sudanese pound; SEK Swedish krona; SGD Singapore dollar; SLL Sierra Leonean leone; SRD Surinamese dollar; SYP Syrian pound; SZL Swazi lilangeni; THB Thai baht; TJS Tajikistani somoni; TMT Turkmen manat; TND Tunisian dinar; TRY Turkish lira; TTD Trinidad and Tobago dollar; TWD New Taiwan dollar; TZS Tanzanian shilling; UAH Ukrainian hryvnia; UGX Ugandan shilling; USD United States dollar; UYU Uruguayan peso; UZS Uzbekistani som; VES Venezuelan bolivar; VND Vietnamese dong; WST Samoan tala; XAF Central African CFA franc; XCD East Caribbean dollar; XOF West African CFA franc; XPF CFP franc; YER Yemeni rial; ZAR South African rand; ZMW Zambian kwacha; none Cook Islands dollar; none Faroese krona