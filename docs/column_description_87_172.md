# Ý nghĩa các cột 87–172

Nguồn: `schema.csv` (lời dẫn câu hỏi) và bảng dữ liệu khảo sát (172 cột; số thứ tự `#` dưới đây là vị trí cột từ 87 đến 172, nối tiếp phần 2–86).

**Cách đọc:** *chọn một* = mỗi dòng có đúng 1 giá trị; *chọn nhiều* = ô chứa nhiều lựa chọn nối bằng `;`; *văn bản tự do* = người trả lời tự gõ. Ô trống (`NaN` / `NA`) nghĩa là không trả lời hoặc không được hỏi câu đó (ví dụ chọn `No` ở câu `*Choice` hoặc không dùng AI agents).

---

## A. Phần tiếp nối Web Framework, IDE / AI Editors & Tag Stack Overflow (cột 87–99)

### 87. `WebframeHaveEntry` — Gõ tay: web framework đã dùng nhưng không có trong danh sách

- **Lời dẫn (schema):** "Were the web frameworks and web technologies you use not listed above? List below, separated by a comma and a space for each, what you used in the past year."
  - Dịch: Những web framework và công nghệ web bạn sử dụng chưa có trong danh sách trên là gì? Liệt kê những gì bạn đã dùng trong năm qua.
- **Kiểu:** văn bản tự do

### 88. `WebframeWantEntry` — Gõ tay: web framework muốn dùng nhưng không có trong danh sách

- **Lời dẫn (schema):** "Were the web frameworks and web technologies you want to use not listed above? List below, separated by a comma and a space for each, what you want to use next year."
  - Dịch: Những web framework và công nghệ web bạn muốn dùng chưa có trong danh sách trên là gì? Liệt kê những gì bạn muốn dùng trong năm tới.
- **Kiểu:** văn bản tự do

### 89. `DevEnvsChoice` — Có dùng môi trường phát triển / công cụ chỉnh sửa mã AI không

- **Lời dẫn (schema):** "Did you work with development environments or AI-enabled code editing tools in the last year or do you plan to in the year to come? Here, we are referring to programs like VS Code that allow you to write, edit and save code easily and help you share code with other developers or AI agents."
  - Dịch: Bạn có làm việc với các môi trường phát triển hoặc công cụ chỉnh sửa mã hỗ trợ AI trong năm qua hoặc có kế hoạch trong năm tới không?
- **Kiểu:** chọn **một** đáp án · **2 giá trị** (`Yes`, `No`)
- **Lưu ý:** Câu hỏi rẽ nhánh cho nhóm `DevEnvs`.

### 90. `DevEnvsHaveWorkedWith` — Môi trường phát triển / công cụ chỉnh sửa mã AI đã dùng

- **Lời dẫn (schema):** *(không có trong schema.csv)*
  - Dịch: Danh sách IDE và công cụ chỉnh sửa mã hỗ trợ AI bạn đã dùng thường xuyên trong năm qua.
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 91. `DevEnvsWantToWorkWith` — Môi trường phát triển / công cụ chỉnh sửa mã AI muốn dùng

- **Lời dẫn (schema):** *(không có trong schema.csv)*
  - Dịch: Danh sách IDE và công cụ chỉnh sửa mã hỗ trợ AI bạn muốn dùng trong năm tới.
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 92. `DevEnvsAdmired` — Môi trường phát triển / công cụ chỉnh sửa mã AI được ngưỡng mộ

- **Lời dẫn (schema):** *(không có trong schema.csv)*
  - Dịch: Danh sách IDE và công cụ chỉnh sửa mã AI vừa đã dùng vừa muốn tiếp tục dùng.
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 93. `DevEnvHaveEntry` — Gõ tay: IDE / công cụ chỉnh sửa mã AI đã dùng

- **Lời dẫn (schema):** "Was the developer environment or AI-enabled code editing tool you use not listed above? List below, separated by a comma and a space for each, what you used in the past year."
  - Dịch: Môi trường phát triển hoặc công cụ chỉnh sửa mã AI bạn đã dùng nhưng chưa có trong danh sách là gì?
- **Kiểu:** văn bản tự do

