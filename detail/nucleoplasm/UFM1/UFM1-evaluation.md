---
type: protein-evaluation
gene: "UFM1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## UFM1 — REJECTED (研究热度过高 (PubMed strict=212，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | UFM1 / C13orf20 |
| 蛋白名称 | Ubiquitin-fold modifier 1 |
| 蛋白大小 | 85 aa / 9.1 kDa |
| UniProt ID | P61960 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 5/10 | ×1 | 5 | 85 aa / 9.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=212 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=91.6; PDB: 1WXS, 5HKH, 5IA7, 5IA8, 5IAA, 5L95, 6H77 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR029071, IPR005375; Pfam: PF03671 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **91.0/180** | |
| **归一化总分** | | | **50.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- endoplasmic reticulum (GO:0005783)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 212 |
| PubMed broad count | 298 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C13orf20 |

**关键文献**:
1. UFMylation: a ubiquitin-like modification.. *Trends in biochemical sciences*. PMID: 37945409
2. Reticulophagy and viral infection.. *Autophagy*. PMID: 39394962
3. Metformin induces Ferroptosis by inhibiting UFMylation of SLC7A11 in breast cancer.. *Journal of experimental & clinical cancer research : CR*. PMID: 34162423
4. VCP/p97 UFMylation stabilizes BECN1 and facilitates the initiation of autophagy.. *Autophagy*. PMID: 38762759
5. The UFM1 system regulates ER-phagy through the ufmylation of CYB5R3.. *Nature communications*. PMID: 36543799

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.6 |
| 高置信度残基 (pLDDT>90) 占比 | 88.2% |
| 置信残基 (pLDDT 70-90) 占比 | 3.5% |
| 中等置信 (pLDDT 50-70) 占比 | 5.9% |
| 低置信 (pLDDT<50) 占比 | 2.4% |
| 有序区域 (pLDDT>70) 占比 | 91.7% |
| 可用 PDB 条目 | 1WXS, 5HKH, 5IA7, 5IA8, 5IAA, 5L95, 6H77, 7W3N, 8BZR, 8OHD |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1WXS, 5HKH, 5IA7, 5IA8, 5IAA, 5L95, 6H77, 7W3N, 8BZR, 8OHD）+ AlphaFold极高置信度预测（pLDDT=91.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029071, IPR005375; Pfam: PF03671 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UBA5 | 0.999 | 0.986 | — |
| UFC1 | 0.998 | 0.830 | — |
| UFSP2 | 0.998 | 0.904 | — |
| UFSP1 | 0.997 | 0.823 | — |
| UFL1 | 0.975 | 0.492 | — |
| DDRGK1 | 0.972 | 0.305 | — |
| URM1 | 0.803 | 0.000 | — |
| UBE2M | 0.802 | 0.000 | — |
| NEDD8 | 0.791 | 0.000 | — |
| GABARAPL2 | 0.781 | 0.087 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Ufl1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| ttm50 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| swa | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Ddrgk1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| PRKAB1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CDK5RAP3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| UBA5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| EBI-6095589 | psi-mi:"MI:0096"(pull down) | pubmed:21712045|imex:IM-17900 |
| DLD | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| KCTD21 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.6 + PDB: 1WXS, 5HKH, 5IA7, 5IA8, 5IAA,  | pLDDT=91.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. UFM1 — Ubiquitin-fold modifier 1，研究基础较多，新颖性有限。
2. 蛋白大小85 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 212 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 212 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P61960
- Protein Atlas: https://www.proteinatlas.org/ENSG00000120686-UFM1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=UFM1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P61960
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03



<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P61960-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
