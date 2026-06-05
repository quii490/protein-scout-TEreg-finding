---
type: protein-evaluation
gene: "TFAP2C"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TFAP2C — REJECTED (研究热度过高 (PubMed strict=222，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TFAP2C |
| 蛋白名称 | Transcription factor AP-2 gamma |
| 蛋白大小 | 450 aa / 49.2 kDa |
| UniProt ID | Q92754 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 450 aa / 49.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=222 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004979, IPR013854, IPR008123; Pfam: PF03299 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 222 |
| PubMed broad count | 380 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Defining a TFAP2C-centered transcription factor network during murine peri-implantation.. *Developmental cell*. PMID: 38574734
2. Efficient derivation of embryonic stem cells and primordial germ cell-like cells in cattle.. *The Journal of reproduction and development*. PMID: 38355134
3. Single-cell multi-omics analysis of human testicular germ cell tumor reveals its molecular features and microenvironment.. *Nature communications*. PMID: 38123589
4. CRISPR screening identifies regulators of enhancer-mediated androgen receptor transcription in advanced prostate cancer.. *Cell reports*. PMID: 39954255
5. The transcription factor GABPA is a master regulator of naive pluripotency.. *Nature cell biology*. PMID: 39747581

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.3 |
| 高置信度残基 (pLDDT>90) 占比 | 35.1% |
| 置信残基 (pLDDT 70-90) 占比 | 12.4% |
| 中等置信 (pLDDT 50-70) 占比 | 7.3% |
| 低置信 (pLDDT<50) 占比 | 45.1% |
| 有序区域 (pLDDT>70) 占比 | 47.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=66.3），有序残基占 47.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004979, IPR013854, IPR008123; Pfam: PF03299 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WWOX | 0.989 | 0.292 | — |
| MYC | 0.960 | 0.459 | — |
| CITED2 | 0.945 | 0.482 | — |
| ESR1 | 0.938 | 0.562 | — |
| KCTD1 | 0.936 | 0.362 | — |
| TFAP2A | 0.931 | 0.292 | — |
| KDM5B | 0.914 | 0.292 | — |
| GATA3 | 0.858 | 0.229 | — |
| EGFR | 0.820 | 0.078 | — |
| CGB5 | 0.820 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| UBE2I | psi-mi:"MI:0018"(two hybrid) | pubmed:12072434|imex:IM-19634 |
| CITED2 | psi-mi:"MI:0047"(far western blotting) | pubmed:12586840|imex:IM-19636 |
| GPR22 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| IKBKB | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| NR1I2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CCNG1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| ZFAND4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| SHARPIN | psi-mi:"MI:0018"(two hybrid) | imex:IM-22985|pubmed:24835590 |
| RPL38 | psi-mi:"MI:0018"(two hybrid) | imex:IM-22985|pubmed:24835590 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.3 + PDB: 无 | pLDDT=66.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. TFAP2C — Transcription factor AP-2 gamma，研究基础较多，新颖性有限。
2. 蛋白大小450 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 222 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=66.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 222 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92754
- Protein Atlas: https://www.proteinatlas.org/ENSG00000087510-TFAP2C/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TFAP2C
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92754
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000087510-TFAP2C/subcellular

![](https://images.proteinatlas.org/55179/1081_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/55179/1081_D7_2_red_green.jpg)
![](https://images.proteinatlas.org/55179/875_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/55179/875_B6_4_red_green.jpg)
![](https://images.proteinatlas.org/55179/883_B6_2_red_green.jpg)
![](https://images.proteinatlas.org/55179/883_B6_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