### 94. `DevEnvWantEntry` — Gõ tay: IDE / công cụ chỉnh sửa mã AI muốn dùng

- **Lời dẫn (schema):** "Was the developer environment or AI-enabled code editing tool you use not listed above? List below, separated by a comma and a space for each, what you want to use next year."
  - Dịch: Môi trường phát triển hoặc công cụ chỉnh sửa mã AI bạn muốn dùng nhưng chưa có trong danh sách là gì?
- **Kiểu:** văn bản tự do

### 95. `SOTagsHaveWorkedWith` — Tag công nghệ mới nổi trên Stack Overflow đã dùng

- **Lời dẫn (schema):** *(không có trong schema.csv)*
  - Dịch: Danh sách tag / chủ đề công nghệ mới nổi trên Stack Overflow bạn đã dùng thường xuyên trong năm qua.
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 96. `SOTagsWantToWorkWith` — Tag công nghệ mới nổi trên Stack Overflow muốn dùng

- **Lời dẫn (schema):** *(không có trong schema.csv)*
  - Dịch: Danh sách tag / chủ đề công nghệ mới nổi trên Stack Overflow bạn muốn dùng trong năm tới.
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 97. `SOTagsAdmired` — Tag công nghệ mới nổi trên Stack Overflow được ngưỡng mộ

- **Lời dẫn (schema):** *(không có trong schema.csv)*
  - Dịch: Danh sách tag / chủ đề công nghệ mới nổi trên Stack Overflow vừa đã dùng vừa muốn tiếp tục dùng.
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 98. `SOTagsHaveEntry` — Gõ tay: tag mới trên Stack Overflow đã dùng

- **Lời dẫn (schema):** "Was the new tag on Stack Overflow (i.e. added in the last 2 - 3 years) you use not listed above? List below, separated by a comma and a space for each, what you used in the past year."
  - Dịch: Tag mới trên Stack Overflow bạn đã dùng nhưng chưa có trong danh sách là gì?
- **Kiểu:** văn bản tự do

### 99. `SOTagsWant Entry` — Gõ tay: tag mới trên Stack Overflow muốn dùng

- **Lời dẫn (schema):** "Was the new tag on Stack Overflow (i.e. added in the last 2 - 3 years) you want to use not listed above? List below, separated by a comma and a space for each, what you want to use next year."
  - Dịch: Tag mới trên Stack Overflow bạn muốn dùng trong năm tới nhưng chưa có trong danh sách là gì?
- **Kiểu:** văn bản tự do
- **Lưu ý:** Tên cột có dấu cách trước `Entry`.

---

## B. Hệ điều hành, công cụ cộng tác, cộng đồng & mô hình LLM (cột 100–117)

### 100. `OpSysPersonal use` — Hệ điều hành sử dụng cá nhân

- **Lời dẫn (schema):** *(tách từ câu hỏi `OpSys`)*
  - Dịch: Hệ điều hành bạn sử dụng cho mục đích cá nhân.
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 101. `OpSysProfessional use` — Hệ điều hành sử dụng cho công việc

- **Lời dẫn (schema):** *(tách từ câu hỏi `OpSys`)*
  - Dịch: Hệ điều hành bạn sử dụng cho công việc chuyên môn.
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 102. `OfficeStackAsyncHaveWorkedWith` — Công cụ quản lý công việc cộng tác / tài liệu mã nguồn đã dùng

- **Lời dẫn (schema):** *(không có trong schema.csv)*
  - Dịch: Danh sách công cụ quản lý công việc cộng tác và/hoặc tài liệu mã nguồn bạn đã dùng thường xuyên trong năm qua.
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 103. `OfficeStackAsyncWantToWorkWith` — Công cụ quản lý công việc cộng tác / tài liệu mã nguồn muốn dùng

- **Lời dẫn (schema):** *(không có trong schema.csv)*
  - Dịch: Danh sách công cụ quản lý công việc cộng tác và/hoặc tài liệu mã nguồn bạn muốn dùng trong năm tới.
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 104. `OfficeStackAsyncAdmired` — Công cụ quản lý công việc cộng tác / tài liệu mã nguồn được ngưỡng mộ

