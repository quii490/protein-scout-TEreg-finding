---
type: protein-evaluation
gene: "GORAB"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GORAB 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GORAB / NTKLBP1, SCYL1BP1 |
| 蛋白名称 | RAB6-interacting golgin |
| 蛋白大小 | 369 aa / 42.3 kDa |
| UniProt ID | Q5T7V8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Golgi apparatus; 额外: Nucleoli, Cytosol; UniProt: Cytoplasm; Golgi apparatus |
| 蛋白大小 | 10/10 | ×1 | 10 | 369 aa / 42.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=30 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007033; Pfam: PF04949 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Golgi apparatus; 额外: Nucleoli, Cytosol | Supported |
| UniProt | Cytoplasm; Golgi apparatus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 30 |
| PubMed broad count | 136 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NTKLBP1, SCYL1BP1 |

**关键文献**:
1. Vimentin intermediate filaments provide structural stability to the mammalian Golgi complex.. *Journal of cell science*. PMID: 37732478
2. GORAB Missense Mutations Disrupt RAB6 and ARF5 Binding and Golgi Targeting.. *The Journal of investigative dermatology*. PMID: 26000619
3. Targeting TGF-β signaling, oxidative stress, and cellular senescence rescues osteoporosis in gerodermia osteodysplastica.. *Aging cell*. PMID: 39234801
4. Identification of Hypoxia and Mitochondrial-related Gene Signature and Prediction of Prognostic Model in Lung Adenocarcinoma.. *Journal of Cancer*. PMID: 39006078
5. GORAB scaffolds COPI at the trans-Golgi for efficient enzyme recycling and correct protein glycosylation.. *Nature communications*. PMID: 30631079

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.9 |
| 高置信度残基 (pLDDT>90) 占比 | 36.9% |
| 置信残基 (pLDDT 70-90) 占比 | 15.2% |
| 中等置信 (pLDDT 50-70) 占比 | 14.6% |
| 低置信 (pLDDT<50) 占比 | 33.3% |
| 有序区域 (pLDDT>70) 占比 | 52.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=70.9，有序区 52.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007033; Pfam: PF04949 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SCYL1 | 0.990 | 0.431 | — |
| RAB6A | 0.982 | 0.328 | — |
| RCHY1 | 0.974 | 0.550 | — |
| PYCR1 | 0.823 | 0.000 | — |
| ARF5 | 0.745 | 0.292 | — |
| ATP6V0A2 | 0.742 | 0.000 | — |
| PDIK1L | 0.667 | 0.000 | — |
| EFEMP2 | 0.638 | 0.000 | — |
| MDM2 | 0.610 | 0.292 | — |
| RIN2 | 0.587 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SCYL1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| RCHY1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| ZNF16 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| NEDD4L | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| BET1L | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| HSD17B7 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| HOXD9 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| NKG7 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| PTAFR | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| FARSA | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.9 + PDB: 无 | pLDDT=70.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Golgi apparatus / Nucleoplasm, Golgi apparatus; 额外: Nucleoli, Cytoso | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GORAB — RAB6-interacting golgin，非常新颖，仅有少数基础研究。
2. 蛋白大小369 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 30 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5T7V8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000120370-GORAB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GORAB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5T7V8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
