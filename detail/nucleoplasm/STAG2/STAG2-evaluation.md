---
type: protein-evaluation
gene: "STAG2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## STAG2 — REJECTED (研究热度过高 (PubMed strict=254，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | STAG2 / SA2 |
| 蛋白名称 | Cohesin subunit SA-2 |
| 蛋白大小 | 1231 aa / 141.3 kDa |
| UniProt ID | Q8N3U4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli, Nucleoli fibrillar center; UniProt: Nucleus; Chromosome; Chromosome, centromere |
| 蛋白大小 | 5/10 | ×1 | 5 | 1231 aa / 141.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=254 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=79.5; PDB: 4PJU, 4PJW, 4PK7, 6QNX, 7ZJS, 8K4D, 9HMS |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016024, IPR039662, IPR056396, IPR020839, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.0/180** | |
| **归一化总分** | | | **49.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli, Nucleoli fibrillar center | Supported |
| UniProt | Nucleus; Chromosome; Chromosome, centromere | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- chromosome (GO:0005694)
- chromosome, centromeric region (GO:0000775)
- cohesin complex (GO:0008278)
- cytosol (GO:0005829)
- fibrillar center (GO:0001650)
- membrane (GO:0016020)
- mitotic cohesin complex (GO:0030892)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 254 |
| PubMed broad count | 436 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SA2 |

**关键文献**:
1. Ewing sarcoma.. *Nature reviews. Disease primers*. PMID: 29977059
2. The spectrum of GATA2 deficiency syndrome.. *Blood*. PMID: 36455197
3. What is new in acute myeloid leukemia classification?. *Blood research*. PMID: 38616211
4. Mouse and human urothelial cancer organoids: A tool for bladder cancer research.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 30787188
5. The expanding phenotypes of cohesinopathies: one ring to rule them all!. *Cell cycle (Georgetown, Tex.)*. PMID: 31516082

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.5 |
| 高置信度残基 (pLDDT>90) 占比 | 63.1% |
| 置信残基 (pLDDT 70-90) 占比 | 12.8% |
| 中等置信 (pLDDT 50-70) 占比 | 2.2% |
| 低置信 (pLDDT<50) 占比 | 21.9% |
| 有序区域 (pLDDT>70) 占比 | 75.9% |
| 可用 PDB 条目 | 4PJU, 4PJW, 4PK7, 6QNX, 7ZJS, 8K4D, 9HMS, 9HMV |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（4PJU, 4PJW, 4PK7, 6QNX, 7ZJS, 8K4D, 9HMS, 9HMV）+ AlphaFold极高置信度预测（pLDDT=79.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016024, IPR039662, IPR056396, IPR020839, IPR013721; Pfam: PF24571, PF21581, PF08514 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SMC3 | 0.999 | 0.979 | — |
| RAD21 | 0.999 | 0.999 | — |
| PDS5A | 0.999 | 0.895 | — |
| SMC1A | 0.999 | 0.945 | — |
| WAPL | 0.997 | 0.893 | — |
| SMC1B | 0.997 | 0.842 | — |
| PDS5B | 0.996 | 0.857 | — |
| STAG1 | 0.996 | 0.792 | — |
| REC8 | 0.993 | 0.569 | — |
| ESPL1 | 0.987 | 0.094 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSMUSP00000110724.2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| smc1a | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:10931856 |
| smc3 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:10931856 |
| rad21 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:10931856 |
| WAPL | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12007|pubmed:17113138 |
| PDS5A | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12007|pubmed:17113138 |
| PDS5B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12007|pubmed:17113138 |
| MYC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ITGB1BP2 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| ENSP00000397265.2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 3 / 15 = 20%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 20%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.5 + PDB: 4PJU, 4PJW, 4PK7, 6QNX, 7ZJS,  | pLDDT=79.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome; Chromosome, centromere / Nucleoplasm, Nucleoli, Nucleoli fibrillar center | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. STAG2 — Cohesin subunit SA-2，研究基础较多，新颖性有限。
2. 蛋白大小1231 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 254 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 254 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N3U4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000101972-STAG2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STAG2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N3U4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
