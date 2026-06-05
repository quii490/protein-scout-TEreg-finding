---
type: protein-evaluation
gene: "FLII"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FLII — REJECTED (研究热度过高 (PubMed strict=220，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FLII / FLIL |
| 蛋白名称 | Protein flightless-1 homolog |
| 蛋白大小 | 1269 aa / 144.8 kDa |
| UniProt ID | Q13045 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Centriolar satellite, Cytosol; UniProt: Nucleus; Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton, m |
| 蛋白大小 | 5/10 | ×1 | 5 | 1269 aa / 144.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=220 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=80.9; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR029006, IPR007123, IPR001611, IPR003591, IPR032 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Centriolar satellite, Cytosol | Approved |
| UniProt | Nucleus; Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- brush border (GO:0005903)
- centriolar satellite (GO:0034451)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- focal adhesion (GO:0005925)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 220 |
| PubMed broad count | 365 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FLIL |

**关键文献**:
1. A ZFYVE21-Rubicon-RNF34 signaling complex promotes endosome-associated inflammasome activity in endothelial cells.. *Nature communications*. PMID: 37225719
2. A human FLII gene variant alters sarcomeric actin thin filament length and predisposes to cardiomyopathy.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 37126682
3. Interaction between FliI ATPase and a flagellar chaperone FliT during bacterial flagellar protein export.. *Molecular microbiology*. PMID: 22111876
4. NIBAN2/FLII/RREB1 Axis Drives Glioma Stem Cell Malignancy via TLR3 Pathway Activation.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 41736673
5. Polymorphisms of FLII implicate gene expressions and growth traits in Chinese cattle.. *Molecular and cellular probes*. PMID: 27453522

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.9 |
| 高置信度残基 (pLDDT>90) 占比 | 39.6% |
| 置信残基 (pLDDT 70-90) 占比 | 41.2% |
| 中等置信 (pLDDT 50-70) 占比 | 6.1% |
| 低置信 (pLDDT<50) 占比 | 13.2% |
| 有序区域 (pLDDT>70) 占比 | 80.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=80.9，有序区 80.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029006, IPR007123, IPR001611, IPR003591, IPR032675; Pfam: PF00626, PF00560, PF23598 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LRRFIP1 | 0.998 | 0.901 | — |
| LRRFIP2 | 0.989 | 0.831 | — |
| EWSR1 | 0.897 | 0.000 | — |
| LLGL1 | 0.838 | 0.045 | — |
| MYD88 | 0.814 | 0.354 | — |
| ACTL6A | 0.792 | 0.537 | — |
| DHX9 | 0.772 | 0.201 | — |
| GCFC2 | 0.763 | 0.000 | — |
| ESR1 | 0.743 | 0.522 | — |
| MYH9 | 0.701 | 0.190 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| P78073 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-2994|pubmed:19834901 |
| P94822 | psi-mi:"MI:0027"(cosedimentation) | imex:IM-14496|pubmed:16260786 |
| GRB2 | psi-mi:"MI:0096"(pull down) | pubmed:12577067|mint:MINT-5216 |
| DLST | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| lyx | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |
| yecJ | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |
| bluR | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |
| envZ | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |
| rplB | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |
| groEL | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.9 + PDB: 无 | pLDDT=80.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytoskeleton; Cytoplasm, cytos / Nucleoplasm, Centriolar satellite, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. FLII — Protein flightless-1 homolog，研究基础较多，新颖性有限。
2. 蛋白大小1269 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 220 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 220 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13045
- Protein Atlas: https://www.proteinatlas.org/ENSG00000177731-FLII/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FLII
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13045
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/FLII/IF_images/HPA007084_U2OS_1.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/FLII/IF_images/HPA007084_U2OS_2.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000177731-FLII/subcellular

![](https://images.proteinatlas.org/7084/2268_D12_163_red_green.jpg)
![](https://images.proteinatlas.org/7084/2268_D12_89_red_green.jpg)
![](https://images.proteinatlas.org/7084/71_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/7084/71_D11_2_red_green.jpg)
![](https://images.proteinatlas.org/7084/72_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/7084/72_D11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13045-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