- **Lời dẫn (schema):** *(không có trong schema.csv)*
  - Dịch: Danh sách công cụ quản lý công việc cộng tác và/hoặc tài liệu mã nguồn vừa đã dùng vừa muốn tiếp tục dùng.
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 105. `OfficeStackHaveEntry` — Gõ tay: công cụ quản lý công việc / tài liệu đã dùng

- **Lời dẫn (schema):** "Was the collaborative work management and/or code documentation tools you use not listed above? List below, separated by a comma and a space for each, what you used in the past year."
  - Dịch: Công cụ quản lý công việc cộng tác / tài liệu mã nguồn đã dùng trong năm qua nhưng chưa có trong danh sách.
- **Kiểu:** văn bản tự do

### 106. `OfficeStackWantEntry` — Gõ tay: công cụ quản lý công việc / tài liệu muốn dùng

- **Lời dẫn (schema):** "Was the collaborative work management and/or code documentation tools you want to use not listed above? List below, separated by a comma and a space for each, what you used in the past year."
  - Dịch: Công cụ quản lý công việc cộng tác / tài liệu mã nguồn muốn dùng nhưng chưa có trong danh sách.
- **Kiểu:** văn bản tự do

### 107. `CommPlatformHaveWorkedWith` — Nền tảng cộng đồng đã dùng

- **Lời dẫn (schema):** *(không có trong schema.csv)*
  - Dịch: Danh sách nền tảng cộng đồng bạn đã sử dụng đáng kể hoặc đều đặn trong năm qua.
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 108. `CommPlatformWantToWorkWith` — Nền tảng cộng đồng muốn dùng

- **Lời dẫn (schema):** *(không có trong schema.csv)*
  - Dịch: Danh sách nền tảng cộng đồng bạn muốn sử dụng trong năm tới.
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 109. `CommPlatformAdmired` — Nền tảng cộng đồng được ngưỡng mộ

- **Lời dẫn (schema):** *(không có trong schema.csv)*
  - Dịch: Danh sách nền tảng cộng đồng vừa đã dùng vừa muốn tiếp tục dùng.
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 110. `CommPlatformHaveEntr` — Gõ tay: nền tảng cộng đồng đã dùng

- **Lời dẫn (schema):** "Was the community platform you use not listed above? List below, separated by a comma and a space for each, what you used in the past year."
  - Dịch: Nền tảng cộng đồng đã dùng trong năm qua nhưng chưa có trong danh sách.
- **Kiểu:** văn bản tự do
- **Lưu ý:** Tên cột bị cắt chữ `y` (`HaveEntr`).

### 111. `CommPlatformWantEntr` — Gõ tay: nền tảng cộng đồng muốn dùng

- **Lời dẫn (schema):** "Was the community platform you want to use not listed above? List below, separated by a comma and a space for each, what you used in the past year."
  - Dịch: Nền tảng cộng đồng muốn dùng nhưng chưa có trong danh sách.
- **Kiểu:** văn bản tự do
- **Lưu ý:** Tên cột bị cắt chữ `y` (`WantEntr`).

### 112. `AIModelsChoice` — Có sử dụng / tích hợp mô hình LLM không

- **Lời dẫn (schema):** "Did you utilize or integrate specific Large Language Models (LLMs) to power your development tools or applications in the last year? Here, we are referring to models like GPT-4, Llama, Claude, etc., within your development environments or solutions."
  - Dịch: Trong năm qua bạn có sử dụng hoặc tích hợp các mô hình ngôn ngữ lớn (LLM) để vận hành công cụ phát triển hoặc ứng dụng của mình không?
- **Kiểu:** chọn **một** đáp án · **2 giá trị** (`Yes`, `No`)

### 113. `AIModelsHaveWorkedWith` — Mô hình LLM đã dùng

- **Lời dẫn (schema):** *(không có trong schema.csv)*
  - Dịch: Danh sách mô hình LLM bạn đã dùng cho công việc phát triển trong năm qua.
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 114. `AIModelsWantToWorkWith` — Mô hình LLM muốn dùng

