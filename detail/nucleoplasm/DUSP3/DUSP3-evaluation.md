---
type: protein-evaluation
gene: "DUSP3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DUSP3 — REJECTED (研究热度过高 (PubMed strict=104，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DUSP3 |
| 蛋白名称 | Dual specificity protein phosphatase 3 |
| 蛋白大小 | 185 aa / 20.5 kDa |
| UniProt ID | P51452 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Cytoplasm, cytoskeleton, flagellum axoneme |
| 蛋白大小 | 8/10 | ×1 | 8 | 185 aa / 20.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=104 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=95.9; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **82.5/180** | |
| **归一化总分** | | | **45.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm, cytoskeleton, flagellum axoneme | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 104 |
| PubMed broad count | 139 |
| 别名(未计入scoring) |  |

**关键文献**:
1. DUSP family phosphatases in cell signaling, inflammation, and chronic diseases.. *J Biomed Sci*. PMID: 42087139
2. The Utility of a Three-gene Host Response to Discriminate Tuberculous Meningitis From Other Infections in Children.. *Pediatr Infect Dis J*. PMID: 41430759
3. A whole-blood transcriptional signature associated with obstructive post-tuberculosis lung disease.. *medRxiv*. PMID: 42051569
4. Atranorin Impedes Glioma Invasiveness and Progression by Inhibiting the Epithelial-Mesenchymal Transition and Stemness in Monotherapy and in Combination Therapy With Temozolomide.. *Phytother Res*. PMID: 41239946
5. Integration of human ERKs and DUSPs into the yeast cell wall integrity pathway.. *Sci Rep*. PMID: 41453955

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.9 |
| 高置信度残基 (pLDDT>90) 占比 | 92.4% |
| 置信残基 (pLDDT 70-90) 占比 | 4.3% |
| 中等置信 (pLDDT 50-70) 占比 | 1.6% |
| 低置信 (pLDDT<50) 占比 | 1.6% |
| 有序区域 (pLDDT>70) 占比 | 96.7% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 极高置信度预测（pLDDT=95.9，有序区 96.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VRK3 | 0.000 | 0.000 | — |
| MAPK1 | 0.000 | 0.000 | — |
| MAPK3 | 0.000 | 0.000 | — |
| PTPN7 | 0.000 | 0.000 | — |
| MAPK14 | 0.000 | 0.000 | — |
| MAPK8 | 0.000 | 0.000 | — |
| PTPRR | 0.000 | 0.000 | — |
| MAPK12 | 0.000 | 0.000 | — |
| MAPK9 | 0.000 | 0.000 | — |
| MAPK11 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:P51452 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:O60238 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q13562 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:P49411 | psi-mi:"MI:0030"(cross-linking study) | pubmed:- |
| uniprotkb:A0A0G2K064 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:A7VJC2 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| intact:EBI-22249836 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:B1WC33 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O08776 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q5XIM5 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.9 + PDB: 无 | pLDDT=95.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytoskeleton, flagellum axonem / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DUSP3 — Dual specificity protein phosphatase 3，研究基础较多，新颖性有限。
2. 蛋白大小185 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 104 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 104 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P51452
- Protein Atlas: https://www.proteinatlas.org/ENSG00000108861-DUSP3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DUSP3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P51452
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
