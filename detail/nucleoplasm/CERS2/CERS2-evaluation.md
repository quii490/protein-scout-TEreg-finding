---
type: protein-evaluation
gene: "CERS2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CERS2 — REJECTED (研究热度过高 (PubMed strict=106，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CERS2 / LASS2, TMSG1 |
| 蛋白名称 | Ceramide synthase 2 |
| 蛋白大小 | 380 aa / 44.9 kDa |
| UniProt ID | Q96G23 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear membrane, Endoplasmic reticulum; UniProt: Endoplasmic reticulum membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 380 aa / 44.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=106 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=86.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001356, IPR009057, IPR016439, IPR006634; Pfam:  |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **73.0/180** | |
| **归一化总分** | | | **40.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane, Endoplasmic reticulum | Supported |
| UniProt | Endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasmic side of endoplasmic reticulum membrane (GO:0098554)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 106 |
| PubMed broad count | 255 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LASS2, TMSG1 |

**关键文献**:
1. IL-10 constrains sphingolipid metabolism to limit inflammation.. *Nature*. PMID: 38383790
2. Disruption of adipocyte HIF-1α improves atherosclerosis through the inhibition of ceramide generation.. *Acta pharmaceutica Sinica. B*. PMID: 35847503
3. EMP1 safeguards hematopoietic stem cells by suppressing sphingolipid metabolism and alleviating endoplasmic reticulum stress.. *Nature communications*. PMID: 40624017
4. Reduced circulating sphingolipids and CERS2 activity are linked to T2D risk and impaired insulin secretion.. *Science advances*. PMID: 39792658
5. Long-chain ceramides are cell non-autonomous signals linking lipotoxicity to endoplasmic reticulum stress in skeletal muscle.. *Nature communications*. PMID: 35365625

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.6 |
| 高置信度残基 (pLDDT>90) 占比 | 68.2% |
| 置信残基 (pLDDT 70-90) 占比 | 19.5% |
| 中等置信 (pLDDT 50-70) 占比 | 3.4% |
| 低置信 (pLDDT<50) 占比 | 8.9% |
| 有序区域 (pLDDT>70) 占比 | 87.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=86.6，有序区 87.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR009057, IPR016439, IPR006634; Pfam: PF00046, PF03798 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ASGR1 | psi-mi:"MI:0018"(two hybrid) | pubmed:11543633|imex:IM-19013 |
| ASGR2 | psi-mi:"MI:0018"(two hybrid) | pubmed:11543633|imex:IM-19013 |
| SLC22A1 | psi-mi:"MI:0018"(two hybrid) | pubmed:11543633|imex:IM-19013 |
| ATP6V0C | psi-mi:"MI:0018"(two hybrid) | pubmed:11543633|imex:IM-19013 |
| NDN | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| 7242199 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| RAB5IF | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SLC19A2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| SLC39A1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| PEX6 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.6 + PDB: 无 | pLDDT=86.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane / Nuclear membrane, Endoplasmic reticulum | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CERS2 — Ceramide synthase 2，研究基础较多，新颖性有限。
2. 蛋白大小380 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 106 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 106 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96G23
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143418-CERS2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CERS2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96G23
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96G23-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