- **Lời dẫn (schema):** *(không có trong schema.csv)*
  - Dịch: Danh sách mô hình LLM bạn muốn dùng trong năm tới.
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 115. `AIModelsAdmired` — Mô hình LLM được ngưỡng mộ

- **Lời dẫn (schema):** *(không có trong schema.csv)*
  - Dịch: Danh sách mô hình LLM vừa đã dùng vừa muốn tiếp tục dùng.
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 116. `AIModelsHaveEntry` — Gõ tay: mô hình LLM đã dùng

- **Lời dẫn (schema):** "Was the LLM model for AI tools you use not listed above? List below, separated by a comma and a space for each, what you used in the past year."
  - Dịch: Mô hình LLM đã dùng trong năm qua nhưng chưa có trong danh sách.
- **Kiểu:** văn bản tự do

### 117. `AIModelsWantEntry` — Gõ tay: mô hình LLM muốn dùng

- **Lời dẫn (schema):** "Was the LLM model for AI tools you want to use not listed above? List below, separated by a comma and a space for each, what you want to use next year."
  - Dịch: Mô hình LLM muốn dùng trong năm tới nhưng chưa có trong danh sách.
- **Kiểu:** văn bản tự do

---

## C. Tương tác Stack Overflow, Thái độ & Cách dùng AI (cột 118–146)

### 118. `SOAccount` — Có tài khoản Stack Overflow không

- **Lời dẫn (schema):** "Do you have a Stack Overflow account?"
  - Dịch: Bạn có tài khoản Stack Overflow không?
- **Kiểu:** chọn **một** đáp án

### 119. `SOVisitFreq` — Tần suất truy cập Stack Overflow

- **Lời dẫn (schema):** "How frequently would you say you visit Stack Overflow?"
  - Dịch: Bạn truy cập Stack Overflow với tần suất như thế nào?
- **Kiểu:** chọn **một** đáp án

### 120. `SODuration` — Thời gian đã sử dụng Stack Overflow

- **Lời dẫn (schema):** "How long have you used Stack Overflow?"
  - Dịch: Bạn đã sử dụng Stack Overflow được bao lâu rồi?
- **Kiểu:** chọn **một** đáp án

### 121. `SOPartFreq` — Tần suất tham gia Q&A trên Stack Overflow

- **Lời dẫn (schema):** "How frequently would you say you participate in Q&A on Stack Overflow? By participate we mean ask, answer, and vote or comment on questions."
  - Dịch: Bạn tham gia hỏi-đáp, bình chọn hoặc bình luận trên Stack Overflow thường xuyên thế nào?
- **Kiểu:** chọn **một** đáp án

### 122. `SO_Dev_Content` — Định dạng nội dung thay thế Q&A ưa thích

- **Lời dẫn (schema):** "Whether it be to solve a problem, for career growth or connecting with a community of developers, is there an alternative to the Q&A format you prefer using today or would like to see on Stack Overflow to get what you need? Select all that apply."
  - Dịch: Có định dạng thay thế nào cho hình thức hỏi-đáp mà bạn thích dùng hiện nay hoặc muốn thấy trên Stack Overflow không?
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 123–132. `SO_Actions_1`, `SO_Actions_16`, `SO_Actions_3`, `SO_Actions_4`, `SO_Actions_5`, `SO_Actions_6`, `SO_Actions_9`, `SO_Actions_7`, `SO_Actions_10`, `SO_Actions_15` — Các mục xếp hạng / hành động trên Stack Overflow

- **Lời dẫn (schema):** Nhóm câu hỏi xếp hạng / hành động tương tác liên quan tới Stack Overflow.
- **Kiểu:** xếp hạng / số thứ tự

### 133. `SO_Actions_15_TEXT` — Gõ tay cho mục `SO_Actions_15`

- **Lời dẫn (schema):** Ô nhập văn bản tương ứng với `SO_Actions_15`.
- **Kiểu:** văn bản tự do

### 134. `SOComm` — Cảm nhận có thuộc cộng đồng Stack Overflow không

- **Lời dẫn (schema):** "Do you consider yourself a member of the Stack Overflow community?"
  - Dịch: Bạn có tự coi mình là thành viên cộng đồng Stack Overflow không?
