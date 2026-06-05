---
type: protein-evaluation
gene: "ASPA"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ASPA — REJECTED (研究热度过高 (PubMed strict=304，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ASPA / ACY2, ASP |
| 蛋白名称 | Aspartoacylase |
| 蛋白大小 | 313 aa / 35.7 kDa |
| UniProt ID | P45381 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 313 aa / 35.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=304 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=96.1; PDB: 2I3C, 2O4H, 2O53, 2Q51, 4MRI, 4MXU, 4NFR |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR050178, IPR016708, IPR055438, IPR007036; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **95.5/180** | |
| **归一化总分** | | | **53.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 304 |
| PubMed broad count | 863 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ACY2, ASP |

**关键文献**:
1. Allogeneic hematopoietic stem cell transplantation for NK/T-cell lymphoma: an international collaborative analysis.. *Leukemia*. PMID: 37157017
2. Development and application of a quadruplex TaqMan real-time fluorescence quantitative PCR assay for four porcine digestive pathogens.. *Frontiers in cellular and infection microbiology*. PMID: 39660284
3. The Purification of Human Carboxypeptidase O.. *Studies in health technology and informatics*. PMID: 38007733
4. Identification and Confirmation of Shared Etiology and Hub Biomarkers in Nonalcoholic Steatohepatitis and Crohn's Disease.. *Digestive diseases and sciences*. PMID: 40591229
5. Nur7 is a nonsense mutation in the mouse aspartoacylase gene that causes spongy degeneration of the CNS.. *The Journal of neuroscience : the official journal of the Society for Neuroscience*. PMID: 18987190

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.1 |
| 高置信度残基 (pLDDT>90) 占比 | 94.2% |
| 置信残基 (pLDDT 70-90) 占比 | 3.5% |
| 中等置信 (pLDDT 50-70) 占比 | 1.6% |
| 低置信 (pLDDT<50) 占比 | 0.6% |
| 有序区域 (pLDDT>70) 占比 | 97.7% |
| 可用 PDB 条目 | 2I3C, 2O4H, 2O53, 2Q51, 4MRI, 4MXU, 4NFR, 4TNU |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2I3C, 2O4H, 2O53, 2Q51, 4MRI, 4MXU, 4NFR, 4TNU）+ AlphaFold极高置信度预测（pLDDT=96.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050178, IPR016708, IPR055438, IPR007036; Pfam: PF24827, PF04952 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ACY1 | 0.981 | 0.000 | — |
| NAT8L | 0.977 | 0.000 | — |
| FOLH1 | 0.934 | 0.000 | — |
| RIMKLB | 0.918 | 0.000 | — |
| ASS1 | 0.916 | 0.000 | — |
| GOT1 | 0.915 | 0.000 | — |
| ASNS | 0.908 | 0.000 | — |
| ASRGL1 | 0.905 | 0.000 | — |
| RIMKLA | 0.904 | 0.000 | — |
| GOT2 | 0.902 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=96.1 + PDB: 2I3C, 2O4H, 2O53, 2Q51, 4MRI,  | pLDDT=96.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. ASPA — Aspartoacylase，研究基础较多，新颖性有限。
2. 蛋白大小313 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 304 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 304 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P45381
- Protein Atlas: https://www.proteinatlas.org/ENSG00000108381-ASPA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ASPA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P45381
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000108381-ASPA/subcellular

![](https://images.proteinatlas.org/22145/187_A10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/22145/187_A10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/22145/188_A10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/22145/188_A10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/22145/2047_A2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/22145/2047_A2_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P45381-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
