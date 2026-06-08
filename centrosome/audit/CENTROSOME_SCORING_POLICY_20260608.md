# Centrosome 模块独立评分政策（修订版）

**日期:** 2026-06-08
**模块:** centrosome

## 核心原则

- 不使用核定位评分淘汰
- PubMed > 100 篇 → 自动淘汰
- 5维度评分（无 TE relevance）

## 淘汰规则

- **PubMed 总数 > 100:** 自动淘汰（与主表一致）
- **不因核定位分数淘汰**

## 评分维度（总分 0–100）

| 维度 | 权重 | 说明 |
|------|:---:|------|
| 中心体证据 | ×4 | HPA + UniProt/GO-CC + 文献 |
| PubMed/文献 | ×4 | 文献总数 + 中心体特异性 |
| PPI/互作网络 | ×3 | STRING + IntAct + BioGRID |
| 结构/结构域 | ×2 | AlphaFold + PDB + InterPro/Pfam |
| 新颖性/特异性 | ×2 | 研究新颖性 + 中心体定位特异性 |

**计算公式:** raw = 中心体×4 + 文献×4 + PPI×3 + 结构×2 + 新颖×2
**归一化:** raw / 2.6 → 0–100

## 状态分类

| 状态 | 条件 |
|------|------|
| CENTROSOME_ELIMINATED | PubMed > 100 |
| CENTROSOME_CANDIDATE | 评分 ≥ 50 |
| CENTROSOME_LOW_PRIORITY | 评分 25–49 |
| CENTROSOME_MANUAL_REVIEW | 评分 < 25 或证据冲突 |