- **Kiểu:** chọn **một** đáp án

### 135. `SOFriction` — Tần suất vào Stack Overflow do lỗi từ công cụ AI

- **Lời dẫn (schema):** "When you visit Stack Overflow, how often is it a result of encountering issues from AI or AI-enabled tools that require extra time or effort to fix, understand, or debug?"
  - Dịch: Mức độ thường xuyên vào Stack Overflow do gặp sự cố từ AI hoặc công cụ hỗ trợ AI cần thêm thời gian/công sức sửa hoặc gỡ lỗi.
- **Kiểu:** chọn **một** đáp án

### 136. `AISelect` — Có đang sử dụng công cụ AI trong quy trình phát triển không

- **Lời dẫn (schema):** "Do you currently use AI tools in your development process?"
  - Dịch: Hiện tại bạn có sử dụng công cụ AI trong quy trình phát triển phần mềm của mình không?
- **Kiểu:** chọn **một** đáp án

### 137. `AISent` — Thái độ / mức độ ủng hộ dùng công cụ AI

- **Lời dẫn (schema):** "How favorable is your stance on using AI tools as part of your development workflow?"
  - Dịch: Quan điểm ủng hộ dùng công cụ AI trong quy trình phát triển của bạn ở mức độ nào?
- **Kiểu:** chọn **một** đáp án

### 138. `AIAcc` — Mức độ tin tưởng độ chính xác của đầu ra từ công cụ AI

- **Lời dẫn (schema):** "How much do you trust the accuracy of the output from AI tools as part of your development workflow?"
  - Dịch: Bạn tin tưởng độ chính xác của kết quả từ công cụ AI đến mức nào?
- **Kiểu:** chọn **một** đáp án

### 139. `AIComplex` — Đánh giá khả năng xử lý tác vụ phức tạp của công cụ AI

- **Lời dẫn (schema):** "How well do the AI tools you use in your development workflow handle complex tasks?"
  - Dịch: Các công cụ AI bạn dùng xử lý tác vụ phức tạp tốt đến mức nào?
- **Kiểu:** chọn **một** đáp án

### 140. `AIToolCurrently partially AI` — Công việc đang dùng AI một phần

- **Lời dẫn (schema):** *(tách từ câu hỏi `AITool`)*
  - Dịch: Những phần trong quy trình phát triển đang tích hợp / dùng AI một phần hiện nay.
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 141. `AIToolDon't plan to use AI for this task` — Công việc không dự định dùng AI

- **Lời dẫn (schema):** *(tách từ câu hỏi `AITool`)*
  - Dịch: Những phần trong quy trình phát triển không dự định dùng AI cho tác vụ đó.
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 142. `AIToolPlan to partially use AI` — Công việc dự định dùng AI một phần trong 3–5 năm tới

- **Lời dẫn (schema):** *(tách từ câu hỏi `AITool`)*
  - Dịch: Những phần dự định dùng AI một phần trong 3–5 năm tới.
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 143. `AIToolPlan to mostly use AI` — Công việc dự định dùng AI chủ yếu trong 3–5 năm tới

- **Lời dẫn (schema):** *(tách từ câu hỏi `AITool`)*
  - Dịch: Những phần dự định dùng AI chủ yếu trong 3–5 năm tới.
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 144. `AIToolCurrently mostly AI` — Công việc đang dùng AI chủ yếu

- **Lời dẫn (schema):** *(tách từ câu hỏi `AITool`)*
  - Dịch: Những phần trong quy trình phát triển đang dùng AI chủ yếu hiện nay.
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 145. `AIFrustration` — Các vấn đề / sự khó chịu gặp phải khi dùng AI

- **Lời dẫn (schema):** "When using AI tools, which of the following problems or frustrations have you encountered? Select all that apply."
  - Dịch: Khi dùng công cụ AI, bạn gặp những vấn đề hoặc sự khó chịu nào sau đây?
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 146. `AIExplain` — Câu hỏi mở: "vibe coding" có nằm trong công việc chuyên môn không

