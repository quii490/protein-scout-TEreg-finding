---
type: protein-evaluation
gene: "IRAK3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## IRAK3 — REJECTED (研究热度过高 (PubMed strict=134，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | IRAK3 |
| 蛋白名称 | Interleukin-1 receptor-associated kinase 3 |
| 蛋白大小 | 596 aa / 67.8 kDa |
| UniProt ID | Q9Y616 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 596 aa / 67.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=134 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=71.5; PDB: 5UKE, 6RUU, 6ZIW |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011029, IPR000488, IPR042747, IPR042698, IPR011 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **87.5/180** | |
| **归一化总分** | | | **48.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 134 |
| PubMed broad count | 342 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Retraction.. *Journal of cellular physiology*. PMID: 35262927
2. Exploring the biological functions and immune regulatory roles of IRAK3, TNFRSF1A, CX3CR1, and JUNB in T2DM combined with MAFLD: integrated bioinformatics and single-cell analysis.. *Frontiers in immunology*. PMID: 40918148
3. IRAK3 is upregulated in rheumatoid arthritis synovium and delays the onset of experimental arthritis.. *Frontiers in immunology*. PMID: 40370470
4. IRAK3 Knockout and Wildtype THP-1 Monocytes as Models for Endotoxin Detection Assays and Fusobacterium nucleatum Bacteriophage FNU1 Cytokine Induction.. *International journal of molecular sciences*. PMID: 37894788
5. Regulation of the MIR155 host gene in physiological and pathological processes.. *Gene*. PMID: 23246696

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.5 |
| 高置信度残基 (pLDDT>90) 占比 | 39.6% |
| 置信残基 (pLDDT 70-90) 占比 | 23.0% |
| 中等置信 (pLDDT 50-70) 占比 | 6.4% |
| 低置信 (pLDDT<50) 占比 | 31.0% |
| 有序区域 (pLDDT>70) 占比 | 62.6% |
| 可用 PDB 条目 | 5UKE, 6RUU, 6ZIW |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（5UKE, 6RUU, 6ZIW）+ AlphaFold高质量预测（pLDDT=71.5），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011029, IPR000488, IPR042747, IPR042698, IPR011009; Pfam: PF00531, PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TICAM2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:12721283|imex:IM-30173 |
| CD14 | psi-mi:"MI:0663"(confocal microscopy) | imex:IM-15364|pubmed:21988832 |
| HOXB7 | psi-mi:"MI:0663"(confocal microscopy) | imex:IM-15364|pubmed:21988832 |
| NSA2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| NTRK3 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| NONO | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| LDB1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| ADH1B | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| COPB1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| ECM1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.5 + PDB: 5UKE, 6RUU, 6ZIW | pLDDT=71.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Vesicles | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. IRAK3 — Interleukin-1 receptor-associated kinase 3，研究基础较多，新颖性有限。
2. 蛋白大小596 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 134 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 134 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y616
- Protein Atlas: https://www.proteinatlas.org/ENSG00000090376-IRAK3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=IRAK3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y616
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
