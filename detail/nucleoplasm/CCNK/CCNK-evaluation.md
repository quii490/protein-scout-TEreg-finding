---
type: protein-evaluation
gene: "CCNK"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCNK 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCNK |
| 蛋白名称 | Cyclin-K |
| 蛋白大小 | 580 aa / 64.2 kDa |
| UniProt ID | O75909 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CCNK/IF_images/U-251MG_1.jpg|U 251MG]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CCNK/IF_images/MCF-7_1.jpg|MCF 7]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 8/10 | ×4 | 32 | HPA: Nucleoplasm; UniProt: Nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 580 aa / 64.2 kDa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=26 篇 (≤40→8) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.1; PDB: 无 |
| 🧬 调控结构域 | 5/10 | ×2 | 10 | 无注释结构域 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已嵌入

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 26 |
| PubMed broad count | 65 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Additional case report supports loss-of-function CCNK variants being causative for a recognizable syndromic neurodevelopmental disorder.. *Clin Dysmorphol*. PMID: 41661203
2. Dual-Stimuli-Responsive Nanoplatform Delivering Molecular Glue CR8 for Synergistic CDK12 Degradation and Immunomodulatory Photothermal Therapy in TNBC.. *ACS Appl Mater Interfaces*. PMID: 41810739
3. A Further Case Supporting CCNK as a Neurodevelopmental Disease Gene.. *Clin Genet*. PMID: 41101726
4. Overexpression of CCNK Leads to Early Resumption of Meiosis in Mouse Oocytes.. *Mol Reprod Dev*. PMID: 41355749
5. Discovery of Highly Potent and Orally Available CCNK Molecular Glue Degraders as Broad-Spectrum Antitumor Agents.. *J Med Chem*. PMID: 41165741

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.1 |
| 高置信度残基 (pLDDT>90) 占比 | 39.5% |
| 置信残基 (pLDDT 70-90) 占比 | 2.1% |
| 中等置信 (pLDDT 50-70) 占比 | 11.0% |
| 低置信 (pLDDT<50) 占比 | 47.4% |
| 有序区域 (pLDDT>70) 占比 | 41.6% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CCNK/CCNK-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=65.1），有序残基占 41.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDK12 | 0.000 | 0.000 | — |
| CDK13 | 0.000 | 0.000 | — |
| CDK9 | 0.000 | 0.000 | — |
| POLR2A | 0.000 | 0.000 | — |
| DDB1 | 0.000 | 0.000 | — |
| CDK7 | 0.000 | 0.000 | — |
| CCNT2 | 0.000 | 0.000 | — |
| CCNH | 0.000 | 0.000 | — |
| CNOT2 | 0.000 | 0.000 | — |
| CTDP1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9BQY4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9BQ66 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:O75909 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9NP66 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q93062 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q8TAP6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q8N6Y0 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:O95967 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q8N5I3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q8HWS3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.1 + PDB: 无 | pLDDT=65.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CCNK — Cyclin-K，非常新颖，仅有少数基础研究。
2. 蛋白大小580 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 26 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=65.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75909
- Protein Atlas: https://www.proteinatlas.org/ENSG00000090061-CCNK/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCNK
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75909
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CCNK/CCNK-PAE.png]]