- **Lời dẫn (schema):** "In your own words, is 'vibe coding' part of your professional development work? For this question, we define vibe coding according to the Wikipedia definition, the process of generating software from LLM prompts."
  - Dịch: Bằng lời văn của riêng bạn, "vibe coding" có phải một phần trong công việc phát triển chuyên nghiệp của bạn không?
- **Kiểu:** văn bản tự do

---

## D. AI Agents, Triển vọng tương lai & 2 cột cuối (cột 147–172)

### 147. `AIAgents` — Có sử dụng AI agents trong công việc không

- **Lời dẫn (schema):** "Are you using AI agents in your work (development or otherwise)? AI agents refer to autonomous software entities that can operate with minimal to no direct human intervention using artificial intelligence techniques."
  - Dịch: Bạn có đang sử dụng AI agents trong công việc không?
- **Kiểu:** chọn **một** đáp án

### 148. `AIAgentChange` — Công cụ AI / AI agents làm thay đổi cách làm việc thế nào

- **Lời dẫn (schema):** "Have AI tools or AI agents changed how you complete development work in the past year?"
  - Dịch: Công cụ AI hoặc AI agents đã thay đổi cách hoàn thành công việc phát triển trong năm qua như thế nào?
- **Kiểu:** chọn **một** đáp án

### 149. `AIAgent_Uses` — Mục đích / tác vụ cụ thể dùng AI agents

- **Lời dẫn (schema):** "What industry purposes or specific tasks are you using AI agents in your development work? Select all that apply from both lists."
  - Dịch: Mục đích ngành nghề hoặc tác vụ cụ thể đang dùng AI agents trong công việc phát triển.
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 150. `AgentUsesGeneral` — Mục đích sử dụng AI agents tổng quát

- **Lời dẫn (schema):** *(đi liền sau `AIAgent_Uses`)*
  - Dịch: Nhóm mục đích sử dụng AI agents tổng quát.
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 151–155. `AIAgentImpactSomewhat agree`, `AIAgentImpactNeutral`, `AIAgentImpactSomewhat disagree`, `AIAgentImpactStrongly agree`, `AIAgentImpactStrongly disagree` — Tác động của AI agents theo mức độ đồng ý

- **Lời dẫn (schema):** "To what extent do you agree with the following statements regarding the impact of AI agents on your work as a developer?"
  - Dịch: Các cột phân theo từng mức độ đồng ý về tác động của AI agents đối với công việc lập trình viên.
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 156–160. `AIAgentChallengesNeutral`, `AIAgentChallengesSomewhat disagree`, `AIAgentChallengesStrongly agree`, `AIAgentChallengesSomewhat agree`, `AIAgentChallengesStrongly disagree` — Thách thức của AI agents theo mức độ đồng ý

- **Lời dẫn (schema):** "To what extent do you agree with the following statements regarding AI agents?"
  - Dịch: Các cột phân theo từng mức độ đồng ý về thách thức khi dùng AI agents.
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 161. `AIAgentKnowledge` — Công cụ quản lý bộ nhớ / dữ liệu cho AI agents

- **Lời dẫn (schema):** "You indicated you use or develop AI agents as part of your development work. Have you used any of the following tools for AI agent memory or data management in the past year?"
  - Dịch: Công cụ quản lý bộ nhớ hoặc dữ liệu cho AI agents đã dùng trong năm qua.
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 162. `AIAgentKnowWrite` — Gõ tay: công cụ bộ nhớ / điều phối AI agents

- **Lời dẫn (schema):** "Was the tool or tools for AI agent orchestration or agent frameworks you used in the past year not listed above? Please write them below separated by a comma and space if there are more than one."
  - Dịch: Gõ tay công cụ bộ nhớ / điều phối AI agents đã dùng nhưng chưa có trong danh sách.
- **Kiểu:** văn bản tự do

### 163. `AIAgentOrchestration` — Công cụ điều phối / framework cho AI agents

- **Lời dẫn (schema):** "You indicated you use or develop AI agents as part of your development work. Have you used any of the following tools for AI agent orchestration or agent frameworks in the past year?"
  - Dịch: Công cụ điều phối hoặc framework cho AI agents đã dùng trong năm qua.
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 164. `AIAgentOrchWrite` — Gõ tay: công cụ điều phối / framework AI agents

