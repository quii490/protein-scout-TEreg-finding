---
type: protein-evaluation
gene: "CLINT1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CLINT1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLINT1 |
| 蛋白名称 | Clathrin interactor 1 isoform 2 |
| 蛋白大小 | 643 aa / 70.3 kDa |
| UniProt ID | A0A0S2Z5H3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Vesicles; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | x1 | 10 | 643 aa / 70.3 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=24 篇 (≤40→8) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=50.4; PDB: 无 |
| 调控结构域 | 5/10 | x2 | 10 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **103.5/180** | |
| **归一化总分** | | | **57.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm | Supported |
| UniProt | 无注释 | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 24 |
| PubMed broad count | 49 |
| 别名(未计入scoring) |  |

**关键文献**:
1. CLINT1 is a subtype-specific biomarker and a downstream effector of p53-R273H in lung adenocarcinoma migration.. *Acta Biochim Biophys Sin (Shanghai)*. PMID: 42115009
2. Polygenic insight identifies precision biomarkers decoding protein catabolism and autophagy pathways in obstructive sleep apnea.. *Sci Rep*. PMID: 40759999
3. Identification of Genomic Structural Variations in Xinjiang Brown Cattle by Deep Sequencing and Their Association with Body Conformation Traits.. *Int J Mol Sci*. PMID: 40508044
4. Gamma-Aminobutyric Acid Type A Receptor Subunit Pi is a potential chemoresistance regulator in colorectal cancer.. *Mol Biol Rep*. PMID: 36696022
5. Identification of Prognostic Biomarkers for Breast Cancer Metastasis Using Penalized Additive Hazards Regression Model.. *Cancer Inform*. PMID: 36968522

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 50.4 |
| 高置信度残基 (pLDDT>90) 占比 | 16.6% |
| 置信残基 (pLDDT 70-90) 占比 | 5.8% |
| 中等置信 (pLDDT 50-70) 占比 | 10.7% |
| 低置信 (pLDDT<50) 占比 | 66.9% |
| 有序区域 (pLDDT>70) 占比 | 22.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=50.4），有序残基占 22.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VTI1B | 0.000 | 0.000 | — |
| PICALM | 0.000 | 0.000 | — |
| CLTC | 0.000 | 0.000 | — |
| CLTCL1 | 0.000 | 0.000 | — |
| AP2A1 | 0.000 | 0.000 | — |
| CLTB | 0.000 | 0.000 | — |
| GGA2 | 0.000 | 0.000 | — |
| AP1B1 | 0.000 | 0.000 | — |
| AP1G1 | 0.000 | 0.000 | — |
| PUM1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q14677 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9BXW4 | psi-mi:"MI:0096"(pull down) | pubmed:- |
| uniprotkb:O95166 | psi-mi:"MI:0096"(pull down) | pubmed:- |
| uniprotkb:A0A2U2GZL1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:A0A5P8YBI5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q8ZDX4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q14677-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 1 / 20 = 5%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 5%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=50.4 + PDB: 无 | pLDDT=50.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Vesicles; 额外: Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CLINT1 -- Clathrin interactor 1 isoform 2，非常新颖，仅有少数基础研究。
2. 蛋白大小643 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 24 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=50.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A0A0S2Z5H3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000113282-CLINT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLINT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A0A0S2Z5H3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
