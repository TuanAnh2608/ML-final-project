# Đề xuất giữ / bỏ cột 87–172 

**Quy ước:** *Giữ* = dùng làm đặc trưng; *Bỏ* = loại; *Giữ tạm* = cần để lọc đối tượng hoặc tạo nhãn, sau bước đó bỏ khỏi tập đặc trưng.

**Tiêu chí:** (1) bỏ cột quan điểm / thái độ / cảm nhận / đánh giá chủ quan hoặc dự đoán tương lai cá nhân; (2) bỏ văn bản tự do (`*Entry`, `*Entr`, `*Write`, `AIExplain`, `AIOpen`, `SO_Actions_15_TEXT`); (3) bỏ cột điều hướng `*Choice`, nguyện vọng `*WantToWorkWith`, cột trùng lặp `*Admired` và nhánh ít dữ liệu / liên hệ yếu; (4) quy tắc NaN >= 50% đánh giá sau khi lọc đối tượng (16.991 / 15.160 dòng), không loại nhầm cột thực tế có độ phủ tốt sau lọc.

**Tổng kết:** Giữ 7 cột, Giữ tạm 1 cột, Bỏ 78 cột (tổng 86 cột từ vị trí 87 đến 172 trên bảng khảo sát).

| # | Cột | Giữ/Bỏ | Lý do |
|---|---|---|---|
| 87 | `WebframeHaveEntry` | Bỏ | Văn bản tự do, nhiễu, tỉ lệ NaN rất cao. |
| 88 | `WebframeWantEntry` | Bỏ | Văn bản tự do, nhiễu, tỉ lệ NaN rất cao. |
| 89 | `DevEnvsChoice` | Bỏ | Chỉ 2 giá trị (Yes/No); No luôn ứng với danh sách trống, trùng thông tin. |
| 90 | `DevEnvsHaveWorkedWith` | Giữ | Đặc trưng công cụ phát triển / AI code editor thực tế; kiểm tra NaN < 50% sau lọc đối tượng. |
| 91 | `DevEnvsWantToWorkWith` | Bỏ | Nguyện vọng tương lai, không phải thực tế hiện tại. |
| 92 | `DevEnvsAdmired` | Bỏ | Trùng lặp / suy ra được từ phần giao của HaveWorkedWith và WantToWorkWith; thiên về đánh giá cá nhân. |
| 93 | `DevEnvHaveEntry` | Bỏ | Văn bản tự do, nhiễu, tỉ lệ NaN rất cao. |
| 94 | `DevEnvWantEntry` | Bỏ | Văn bản tự do, nhiễu, tỉ lệ NaN rất cao. |
| 95 | `SOTagsHaveWorkedWith` | Bỏ | Tag mới nổi trên Stack Overflow, độ phủ thấp, liên hệ lương yếu. |
| 96 | `SOTagsWantToWorkWith` | Bỏ | Nguyện vọng tương lai, không phải thực tế hiện tại. |
| 97 | `SOTagsAdmired` | Bỏ | Trùng lặp / suy ra được từ phần giao của HaveWorkedWith và WantToWorkWith; thiên về đánh giá cá nhân. |
| 98 | `SOTagsHaveEntry` | Bỏ | Văn bản tự do, nhiễu, tỉ lệ NaN rất cao. |
| 99 | `SOTagsWant Entry` | Bỏ | Văn bản tự do, nhiễu, tỉ lệ NaN rất cao. |
| 100 | `OpSysPersonal use` | Giữ | Hệ điều hành sử dụng thực tế; OpSysProfessional use phản ánh môi trường làm việc trực tiếp, kiểm tra NaN < 50% sau lọc. |
| 101 | `OpSysProfessional use` | Giữ | Hệ điều hành sử dụng thực tế; OpSysProfessional use phản ánh môi trường làm việc trực tiếp, kiểm tra NaN < 50% sau lọc. |
| 102 | `OfficeStackAsyncHaveWorkedWith` | Giữ | Công cụ quản lý công việc cộng tác & tài liệu mã nguồn đang dùng thực tế; kiểm tra NaN < 50% sau lọc. |
| 103 | `OfficeStackAsyncWantToWorkWith` | Bỏ | Nguyện vọng tương lai, không phải thực tế hiện tại. |
| 104 | `OfficeStackAsyncAdmired` | Bỏ | Trùng lặp / suy ra được từ phần giao của HaveWorkedWith và WantToWorkWith; thiên về đánh giá cá nhân. |
| 105 | `OfficeStackHaveEntry` | Bỏ | Văn bản tự do, nhiễu, tỉ lệ NaN rất cao. |
| 106 | `OfficeStackWantEntry` | Bỏ | Văn bản tự do, nhiễu, tỉ lệ NaN rất cao. |
| 107 | `CommPlatformHaveWorkedWith` | Bỏ | Nền tảng cộng đồng / thói quen giao tiếp cá nhân, liên hệ lương yếu. |
| 108 | `CommPlatformWantToWorkWith` | Bỏ | Nguyện vọng tương lai, không phải thực tế hiện tại. |
| 109 | `CommPlatformAdmired` | Bỏ | Trùng lặp / suy ra được từ phần giao của HaveWorkedWith và WantToWorkWith; thiên về đánh giá cá nhân. |
| 110 | `CommPlatformHaveEntr` | Bỏ | Văn bản tự do, nhiễu, tỉ lệ NaN rất cao. |
| 111 | `CommPlatformWantEntr` | Bỏ | Văn bản tự do, nhiễu, tỉ lệ NaN rất cao. |
| 112 | `AIModelsChoice` | Bỏ | Chỉ 2 giá trị (Yes/No); No luôn ứng với danh sách trống, trùng thông tin. |
| 113 | `AIModelsHaveWorkedWith` | Giữ | Mô hình LLM đã dùng trong công việc phát triển; kiểm tra NaN < 50% sau lọc. |
| 114 | `AIModelsWantToWorkWith` | Bỏ | Nguyện vọng tương lai, không phải thực tế hiện tại. |
| 115 | `AIModelsAdmired` | Bỏ | Trùng lặp / suy ra được từ phần giao của HaveWorkedWith và WantToWorkWith; thiên về đánh giá cá nhân. |
| 116 | `AIModelsHaveEntry` | Bỏ | Văn bản tự do, nhiễu, tỉ lệ NaN rất cao. |
| 117 | `AIModelsWantEntry` | Bỏ | Văn bản tự do, nhiễu, tỉ lệ NaN rất cao. |
| 118 | `SOAccount` | Bỏ | Hành vi / thói quen / cảm nhận cá nhân trên Stack Overflow, không phản ánh trực tiếp thu nhập. |
| 119 | `SOVisitFreq` | Bỏ | Hành vi / thói quen / cảm nhận cá nhân trên Stack Overflow, không phản ánh trực tiếp thu nhập. |
| 120 | `SODuration` | Bỏ | Hành vi / thói quen / cảm nhận cá nhân trên Stack Overflow, không phản ánh trực tiếp thu nhập. |
| 121 | `SOPartFreq` | Bỏ | Hành vi / thói quen / cảm nhận cá nhân trên Stack Overflow, không phản ánh trực tiếp thu nhập. |
| 122 | `SO_Dev_Content` | Bỏ | Hành vi / thói quen / cảm nhận cá nhân trên Stack Overflow, không phản ánh trực tiếp thu nhập. |
| 123 | `SO_Actions_1` | Bỏ | Xếp hạng / hành động tương tác trên Stack Overflow, không thuộc đặc trưng lương cốt lõi. |
| 124 | `SO_Actions_16` | Bỏ | Xếp hạng / hành động tương tác trên Stack Overflow, không thuộc đặc trưng lương cốt lõi. |
| 125 | `SO_Actions_3` | Bỏ | Xếp hạng / hành động tương tác trên Stack Overflow, không thuộc đặc trưng lương cốt lõi. |
| 126 | `SO_Actions_4` | Bỏ | Xếp hạng / hành động tương tác trên Stack Overflow, không thuộc đặc trưng lương cốt lõi. |
| 127 | `SO_Actions_5` | Bỏ | Xếp hạng / hành động tương tác trên Stack Overflow, không thuộc đặc trưng lương cốt lõi. |
| 128 | `SO_Actions_6` | Bỏ | Xếp hạng / hành động tương tác trên Stack Overflow, không thuộc đặc trưng lương cốt lõi. |
| 129 | `SO_Actions_9` | Bỏ | Xếp hạng / hành động tương tác trên Stack Overflow, không thuộc đặc trưng lương cốt lõi. |
| 130 | `SO_Actions_7` | Bỏ | Xếp hạng / hành động tương tác trên Stack Overflow, không thuộc đặc trưng lương cốt lõi. |
| 131 | `SO_Actions_10` | Bỏ | Xếp hạng / hành động tương tác trên Stack Overflow, không thuộc đặc trưng lương cốt lõi. |
| 132 | `SO_Actions_15` | Bỏ | Xếp hạng / hành động tương tác trên Stack Overflow, không thuộc đặc trưng lương cốt lõi. |
| 133 | `SO_Actions_15_TEXT` | Bỏ | Văn bản tự do, nhiễu, tỉ lệ NaN rất cao. |
| 134 | `SOComm` | Bỏ | Hành vi / thói quen / cảm nhận cá nhân trên Stack Overflow, không phản ánh trực tiếp thu nhập. |
| 135 | `SOFriction` | Bỏ | Hành vi / thói quen / cảm nhận cá nhân trên Stack Overflow, không phản ánh trực tiếp thu nhập. |
| 136 | `AISelect` | Giữ | Hành vi áp dụng công cụ AI thực tế trong quy trình phát triển. |
| 137 | `AISent` | Bỏ | Quan điểm / thái độ / cảm nhận / đánh giá chủ quan cá nhân. |
| 138 | `AIAcc` | Bỏ | Quan điểm / thái độ / cảm nhận / đánh giá chủ quan cá nhân. |
| 139 | `AIComplex` | Bỏ | Quan điểm / thái độ / cảm nhận / đánh giá chủ quan cá nhân. |
| 140 | `AIToolCurrently partially AI` | Bỏ | Cột con của AITool (kế hoạch tương lai hoặc mức độ riêng lẻ); chỉ cân nhắc giữ nếu cột đang dùng thực tế có NaN < 50% sau lọc. |
| 141 | `AIToolDon't plan to use AI for this task` | Bỏ | Cột con của AITool (kế hoạch tương lai hoặc mức độ riêng lẻ); chỉ cân nhắc giữ nếu cột đang dùng thực tế có NaN < 50% sau lọc. |
| 142 | `AIToolPlan to partially use AI` | Bỏ | Cột con của AITool (kế hoạch tương lai hoặc mức độ riêng lẻ); chỉ cân nhắc giữ nếu cột đang dùng thực tế có NaN < 50% sau lọc. |
| 143 | `AIToolPlan to mostly use AI` | Bỏ | Cột con của AITool (kế hoạch tương lai hoặc mức độ riêng lẻ); chỉ cân nhắc giữ nếu cột đang dùng thực tế có NaN < 50% sau lọc. |
| 144 | `AIToolCurrently mostly AI` | Bỏ | Cột con của AITool (kế hoạch tương lai hoặc mức độ riêng lẻ); chỉ cân nhắc giữ nếu cột đang dùng thực tế có NaN < 50% sau lọc. |
| 145 | `AIFrustration` | Bỏ | Quan điểm / thái độ / cảm nhận / đánh giá chủ quan cá nhân. |
| 146 | `AIExplain` | Bỏ | Văn bản tự do, nhiễu, tỉ lệ NaN rất cao. |
| 147 | `AIAgents` | Giữ | Hành vi sử dụng AI agents thực tế trong công việc; kiểm tra NaN < 50% sau lọc. |
| 148 | `AIAgentChange` | Bỏ | Quan điểm / thái độ / cảm nhận / đánh giá chủ quan cá nhân. |
| 149 | `AIAgent_Uses` | Bỏ | Nhánh AI agents hẹp, tỉ lệ NaN cao sau lọc đối tượng. |
| 150 | `AgentUsesGeneral` | Bỏ | Nhánh AI agents hẹp, tỉ lệ NaN cao sau lọc đối tượng. |
| 151 | `AIAgentImpactSomewhat agree` | Bỏ | Thang đo đồng ý về tác động / thách thức của AI agents, quan điểm chủ quan và NaN cao. |
| 152 | `AIAgentImpactNeutral` | Bỏ | Thang đo đồng ý về tác động / thách thức của AI agents, quan điểm chủ quan và NaN cao. |
| 153 | `AIAgentImpactSomewhat disagree` | Bỏ | Thang đo đồng ý về tác động / thách thức của AI agents, quan điểm chủ quan và NaN cao. |
| 154 | `AIAgentImpactStrongly agree` | Bỏ | Thang đo đồng ý về tác động / thách thức của AI agents, quan điểm chủ quan và NaN cao. |
| 155 | `AIAgentImpactStrongly disagree` | Bỏ | Thang đo đồng ý về tác động / thách thức của AI agents, quan điểm chủ quan và NaN cao. |
| 156 | `AIAgentChallengesNeutral` | Bỏ | Thang đo đồng ý về tác động / thách thức của AI agents, quan điểm chủ quan và NaN cao. |
| 157 | `AIAgentChallengesSomewhat disagree` | Bỏ | Thang đo đồng ý về tác động / thách thức của AI agents, quan điểm chủ quan và NaN cao. |
| 158 | `AIAgentChallengesStrongly agree` | Bỏ | Thang đo đồng ý về tác động / thách thức của AI agents, quan điểm chủ quan và NaN cao. |
| 159 | `AIAgentChallengesSomewhat agree` | Bỏ | Thang đo đồng ý về tác động / thách thức của AI agents, quan điểm chủ quan và NaN cao. |
| 160 | `AIAgentChallengesStrongly disagree` | Bỏ | Thang đo đồng ý về tác động / thách thức của AI agents, quan điểm chủ quan và NaN cao. |
| 161 | `AIAgentKnowledge` | Bỏ | Nhánh AI agents hẹp, tỉ lệ NaN cao sau lọc đối tượng. |
| 162 | `AIAgentKnowWrite` | Bỏ | Văn bản tự do, nhiễu, tỉ lệ NaN rất cao. |
| 163 | `AIAgentOrchestration` | Bỏ | Nhánh AI agents hẹp, tỉ lệ NaN cao sau lọc đối tượng. |
| 164 | `AIAgentOrchWrite` | Bỏ | Văn bản tự do, nhiễu, tỉ lệ NaN rất cao. |
| 165 | `AIAgentObserveSecure` | Bỏ | Nhánh AI agents hẹp, tỉ lệ NaN cao sau lọc đối tượng. |
| 166 | `AIAgentObsWrite` | Bỏ | Văn bản tự do, nhiễu, tỉ lệ NaN rất cao. |
| 167 | `AIAgentExternal` | Bỏ | Nhánh AI agents hẹp, tỉ lệ NaN cao sau lọc đối tượng. |
| 168 | `AIAgentExtWrite` | Bỏ | Văn bản tự do, nhiễu, tỉ lệ NaN rất cao. |
| 169 | `AIHuman` | Bỏ | Quan điểm / thái độ / cảm nhận / đánh giá chủ quan cá nhân. |
| 170 | `AIOpen` | Bỏ | Văn bản tự do, nhiễu, tỉ lệ NaN rất cao. |
| 171 | `ConvertedCompYearly` | Giữ tạm | Là gốc để tạo nhãn phân loại thu nhập thấp / trung bình / cao (sau quy đổi & lọc ngoại lai); không đưa vào đặc trưng. |
| 172 | `JobSat` | Bỏ | Quan điểm / thái độ / cảm nhận / đánh giá chủ quan cá nhân. |

