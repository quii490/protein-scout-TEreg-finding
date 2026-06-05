---
type: protein-evaluation
gene: "CERKL"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, E-batch]
status: scored
---

## CERKL 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CERKL / — |
| 蛋白名称 | Ceramide kinase-like protein |
| 蛋白大小 | 558 aa / 62.6 kDa |
| UniProt ID | Q49MI3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 6/10 | ×4 | 24 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Nucleus, nucleolus; Cytoplasm; Nucleus, nucleolus; Go |
| 蛋白大小 | 10/10 | ×1 | 10 | 558 aa / 62.6 kDa |
| 研究新颖性 | 7/10 | ×5 | 35 | PubMed strict=66 篇 |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=79.7; PDB: 暂无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR017438, IPR045363, IPR057465, IPR001206, IPR050187, IPR016064; Pfam: PF19280, PF00781, PF25382 |
| PPI 网络 | 9/10 | ×3 | 27 | STRING 15 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 1.5 | AlphaFold 结构预测: +0.25 |
| **原始总分** | | | **132.5/180** | |
| **归一化总分 (÷1.83)** | | | **72.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Cytoplasm | —
| UniProt | Nucleus, nucleolus | —
| UniProt | Cytoplasm | —
| UniProt | Nucleus, nucleolus | —
| UniProt | Golgi apparatus, trans-Golgi network | —
| UniProt | Endoplasmic reticulum | —

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- cytoplasm (GO:0005737) [IDA:UniProtKB]
- cytosol (GO:0005829) [IDA:HPA]
- endoplasmic reticulum (GO:0005783) [IDA:UniProtKB]
- Golgi apparatus (GO:0005794) [IDA:UniProtKB]
- membrane (GO:0016020) [IEA:GOC]
- nucleolus (GO:0005730) [IDA:UniProtKB]
- nucleoplasm (GO:0005654) [IDA:HPA]
- perinuclear region of cytoplasm (GO:0048471) [IEA:Ensembl]

**结论**: HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Nucleus, nucleolus; Cytoplasm; Nucleus, nucleolus; Golgi apparatus, trans-Golgi network; Endoplasmic reticulum

#### 3.2 蛋白大小评估

**评价**: 558 aa / 62.6 kDa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 66 |
| PubMed 搜索链接 | [CERKL PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=CERKL) |

**关键文献**:
暂无文献记录。

**评价**: 有一定研究基础。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.7 |
| 高置信度残基 (pLDDT>90) 占比 | 57.3% |
| 置信残基 (pLDDT 70-90) 占比 | 16.8% |
| 中等置信 (pLDDT 50-70) 占比 | 6.8% |
| 低置信 (pLDDT<50) 占比 | 19.0% |
| 有序区域 (pLDDT>70) 占比 | 74.1% |
| 可用 PDB 条目 | 暂无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量中等。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017438, IPR045363, IPR057465, IPR001206, IPR050187, IPR016064; Pfam: PF19280, PF00781, PF25382 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EYS | 0.857 | 0.000 | — |
| TULP1 | 0.835 | 0.000 | — |
| RDH12 | 0.828 | 0.000 | — |
| CNGB1 | 0.825 | 0.000 | — |
| PDE6A | 0.825 | 0.000 | — |
| ABCA4 | 0.822 | 0.000 | — |
| PCARE | 0.805 | 0.000 | — |
| CNGA1 | 0.800 | 0.000 | — |
| PRCD | 0.800 | 0.000 | — |
| PRPF31 | 0.792 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| PPM1G | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| PPM1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| EIF3G | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| PPM1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| EIF3I | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| MICAL3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| ANKHD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| SIRT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| ERBIN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |

**PPI 互证分析**:
STRING 15 个预测互作，IntAct 11 个实验互作。调控相关配体占比 1/15。

**评价**: STRING + IntAct 双源 PPI 数据充分。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold | pLDDT=79.7, v6 | 预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus, nucleolus; Cytoplasm; Nucleus, nucleolus; Golgi apparatus, trans-Golgi network; Endoplasmic reticulum / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 11 interactions | 数据充分 |

**互证加分明细**:
- AlphaFold 结构预测: +0.25
- 多库定位一致 (HPA+UniProt): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5

**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐

**归一化总分**: 72.4/100

**核心优势**:
1. CERKL — Ceramide kinase-like protein，较新颖，PubMed 66 篇。
2. 蛋白大小558 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. 功能研究较少，具体调控机制待阐明

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q49MI3
- Protein Atlas: https://www.proteinatlas.org/search/CERKL
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CERKL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q49MI3
- STRING: https://string-db.org/network/9606.CERKL
- Packet data timestamp: 2026-06-03 04:50:59

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000188452-CERKL/subcellular

![](https://images.proteinatlas.org/35443/1150_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/35443/1150_D12_3_red_green.jpg)
![](https://images.proteinatlas.org/35443/1527_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/35443/1527_F10_2_red_green.jpg)
![](https://images.proteinatlas.org/43203/1057_E4_1_red_green.jpg)
![](https://images.proteinatlas.org/43203/1057_E4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q49MI3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
