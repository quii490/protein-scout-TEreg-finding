---
type: protein-evaluation
gene: "STAT1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## STAT1 — REJECTED (研究热度过高 (PubMed strict=8074，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | STAT1 |
| 蛋白名称 | Signal transducer and activator of transcription 1-alpha/beta |
| 蛋白大小 | 750 aa / 87.3 kDa |
| UniProt ID | P42224 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 750 aa / 87.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=8074 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=87.2; PDB: 1BF5, 1YVL, 2KA6, 3WWT, 7NUF, 8D3F, 8YYU |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR008967, IPR000980, IPR036860, IPR001217, IPR038 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Enhanced |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- axon (GO:0030424)
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- dendrite (GO:0030425)
- ISGF3 complex (GO:0070721)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8074 |
| PubMed broad count | 14592 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Pyruvate is a natural suppressor of interferon signaling by inducing STAT1 protein pyruvylation.. *Cell*. PMID: 41763198
2. Cardiomyocyte-derived USP13 protects hearts from hypertrophy via deubiquitinating and stabilizing STAT1 in male mice.. *Nature communications*. PMID: 40593642
3. β-hydroxybutyrylation and O-GlcNAc modifications of STAT1 modulate antiviral defense in aging.. *Cellular & molecular immunology*. PMID: 39979583
4. Association of STAT1 gene with milk fat and protein yield in Holstein Friesian crossbred cattle maintained in the sub-tropical climate of India.. *The Journal of dairy research*. PMID: 39439094
5. STAT1 and Its Crucial Role in the Control of Viral Infections.. *International journal of molecular sciences*. PMID: 35456913

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.2 |
| 高置信度残基 (pLDDT>90) 占比 | 70.0% |
| 置信残基 (pLDDT 70-90) 占比 | 17.1% |
| 中等置信 (pLDDT 50-70) 占比 | 6.4% |
| 低置信 (pLDDT<50) 占比 | 6.5% |
| 有序区域 (pLDDT>70) 占比 | 87.1% |
| 可用 PDB 条目 | 1BF5, 1YVL, 2KA6, 3WWT, 7NUF, 8D3F, 8YYU, 8YYV |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1BF5, 1YVL, 2KA6, 3WWT, 7NUF, 8D3F, 8YYU, 8YYV）+ AlphaFold极高置信度预测（pLDDT=87.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008967, IPR000980, IPR036860, IPR001217, IPR038295; Pfam: PF00017, PF12162, PF01017 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| IRF1 | 0.999 | 0.805 | — |
| IFNGR1 | 0.999 | 0.837 | — |
| PIAS1 | 0.999 | 0.853 | — |
| CREBBP | 0.999 | 0.983 | — |
| JAK1 | 0.999 | 0.875 | — |
| STAT2 | 0.999 | 0.886 | — |
| JAK2 | 0.999 | 0.838 | — |
| IRF9 | 0.999 | 0.770 | — |
| KPNA1 | 0.999 | 0.669 | — |
| STAT3 | 0.999 | 0.874 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PIBF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32838362|imex:IM-27901| |
| P | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:20089657|imex:IM-28090 |
| Q82983 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:15242592|imex:IM-28164 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.2 + PDB: 1BF5, 1YVL, 2KA6, 3WWT, 7NUF,  | pLDDT=87.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

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
1. STAT1 — Signal transducer and activator of transcription 1-alpha/beta，研究基础较多，新颖性有限。
2. 蛋白大小750 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8074 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 8074 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P42224
- Protein Atlas: https://www.proteinatlas.org/ENSG00000115415-STAT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STAT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P42224
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000115415-STAT1/subcellular

![](https://images.proteinatlas.org/931/26_D6_1_red_green.jpg)
![](https://images.proteinatlas.org/931/26_D6_2_red_green.jpg)
![](https://images.proteinatlas.org/931/27_D6_1_red_green.jpg)
![](https://images.proteinatlas.org/931/27_D6_2_red_green.jpg)
![](https://images.proteinatlas.org/931/28_D6_1_red_green.jpg)
![](https://images.proteinatlas.org/931/28_D6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P42224-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