- **Lời dẫn (schema):** "Was the tool or tools for AI agent orchestration or agent frameworks you used in the past year not listed above? Please write them below separated by a comma and a space if there are more than one."
  - Dịch: Gõ tay công cụ điều phối / framework AI agents đã dùng nhưng chưa có trong danh sách.
- **Kiểu:** văn bản tự do

### 165. `AIAgentObserveSecure` — Công cụ quan sát, giám sát & bảo mật cho AI agents

- **Lời dẫn (schema):** "You indicated you use or develop AI agents as part of your development work. Have you used any of the following tools for AI agent observability, monitoring or security in the past year?"
  - Dịch: Công cụ quan sát, giám sát hoặc bảo mật cho AI agents đã dùng trong năm qua.
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 166. `AIAgentObsWrite` — Gõ tay: công cụ giám sát & bảo mật AI agents

- **Lời dẫn (schema):** "Was the tool or tools for AI agent observability, monitoring or security you used in the past year not listed above? Please write them below separated by a comma and a space if there are more than one."
  - Dịch: Gõ tay công cụ giám sát hoặc bảo mật AI agents đã dùng nhưng chưa có trong danh sách.
- **Kiểu:** văn bản tự do

### 167. `AIAgentExternal` — Agent, copilot hoặc trợ lý AI đóng gói sẵn đã dùng

- **Lời dẫn (schema):** "You indicated you use or develop AI agents as part of your development work. Have you used any of the following out-of-the-box agents, copilots or assistants?"
  - Dịch: Các agent, copilot hoặc trợ lý AI đóng gói sẵn đã sử dụng.
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 168. `AIAgentExtWrite` — Gõ tay: agent, copilot hoặc trợ lý AI đóng gói sẵn

- **Lời dẫn (schema):** "Was the out-of-the-box agents, copilots or assistants you used in the past year not listed above? Please write them below separated by a comma and a space for each..."
  - Dịch: Gõ tay agent, copilot hoặc trợ lý AI đóng gói sẵn đã dùng nhưng chưa có trong danh sách.
- **Kiểu:** văn bản tự do

### 169. `AIHuman` — Tình huống vẫn muốn nhờ con người hỗ trợ khi AI làm được hầu hết việc code

- **Lời dẫn (schema):** "In the future, if AI can do most coding tasks, in which situations would you still want to ask another person for help? Select all that apply."
  - Dịch: Trong tương lai, nếu AI làm được hầu hết tác vụ lập trình, bạn vẫn muốn nhờ người khác hỗ trợ trong tình huống nào?
- **Kiểu:** chọn **nhiều** đáp án, nối bằng `;`

### 170. `AIOpen` — Câu hỏi mở: kỹ năng nào vẫn có giá trị trong 3–5 năm tới

- **Lời dẫn (schema):** "Looking ahead 3–5 years, what skills do you believe will remain valuable for developers even as AI tools become more capable? Please describe."
  - Dịch: Nhìn về 3–5 năm tới, kỹ năng nào vẫn giữ được giá trị cho lập trình viên khi công cụ AI ngày càng mạnh hơn?
- **Kiểu:** văn bản tự do

### 171. `ConvertedCompYearly` — Tổng thu nhập quy đổi theo năm (USD)

- **Ý nghĩa:** Mức thu nhập hằng năm đã quy đổi sang USD của người trả lời (ví dụ dòng mẫu: `61256`).
- **Kiểu:** số liên tục (`Numeric`)
- **Lưu ý:** Là gốc để tạo nhãn phân loại thu nhập thấp / trung bình / cao (sau quy đổi tiền tệ & cắt ngoại lai); **không đưa vào tập đặc trưng** để tránh rò rỉ nhãn.

### 172. `JobSat` — Mức độ hài lòng với công việc hiện tại

- **Ý nghĩa:** Mức độ hài lòng của người trả lời đối với công việc hiện tại (ví dụ dòng mẫu: `10`).
- **Kiểu:** số / thang điểm (`Numeric`)
- **Lưu ý:** Phản ánh cảm nhận chủ quan cá nhân, loại bỏ khỏi tập đặc trưng.
