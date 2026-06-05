---
type: protein-evaluation
gene: "CSTA"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CSTA — REJECTED (研究热度过高 (PubMed strict=128，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CSTA / STF1, STFA |
| 蛋白名称 | Cystatin-A |
| 蛋白大小 | 98 aa / 11.0 kDa |
| UniProt ID | P01040 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 5/10 | ×1 | 5 | 98 aa / 11.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=128 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=93.2; PDB: 1CYU, 1CYV, 1DVC, 1DVD, 1GD3, 1GD4, 1N9J |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000010, IPR046350, IPR018073, IPR001713; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **91.0/180** | |
| **归一化总分** | | | **50.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cornified envelope (GO:0001533)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular space (GO:0005615)
- nucleoplasm (GO:0005654)
- peptidase inhibitor complex (GO:1904090)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 128 |
| PubMed broad count | 336 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: STF1, STFA |

**关键文献**:
1. Extracellular vesicles from obese visceral adipose promote pancreatic cancer development and resistance to immune checkpoint blockade therapy.. *Cell metabolism*. PMID: 41338178
2. CSTA plays a role in osteoclast formation and bone resorption by mediating the DAP12/TREM2 pathway.. *Biochemical and biophysical research communications*. PMID: 36007331
3. M2-like GAMs secreting CSTA drive glioblastoma progression via the ITGB4-TGFB1 feedback axis.. *Journal of translational medicine*. PMID: 41832564
4. Conformational analysis and chemical reactivity of the multidomain sulfurtransferase, Staphylococcus aureus CstA.. *Biochemistry*. PMID: 25793461
5. Peptide Transporter CstA Imports Pyruvate in Escherichia coli K-12.. *Journal of bacteriology*. PMID: 29358499

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.2 |
| 高置信度残基 (pLDDT>90) 占比 | 82.7% |
| 置信残基 (pLDDT 70-90) 占比 | 14.3% |
| 中等置信 (pLDDT 50-70) 占比 | 3.1% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 97.0% |
| 可用 PDB 条目 | 1CYU, 1CYV, 1DVC, 1DVD, 1GD3, 1GD4, 1N9J, 1NB3, 1NB5, 3K9M |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1CYU, 1CYV, 1DVC, 1DVD, 1GD3, 1GD4, 1N9J, 1NB3, 1NB5, 3K9M）+ AlphaFold极高置信度预测（pLDDT=93.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000010, IPR046350, IPR018073, IPR001713; Pfam: PF00031 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CTSB | 0.998 | 0.981 | — |
| CTSL | 0.992 | 0.967 | — |
| CTSH | 0.964 | 0.659 | — |
| CTSV | 0.960 | 0.919 | — |
| SLC12A8 | 0.958 | 0.045 | — |
| CTSS | 0.921 | 0.044 | — |
| TGM1 | 0.888 | 0.000 | — |
| COL6A5 | 0.884 | 0.046 | — |
| DSP | 0.785 | 0.436 | — |
| LOR | 0.780 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| VAPA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| trxA | psi-mi:"MI:0397"(two hybrid array) | pubmed:17615063 |
| ctsR | psi-mi:"MI:0018"(two hybrid) | pubmed:21630458|imex:IM-16574 |
| btsT | psi-mi:"MI:0276"(blue native page) | pubmed:16858726|imex:IM-18898 |
| aroC | psi-mi:"MI:0397"(two hybrid array) | pubmed:17615063 |
| EBI-528082 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-22256|pubmed:24627523 |
| MINT-159567 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-22256|pubmed:24627523 |
| PTN | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| EBI-1257125 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:19463016|imex:IM-17246 |
| GABARAPL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.2 + PDB: 1CYU, 1CYV, 1DVC, 1DVD, 1GD3,  | pLDDT=93.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CSTA — Cystatin-A，研究基础较多，新颖性有限。
2. 蛋白大小98 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 128 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 128 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P01040
- Protein Atlas: https://www.proteinatlas.org/ENSG00000121552-CSTA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CSTA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P01040
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000121552-CSTA/subcellular

![](https://images.proteinatlas.org/1031/1790_F2_5_red_green.jpg)
![](https://images.proteinatlas.org/1031/1790_F2_6_red_green.jpg)
![](https://images.proteinatlas.org/1031/26_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/1031/26_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/1031/27_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/1031/27_F2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P01040-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
