---
type: protein-evaluation
gene: "EXOC5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EXOC5 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EXOC5 / SEC10, SEC10L1 |
| 蛋白名称 | Exocyst complex component 5 |
| 蛋白大小 | 708 aa / 81.9 kDa |
| UniProt ID | O00471 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Vesicles; UniProt: Cytoplasm; Midbody |
| 蛋白大小 | 10/10 | ×1 | 10 | 708 aa / 81.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=21 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=86.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR009976, IPR048627, IPR048625; Pfam: PF07393, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.5/180** | |
| **归一化总分** | | | **60.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles | Approved |
| UniProt | Cytoplasm; Midbody | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- exocyst (GO:0000145)
- midbody (GO:0030496)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 21 |
| PubMed broad count | 44 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SEC10, SEC10L1 |

**关键文献**:
1. Disrupted glucose homeostasis and skeletal-muscle-specific glucose uptake in an exocyst knockout mouse model.. *The Journal of biological chemistry*. PMID: 33647317
2. Disruption of the exocyst induces podocyte loss and dysfunction.. *The Journal of biological chemistry*. PMID: 31073028
3. The exocyst is required for photoreceptor ciliogenesis and retinal development.. *The Journal of biological chemistry*. PMID: 28729419
4. Exocyst inactivation in urothelial cells disrupts autophagy and activates non-canonical NF-κB signaling.. *Disease models & mechanisms*. PMID: 36004645
5. The exocyst acting through the primary cilium is necessary for renal ciliogenesis, cystogenesis, and tubulogenesis.. *The Journal of biological chemistry*. PMID: 30824539

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.7 |
| 高置信度残基 (pLDDT>90) 占比 | 55.1% |
| 置信残基 (pLDDT 70-90) 占比 | 34.9% |
| 中等置信 (pLDDT 50-70) 占比 | 6.6% |
| 低置信 (pLDDT<50) 占比 | 3.4% |
| 有序区域 (pLDDT>70) 占比 | 90.0% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=86.7，有序区 90.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009976, IPR048627, IPR048625; Pfam: PF07393, PF20667 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EXOC7 | 0.999 | 0.975 | — |
| EXOC6 | 0.999 | 0.979 | — |
| EXOC2 | 0.999 | 0.991 | — |
| EXOC4 | 0.999 | 0.993 | — |
| EXOC1 | 0.999 | 0.972 | — |
| EXOC3 | 0.999 | 0.979 | — |
| EXOC8 | 0.999 | 0.982 | — |
| EXOC6B | 0.997 | 0.975 | — |
| ARF6 | 0.974 | 0.328 | — |
| EXOC3L1 | 0.965 | 0.842 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q8IW24 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| PRKCG | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| Iqcb1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| CDH2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| ICA1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| SOX10 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| TBX21 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| ADCK1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| ACTR3B | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.7 + PDB: 无 | pLDDT=86.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Midbody / Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. EXOC5 — Exocyst complex component 5，非常新颖，仅有少数基础研究。
2. 蛋白大小708 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 21 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O00471
- Protein Atlas: https://www.proteinatlas.org/ENSG00000070367-EXOC5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EXOC5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O00471
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