## Danh sách cột bỏ

```python
drop_cols = [
    "WebframeHaveEntry",
    "WebframeWantEntry",
    "DevEnvsChoice",
    "DevEnvsWantToWorkWith",
    "DevEnvsAdmired",
    "DevEnvHaveEntry",
    "DevEnvWantEntry",
    "SOTagsHaveWorkedWith",
    "SOTagsWantToWorkWith",
    "SOTagsAdmired",
    "SOTagsHaveEntry",
    "SOTagsWant Entry",
    "OfficeStackAsyncWantToWorkWith",
    "OfficeStackAsyncAdmired",
    "OfficeStackHaveEntry",
    "OfficeStackWantEntry",
    "CommPlatformHaveWorkedWith",
    "CommPlatformWantToWorkWith",
    "CommPlatformAdmired",
    "CommPlatformHaveEntr",
    "CommPlatformWantEntr",
    "AIModelsChoice",
    "AIModelsWantToWorkWith",
    "AIModelsAdmired",
    "AIModelsHaveEntry",
    "AIModelsWantEntry",
    "SOAccount",
    "SOVisitFreq",
    "SODuration",
    "SOPartFreq",
    "SO_Dev_Content",
    "SO_Actions_1",
    "SO_Actions_16",
    "SO_Actions_3",
    "SO_Actions_4",
    "SO_Actions_5",
    "SO_Actions_6",
    "SO_Actions_9",
    "SO_Actions_7",
    "SO_Actions_10",
    "SO_Actions_15",
    "SO_Actions_15_TEXT",
    "SOComm",
    "SOFriction",
    "AISent",
    "AIAcc",
    "AIComplex",
    "AIToolCurrently partially AI",
    "AIToolDon't plan to use AI for this task",
    "AIToolPlan to partially use AI",
    "AIToolPlan to mostly use AI",
    "AIToolCurrently mostly AI",
    "AIFrustration",
    "AIExplain",
    "AIAgentChange",
    "AIAgent_Uses",
    "AgentUsesGeneral",
    "AIAgentImpactSomewhat agree",
    "AIAgentImpactNeutral",
    "AIAgentImpactSomewhat disagree",
    "AIAgentImpactStrongly agree",
    "AIAgentImpactStrongly disagree",
    "AIAgentChallengesNeutral",
    "AIAgentChallengesSomewhat disagree",
    "AIAgentChallengesStrongly agree",
    "AIAgentChallengesSomewhat agree",
    "AIAgentChallengesStrongly disagree",
    "AIAgentKnowledge",
    "AIAgentKnowWrite",
    "AIAgentOrchestration",
    "AIAgentOrchWrite",
    "AIAgentObserveSecure",
    "AIAgentObsWrite",
    "AIAgentExternal",
    "AIAgentExtWrite",
    "AIHuman",
    "AIOpen",
    "JobSat",
]
```

## Danh sách cột giữ tạm (lọc / tạo nhãn rồi bỏ)

```python
drop_after_use = [
    "ConvertedCompYearly",
]
```
