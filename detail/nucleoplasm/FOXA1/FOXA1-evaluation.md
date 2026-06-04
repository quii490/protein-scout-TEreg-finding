---
type: protein-evaluation
gene: "FOXA1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FOXA1 — REJECTED (研究热度过高 (PubMed strict=1052，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FOXA1 / HNF3A, TCF3A |
| 蛋白名称 | Hepatocyte nuclear factor 3-alpha |
| 蛋白大小 | 472 aa / 49.1 kDa |
| UniProt ID | P55317 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Nucleoli fibrillar center; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 472 aa / 49.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1052 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.7; PDB: 7VOX, 8VFY, 8VFZ, 8VG1, 8VG2 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR013638, IPR001766, IPR018533, IPR050211, IPR018 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.5/180** | |
| **归一化总分** | | | **49.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli fibrillar center | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- fibrillar center (GO:0001650)
- microvillus (GO:0005902)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1052 |
| PubMed broad count | 1856 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HNF3A, TCF3A |

**关键文献**:
1. The Molecular Taxonomy of Primary Prostate Cancer.. *Cell*. PMID: 26544944
2. Targeting SWI/SNF ATPases in enhancer-addicted prostate cancer.. *Nature*. PMID: 34937944
3. FOXA1 mutations alter pioneering activity, differentiation and prostate cancer phenotypes.. *Nature*. PMID: 31243370
4. Redirecting the pioneering function of FOXA1 with covalent small molecules.. *Molecular cell*. PMID: 39413792
5. Integrated analysis reveals FOXA1 and Ku70/Ku80 as targets of ivermectin in prostate cancer.. *Cell death & disease*. PMID: 36050295

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.7 |
| 高置信度残基 (pLDDT>90) 占比 | 14.8% |
| 置信残基 (pLDDT 70-90) 占比 | 4.9% |
| 中等置信 (pLDDT 50-70) 占比 | 19.5% |
| 低置信 (pLDDT<50) 占比 | 60.8% |
| 有序区域 (pLDDT>70) 占比 | 19.7% |
| 可用 PDB 条目 | 7VOX, 8VFY, 8VFZ, 8VG1, 8VG2 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=55.7），有序残基占 19.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013638, IPR001766, IPR018533, IPR050211, IPR018122; Pfam: PF00250, PF08430, PF09354 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ESR1 | 0.998 | 0.626 | — |
| GATA3 | 0.997 | 0.484 | — |
| AR | 0.996 | 0.761 | — |
| HDAC7 | 0.976 | 0.510 | — |
| TLE3 | 0.976 | 0.292 | — |
| EP300 | 0.933 | 0.000 | — |
| NKX2-1 | 0.916 | 0.634 | — |
| NRIP1 | 0.902 | 0.000 | — |
| ONECUT1 | 0.888 | 0.292 | — |
| PGR | 0.887 | 0.045 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SEZ6L2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| EBI-4305885 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:21741601|imex:IM-15809 |
| AR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:23260764|imex:IM-18641 |
| SMAD3 | psi-mi:"MI:0728"(gal4 vp16 complementation) | imex:IM-26468|pubmed:18003659 |
| ENSMUSP00000041118.7 | psi-mi:"MI:0412"(electrophoretic mobility supershi | imex:IM-26468|pubmed:18003659 |
| NKX2-1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-26468|pubmed:18003659 |
| EBI-20597844 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-26468|pubmed:18003659 |
| PLOD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TFAP2C | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-22985|pubmed:24835590 |
| TFAP2A | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-22985|pubmed:24835590 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.7 + PDB: 7VOX, 8VFY, 8VFZ, 8VG1, 8VG2 | pLDDT=55.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Nucleoli fibrillar center | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. FOXA1 — Hepatocyte nuclear factor 3-alpha，研究基础较多，新颖性有限。
2. 蛋白大小472 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1052 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=55.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1052 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P55317
- Protein Atlas: https://www.proteinatlas.org/ENSG00000129514-FOXA1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FOXA1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P55317
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
