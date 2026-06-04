---
type: protein-evaluation
gene: "DEF6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DEF6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DEF6 / DEF6 |
| 蛋白名称 | Defensin-6 |
| 蛋白大小 | 100 aa / 11.0 kDa |
| UniProt ID | Q01524 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: Secreted; Cytoplasmic vesicle, secretory vesicle |
| 蛋白大小 | 8/10 | ×1 | 8 | 100 aa / 11.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=39 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.0; PDB: 1ZMQ, 3QTE |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016327, IPR006081, IPR002366, IPR006080; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **106.5/180** | |
| **归一化总分** | | | **59.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Secreted; Cytoplasmic vesicle, secretory vesicle | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- extracellular region (GO:0005576)
- extracellular space (GO:0005615)
- Golgi lumen (GO:0005796)
- transport vesicle (GO:0030133)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 39 |
| PubMed broad count | 86 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DEF6 |

**关键文献**:
1. Primary Immune Regulatory Disorders With an Autoimmune Lymphoproliferative Syndrome-Like Phenotype: Immunologic Evaluation, Early Diagnosis and Management.. *Frontiers in immunology*. PMID: 34447369
2. CTLA4-related primary immune dysregulatory disorders.. *Current opinion in allergy and clinical immunology*. PMID: 41158012
3. Different Apples, Same Tree: Visualizing Current Biological and Clinical Insights into CTLA-4 Insufficiency and LRBA and DEF6 Deficiencies.. *Frontiers in pediatrics*. PMID: 33996698
4. Def6 Restrains Osteoclastogenesis and Inflammatory Bone Resorption.. *Journal of immunology (Baltimore, Md. : 1950)*. PMID: 28314855
5. Inborn errors of regulatory T-cell differentiation and function.. *The Journal of allergy and clinical immunology*. PMID: 40633593

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.0 |
| 高置信度残基 (pLDDT>90) 占比 | 29.0% |
| 置信残基 (pLDDT 70-90) 占比 | 16.0% |
| 中等置信 (pLDDT 50-70) 占比 | 27.0% |
| 低置信 (pLDDT<50) 占比 | 28.0% |
| 有序区域 (pLDDT>70) 占比 | 45.0% |
| 可用 PDB 条目 | 1ZMQ, 3QTE |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=67.0），有序残基占 45.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016327, IPR006081, IPR002366, IPR006080; Pfam: PF00323, PF00879 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| IRF4 | 0.829 | 0.000 | — |
| BRCC3 | 0.822 | 0.821 | — |
| CDC42 | 0.796 | 0.334 | — |
| BABAM1 | 0.784 | 0.782 | — |
| BABAM2 | 0.780 | 0.779 | — |
| RAC2 | 0.760 | 0.334 | — |
| RHOA | 0.666 | 0.334 | — |
| LCK | 0.638 | 0.066 | — |
| ABRAXAS2 | 0.622 | 0.620 | — |
| RABIF | 0.605 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BEGAIN | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| Itga7 | psi-mi:"MI:0018"(two hybrid) | pubmed:17403664|imex:IM-19346 |
| ENSP00000319831.5 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| purD | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Pag1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:26512138|imex:IM-25616 |
| DEFA6 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| REL | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| RASAL3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GOLGA6L9 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| L3MBTL3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.0 + PDB: 1ZMQ, 3QTE | pLDDT=67.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Secreted; Cytoplasmic vesicle, secretory vesicle / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DEF6 — Defensin-6，非常新颖，仅有少数基础研究。
2. 蛋白大小100 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 39 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=67.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q01524
- Protein Atlas: https://www.proteinatlas.org/ENSG00000023892-DEF6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DEF6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q01524
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
