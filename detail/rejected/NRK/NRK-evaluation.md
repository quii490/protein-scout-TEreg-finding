---
type: protein-evaluation
gene: "NRK"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NRK — REJECTED (核定位证据不足 (核定位得分 3/10 ≤ 3); 研究热度过高 (PubMed strict=1454，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NRK |
| 蛋白名称 | Nik-related protein kinase |
| 蛋白大小 | 1582 aa / 178.5 kDa |
| UniProt ID | Q7Z2Y5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA: 暂无HPA定位数据; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 1582 aa / 178.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1454 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=47.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001180, IPR011009, IPR000719, IPR017441, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 5 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **58.5/180** | |
| **归一化总分** | | | **32.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1454 |
| PubMed broad count | 2854 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. PKC regulates αKlotho gene expression in MDCK and NRK-52E cells.. *Pflugers Archiv : European journal of physiology*. PMID: 37773536
2. Sanqi oral solution ameliorates renal fibrosis by suppressing fibroblast activation via HIF-1α/PKM2/glycolysis pathway in chronic kidney disease.. *Journal of ethnopharmacology*. PMID: 39121930
3. Geniposidic Acid Attenuates Chronic Tubulointerstitial Nephropathy Through Regulation of the NF-ƙB/Nrf2 Pathway Via Aryl Hydrocarbon Receptor Signaling.. *Phytotherapy research : PTR*. PMID: 39289784
4. Proteomic analysis of Nrk gene-disrupted placental tissue cells explains physiological significance of NRK.. *BMC research notes*. PMID: 31783915
5. Insoluble HIFa protein aggregates by cadmium disrupt hypoxia-prolyl hydroxylase (PHD)-hypoxia inducible factor (HIFa) signaling in renal epithelial (NRK-52E) and interstitial (FAIK3-5) cells.. *Biometals : an international journal on the role of metal ions in biology, biochemistry, and medicine*. PMID: 39256317

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 47.5 |
| 高置信度残基 (pLDDT>90) 占比 | 9.5% |
| 置信残基 (pLDDT 70-90) 占比 | 14.4% |
| 中等置信 (pLDDT 50-70) 占比 | 9.1% |
| 低置信 (pLDDT<50) 占比 | 66.9% |
| 有序区域 (pLDDT>70) 占比 | 23.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=47.5），有序残基占 23.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001180, IPR011009, IPR000719, IPR017441, IPR008271; Pfam: PF00780, PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KRTAP7-1 | 0.529 | 0.000 | — |
| KLHDC10 | 0.495 | 0.000 | — |
| ZBTB32 | 0.450 | 0.000 | — |
| FSIP2 | 0.430 | 0.070 | — |
| RESF1 | 0.406 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RYBP | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:34316702|imex:IM-29168 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 5，IntAct interactions: 1
- 调控相关比例: 0 / 5 = 0%

**评价**: STRING 5 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=47.5 + PDB: 无 | pLDDT=47.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 5 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. NRK — Nik-related protein kinase，研究基础较多，新颖性有限。
2. 蛋白大小1582 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 1454 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=47.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z2Y5
- Protein Atlas: https://www.proteinatlas.org/search/NRK
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NRK
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z2Y5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000123572-NRK/subcellular

![](https://images.proteinatlas.org/17238/1161_F10_2_red_green.jpg)
![](https://images.proteinatlas.org/17238/1161_F10_3_red_green.jpg)
![](https://images.proteinatlas.org/17238/166_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/17238/166_B8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7Z2Y5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
