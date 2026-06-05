---
type: protein-evaluation
gene: "TBX1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TBX1 — REJECTED (研究热度过高 (PubMed strict=546，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TBX1 |
| 蛋白名称 | T-box transcription factor TBX1 |
| 蛋白大小 | 398 aa / 43.1 kDa |
| UniProt ID | O43435 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies, Cytoplasmic bodies; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 398 aa / 43.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=546 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.2; PDB: 4A04 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008967, IPR046360, IPR036960, IPR001699, IPR018 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies, Cytoplasmic bodies | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 546 |
| PubMed broad count | 818 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Hypoparathyroidism and Pseudohypoparathyroidism.. **. PMID: 25905388
2. Lymphatic endothelial transcription factor Tbx1 promotes an immunosuppressive microenvironment to facilitate post-myocardial infarction repair.. *Immunity*. PMID: 37625409
3. Velo-cardio-facial syndrome.. *Current opinion in pediatrics*. PMID: 16282778
4. Cardiac Transcription Factors and Regulatory Networks.. *Advances in experimental medicine and biology*. PMID: 38884718
5. Tbx1: Transcriptional and Developmental Functions.. *Current topics in developmental biology*. PMID: 28057265

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.2 |
| 高置信度残基 (pLDDT>90) 占比 | 42.5% |
| 置信残基 (pLDDT 70-90) 占比 | 8.0% |
| 中等置信 (pLDDT 50-70) 占比 | 7.0% |
| 低置信 (pLDDT<50) 占比 | 42.5% |
| 有序区域 (pLDDT>70) 占比 | 50.5% |
| 可用 PDB 条目 | 4A04 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.2），有序残基占 50.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008967, IPR046360, IPR036960, IPR001699, IPR018186; Pfam: PF00907 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GNB1L | 0.889 | 0.000 | — |
| CRKL | 0.812 | 0.000 | — |
| TMEM26 | 0.785 | 0.000 | — |
| NKX2-5 | 0.779 | 0.114 | — |
| SEPTIN5 | 0.756 | 0.000 | — |
| GSC2 | 0.751 | 0.126 | — |
| LOC102724788 | 0.724 | 0.000 | — |
| ISL1 | 0.715 | 0.126 | — |
| DGCR6L | 0.709 | 0.000 | — |
| DGCR6 | 0.707 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Nfatc2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Litaf | psi-mi:"MI:0400"(affinity technology) | imex:IM-17722|pubmed:11042109| |
| Nedd4 | psi-mi:"MI:0047"(far western blotting) | imex:IM-17722|pubmed:11042109| |
| TLE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RIPPLY3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:30241482|imex:IM-27129 |
| PIPSL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ENST00000332710 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 7
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.2 + PDB: 4A04 | pLDDT=68.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nuclear bodies, Cytoplasmic bodies | 一致 |
| PPI | STRING + IntAct | 15 + 7 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. TBX1 — T-box transcription factor TBX1，研究基础较多，新颖性有限。
2. 蛋白大小398 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 546 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=68.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 546 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43435
- Protein Atlas: https://www.proteinatlas.org/ENSG00000184058-TBX1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TBX1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43435
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (approved)。来源: https://www.proteinatlas.org/ENSG00000184058-TBX1/subcellular

![](https://images.proteinatlas.org/29330/1466_C5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29330/1466_C5_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/29330/1747_E2_19_cr58062ee0c50d7_blue_red_green.jpg)
![](https://images.proteinatlas.org/29330/1747_E2_4_cr58062ec6131fa_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O43435-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
