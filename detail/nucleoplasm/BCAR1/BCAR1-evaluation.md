---
type: protein-evaluation
gene: "BCAR1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BCAR1 — REJECTED (研究热度过高 (PubMed strict=117，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BCAR1 / CAS, CASS1, CRKAS |
| 蛋白名称 | Breast cancer anti-estrogen resistance protein 1 |
| 蛋白大小 | 870 aa / 93.4 kDa |
| UniProt ID | P56945 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane, Focal adhesion sites; 额外: Nucleoli, Nucleol; UniProt: Cell junction, focal adhesion; Cytoplasm; Cell projection, a |
| 蛋白大小 | 8/10 | ×1 | 8 | 870 aa / 93.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=117 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.7; PDB: 1WYX, 3T6G, 5O2M, 5O2P, 5O2Q |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR046976, IPR035745, IPR021901, IPR037362, IPR014 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **67.5/180** | |
| **归一化总分** | | | **37.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Focal adhesion sites; 额外: Nucleoli, Nucleoli fibrillar center, Cytosol | Supported |
| UniProt | Cell junction, focal adhesion; Cytoplasm; Cell projection, axon | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- axon (GO:0030424)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- focal adhesion (GO:0005925)
- lamellipodium (GO:0030027)
- membrane (GO:0016020)
- ruffle (GO:0001726)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 117 |
| PubMed broad count | 561 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CAS, CASS1, CRKAS |

**关键文献**:
1. Phosphorylation regulates cullin-based ubiquitination in tumorigenesis.. *Acta pharmaceutica Sinica. B*. PMID: 33643814
2. p130Cas/BCAR1 and p140Cap/SRCIN1 Adaptors: The Yin Yang in Breast Cancer?. *Frontiers in cell and developmental biology*. PMID: 34708040
3. p130Cas/BCAR1 scaffold protein in tissue homeostasis and pathogenesis.. *Gene*. PMID: 25727852
4. The role of p130Cas/BCAR1 adaptor protein in the pathogenesis of cardiovascular diseases: A literature review.. *American heart journal plus : cardiology research and practice*. PMID: 39036012
5. Integrative functional genomics analysis identifies pleiotropic genes for vascular diseases.. *Nature communications*. PMID: 41644529

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.7 |
| 高置信度残基 (pLDDT>90) 占比 | 27.7% |
| 置信残基 (pLDDT 70-90) 占比 | 12.6% |
| 中等置信 (pLDDT 50-70) 占比 | 8.3% |
| 低置信 (pLDDT<50) 占比 | 51.4% |
| 有序区域 (pLDDT>70) 占比 | 40.3% |
| 可用 PDB 条目 | 1WYX, 3T6G, 5O2M, 5O2P, 5O2Q |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.7），有序残基占 40.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR046976, IPR035745, IPR021901, IPR037362, IPR014928; Pfam: PF12026, PF08824, PF00018 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PXN | 0.999 | 0.717 | — |
| VCL | 0.999 | 0.696 | — |
| SRC | 0.999 | 0.884 | — |
| PTK2 | 0.999 | 0.880 | — |
| CRKL | 0.999 | 0.749 | — |
| CRK | 0.999 | 0.928 | — |
| DOCK1 | 0.999 | 0.292 | — |
| PTK2B | 0.998 | 0.736 | — |
| TLN1 | 0.998 | 0.048 | — |
| RAPGEF1 | 0.997 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Stat2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| EGFR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:15657067 |
| Ptk2 | psi-mi:"MI:0018"(two hybrid) | pubmed:7479864|imex:IM-16912|m |
| HSPA5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| FXYD6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PPP1R15A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| TUBA4A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| VPS11 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| E2F2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| EFS | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.7 + PDB: 1WYX, 3T6G, 5O2M, 5O2P, 5O2Q | pLDDT=61.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell junction, focal adhesion; Cytoplasm; Cell pro / Plasma membrane, Focal adhesion sites; 额外: Nucleol | 一致 |
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
1. BCAR1 — Breast cancer anti-estrogen resistance protein 1，研究基础较多，新颖性有限。
2. 蛋白大小870 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 117 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=61.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 117 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P56945
- Protein Atlas: https://www.proteinatlas.org/ENSG00000050820-BCAR1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BCAR1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P56945
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000050820-BCAR1/subcellular

![](https://images.proteinatlas.org/42282/754_A12_1_red_green.jpg)
![](https://images.proteinatlas.org/42282/754_A12_2_red_green.jpg)
![](https://images.proteinatlas.org/42282/758_A12_1_red_green.jpg)
![](https://images.proteinatlas.org/42282/758_A12_2_red_green.jpg)
![](https://images.proteinatlas.org/42282/813_A12_1_red_green.jpg)
![](https://images.proteinatlas.org/42282/813_A12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P56945-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
