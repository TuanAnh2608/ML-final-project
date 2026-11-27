"""
1. Xóa các cột đã được đề xuất
2. Liệt kê sl cột còn lại, cột giữ tạm, đặc trưng (số, chọn một, chọn nhiều)
3. Lưu dữ liệu đã lọc vào filtered_data.csv (Cần sửa đường dẫn)
"""

import pandas as pd

# Đọc dữ liệu gốc (chỉnh đường dẫn nếu cần)
df = pd.read_csv("./src/datasets/results.csv", low_memory=False)
print(f"Ban đầu: {df.shape[0]} hàng x {df.shape[1]} cột")


# DANH SÁCH CỘT BỎ
# Cột 1-86: 66 cột (column_selection_proposal_02_86.md)
drop_cols_02_86 = [
    "ResponseId",
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

# Cột 87-172: 78 cột (column_selection_proposal_87_172.md)
drop_cols_87_172 = [
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


drop_cols = drop_cols_02_86 + drop_cols_87_172
assert len(drop_cols) == len(set(drop_cols)), "Có cột bị trùng trong danh sách bỏ"


# BỎ CỘT (báo lỗi nếu tên cột trong danh sách không tồn tại)
df_clean = df.drop(columns=drop_cols)
print(f"Đã bỏ {len(drop_cols)} cột, còn {df_clean.shape[1]} cột")


# CÁC CỘT CÒN LẠI
kept_cols = df_clean.columns.tolist()  # toàn bộ cột còn lại

# Cột giữ tạm: dùng để lọc đối tượng và tạo nhãn, KHÔNG đưa vào X
FILTER_COLS = ["MainBranch", "Employment"]
SALARY_COLS = ["CompTotal", "Currency", "ConvertedCompYearly"]
temp_cols = FILTER_COLS + SALARY_COLS

# Đặc trưng
feature_cols = [c for c in kept_cols if c not in temp_cols]

# Phân loại đặc trưng theo kiểu dữ liệu
num_cols = df_clean[feature_cols].select_dtypes(include="number").columns.tolist()
cat_cols = [c for c in feature_cols if c not in num_cols]
# Cột chọn nhiều đáp án: ô chứa dấu ';' (nhận diện tự động từ dữ liệu)
multi_cols = [
    c for c in cat_cols if df_clean[c].dropna().astype(str).str.contains(";").any()
]
single_cols = [c for c in cat_cols if c not in multi_cols]

print("Cột còn lại      :", len(kept_cols))
print("Cột giữ tạm      :", len(temp_cols), temp_cols)
print("Đặc trưng        :", len(feature_cols))
print("  - Số           :", len(num_cols), num_cols)
print("  - Chọn một     :", len(single_cols), single_cols)
print("  - Chọn nhiều   :", len(multi_cols), multi_cols)
print("Số hàng còn lại  :", df_clean.shape[0])

df_clean.to_csv("./src/datasets/filtered_data.csv", index=False)
