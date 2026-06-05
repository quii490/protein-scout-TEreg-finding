---
type: protein-evaluation
gene: "BCCIP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BCCIP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BCCIP / TOK1 |
| 蛋白名称 | BRCA2 and CDKN1A-interacting protein |
| 蛋白大小 | 314 aa / 36.0 kDa |
| UniProt ID | Q9P287 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Cytoplasm, cytoskeleton, microtubule organizing cen |
| 蛋白大小 | 10/10 | ×1 | 10 | 314 aa / 36.0 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=61 篇 (≤80→4) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=79.4; PDB: 7KYQ, 7KYS, 8EQB, 8EXE, 8EXF |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR025602; Pfam: PF13862 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Nucleus; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, centriole; Cytoplasm, c... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centriole (GO:0005814)
- centrosome (GO:0005813)
- cytosol (GO:0005829)
- mitotic spindle pole (GO:0097431)
- nuclear cyclin-dependent protein kinase holoenzyme complex (GO:0019908)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 61 |
| PubMed broad count | 72 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TOK1 |

**关键文献**:
1. Expression and Significance of BCCIP and Glutathione Peroxidase 4 in Clear Cell Renal Cell Carcinoma.. *Bulletin of experimental biology and medicine*. PMID: 38342812
2. Genomic structure of the human BCCIP gene and its expression in cancer.. *Gene*. PMID: 12527204
3. Overexpression of BCCIP predicts an unfavorable prognosis and promotes the proliferation and migration of lung adenocarcinoma.. *Thoracic cancer*. PMID: 34297484
4. The BRCA2 and CDKN1A-interacting protein (BCCIP) stabilizes stalled replication forks and prevents degradation of nascent DNA.. *FEBS letters*. PMID: 35592921
5. Differential BCCIP gene expression in primary human ovarian cancer, renal cell carcinoma and colorectal cancer tissues.. *International journal of oncology*. PMID: 24101097

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.4 |
| 高置信度残基 (pLDDT>90) 占比 | 58.3% |
| 置信残基 (pLDDT 70-90) 占比 | 10.5% |
| 中等置信 (pLDDT 50-70) 占比 | 13.1% |
| 低置信 (pLDDT<50) 占比 | 18.2% |
| 有序区域 (pLDDT>70) 占比 | 68.8% |
| 可用 PDB 条目 | 7KYQ, 7KYS, 8EQB, 8EXE, 8EXF |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（7KYQ, 7KYS, 8EQB, 8EXE, 8EXF）+ AlphaFold极高置信度预测（pLDDT=79.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR025602; Pfam: PF13862 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BRCA2 | 0.997 | 0.510 | — |
| CDKN1A | 0.990 | 0.628 | — |
| DHX32 | 0.963 | 0.000 | — |
| MTDH | 0.945 | 0.292 | — |
| UROS | 0.932 | 0.000 | — |
| RPL23 | 0.931 | 0.908 | — |
| CCNH | 0.921 | 0.000 | — |
| CDK7 | 0.917 | 0.000 | — |
| MNAT1 | 0.915 | 0.000 | — |
| CCNT1 | 0.910 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.4 + PDB: 7KYQ, 7KYS, 8EQB, 8EXE, 8EXF | pLDDT=79.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytoskeleton, microtubule orga / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. BCCIP — BRCA2 and CDKN1A-interacting protein，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小314 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 61 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P287
- Protein Atlas: https://www.proteinatlas.org/ENSG00000107949-BCCIP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BCCIP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P287
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000107949-BCCIP/subcellular

![](https://images.proteinatlas.org/38011/1443_E1_3_red_green.jpg)
![](https://images.proteinatlas.org/38011/1443_E1_4_red_green.jpg)
![](https://images.proteinatlas.org/38011/1564_C6_5_red_green.jpg)
![](https://images.proteinatlas.org/38011/1564_C6_6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9P287-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
