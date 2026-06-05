---
type: protein-evaluation
gene: "BNIP3L"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BNIP3L — REJECTED (研究热度过高 (PubMed strict=359，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BNIP3L / BNIP3A, BNIP3H, NIX |
| 蛋白名称 | BCL2/adenovirus E1B 19 kDa protein-interacting protein 3-like |
| 蛋白大小 | 219 aa / 23.9 kDa |
| UniProt ID | O60238 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Mitochondria; 额外: Nuclear speckles; UniProt: Nucleus envelope; Endoplasmic reticulum; Mitochondrion outer |
| 蛋白大小 | 10/10 | ×1 | 10 | 219 aa / 23.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=359 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR010548; Pfam: PF06553 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Nuclear speckles | Supported |
| UniProt | Nucleus envelope; Endoplasmic reticulum; Mitochondrion outer membrane; Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- membrane (GO:0016020)
- mitochondrial outer membrane (GO:0005741)
- mitochondrion (GO:0005739)
- nuclear envelope (GO:0005635)
- nuclear speck (GO:0016607)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 359 |
| PubMed broad count | 572 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BNIP3A, BNIP3H, NIX |

**关键文献**:
1. Mitochondria ROS and mitophagy in acute kidney injury.. *Autophagy*. PMID: 35678504
2. Autophagy in age-related macular degeneration.. *Autophagy*. PMID: 35468037
3. Mitophagy in tumorigenesis and metastasis.. *Cellular and molecular life sciences : CMLS*. PMID: 33580835
4. ROS-mediated lysosomal membrane permeabilization and autophagy inhibition regulate bleomycin-induced cellular senescence.. *Autophagy*. PMID: 38762757
5. BNIP3L/NIX degradation leads to mitophagy deficiency in ischemic brains.. *Autophagy*. PMID: 32722981

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.4 |
| 高置信度残基 (pLDDT>90) 占比 | 8.2% |
| 置信残基 (pLDDT 70-90) 占比 | 16.9% |
| 中等置信 (pLDDT 50-70) 占比 | 42.9% |
| 低置信 (pLDDT<50) 占比 | 32.0% |
| 有序区域 (pLDDT>70) 占比 | 25.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.4），有序残基占 25.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR010548; Pfam: PF06553 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GABARAP | 0.999 | 0.292 | — |
| GABARAPL2 | 0.999 | 0.329 | — |
| GABARAPL1 | 0.999 | 0.329 | — |
| BCL2 | 0.995 | 0.515 | — |
| STEAP3 | 0.983 | 0.292 | — |
| RHEB | 0.973 | 0.233 | — |
| BNIP3 | 0.967 | 0.891 | — |
| FUNDC1 | 0.966 | 0.000 | — |
| BCL2L1 | 0.951 | 0.294 | — |
| MAP1A | 0.940 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-28977676 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TMEM11 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| EWSR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| BNIP3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| DOK5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RINT1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ECM1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| DUSP3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CAMK1D | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CASK | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.4 + PDB: 无 | pLDDT=60.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus envelope; Endoplasmic reticulum; Mitochond / Mitochondria; 额外: Nuclear speckles | 一致 |
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
1. BNIP3L — BCL2/adenovirus E1B 19 kDa protein-interacting protein 3-like，研究基础较多，新颖性有限。
2. 蛋白大小219 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 359 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=60.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 359 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60238
- Protein Atlas: https://www.proteinatlas.org/ENSG00000104765-BNIP3L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BNIP3L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60238
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (enhanced)。来源: https://www.proteinatlas.org/ENSG00000104765-BNIP3L/subcellular

![](https://images.proteinatlas.org/15652/152_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/15652/152_B3_2_red_green.jpg)
![](https://images.proteinatlas.org/15652/154_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/15652/154_B3_2_red_green.jpg)
![](https://images.proteinatlas.org/15652/198_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/15652/198_B3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O60238-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
