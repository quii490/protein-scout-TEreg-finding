---
type: protein-evaluation
gene: "PPM1A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PPM1A — REJECTED (研究热度过高 (PubMed strict=130，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PPM1A / PPPM1A |
| 蛋白名称 | Protein phosphatase 1A |
| 蛋白大小 | 382 aa / 42.4 kDa |
| UniProt ID | P35813 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Plasma membrane; UniProt: Nucleus; Cytoplasm, cytosol; Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 382 aa / 42.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=130 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=94.5; PDB: 1A6Q, 3FXJ, 3FXK, 3FXL, 3FXM, 3FXO, 4RA2 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR015655, IPR000222, IPR012911, IPR036580, IPR036 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.5/180** | |
| **归一化总分** | | | **51.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Plasma membrane | Supported |
| UniProt | Nucleus; Cytoplasm, cytosol; Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 130 |
| PubMed broad count | 244 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PPPM1A |

**关键文献**:
1. Metal-dependent Ser/Thr protein phosphatase PPM family: Evolution, structures, diseases and inhibitors.. *Pharmacology & therapeutics*. PMID: 32650009
2. Astrocytic NDRG2-PPM1A interaction exacerbates blood-brain barrier disruption after subarachnoid hemorrhage.. *Science advances*. PMID: 36179025
3. m(6)A mRNA methylation regulates testosterone synthesis through modulating autophagy in Leydig cells.. *Autophagy*. PMID: 31983283
4. Protein phosphatase PPM1A inhibition attenuates osteoarthritis via regulating TGF-β/Smad2 signaling in chondrocytes.. *JCI insight*. PMID: 36752205
5. A comprehensive overview of PPM1A: From structure to disease.. *Experimental biology and medicine (Maywood, N.J.)*. PMID: 34861123

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.5 |
| 高置信度残基 (pLDDT>90) 占比 | 90.1% |
| 置信残基 (pLDDT 70-90) 占比 | 5.0% |
| 中等置信 (pLDDT 50-70) 占比 | 1.3% |
| 低置信 (pLDDT<50) 占比 | 3.7% |
| 有序区域 (pLDDT>70) 占比 | 95.1% |
| 可用 PDB 条目 | 1A6Q, 3FXJ, 3FXK, 3FXL, 3FXM, 3FXO, 4RA2, 4RAF, 4RAG, 6B67 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1A6Q, 3FXJ, 3FXK, 3FXL, 3FXM, 3FXO, 4RA2, 4RAF, 4RAG, 6B67）+ AlphaFold极高置信度预测（pLDDT=94.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015655, IPR000222, IPR012911, IPR036580, IPR036457; Pfam: PF00481, PF07830 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LXN | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| NR4A1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| HSPB1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| RPLP0 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| FGFR2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| rpoB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ARRB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17620599 |
| ARRB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17620599 |
| AKT1 | psi-mi:"MI:0813"(proximity ligation assay) | pubmed:25241761|imex:IM-18707 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.5 + PDB: 1A6Q, 3FXJ, 3FXK, 3FXL, 3FXM,  | pLDDT=94.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytosol; Membrane / Cytosol; 额外: Plasma membrane | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

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
1. PPM1A — Protein phosphatase 1A，研究基础较多，新颖性有限。
2. 蛋白大小382 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 130 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 130 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P35813
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100614-PPM1A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PPM1A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P35813
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000100614-PPM1A/subcellular

![](https://images.proteinatlas.org/29209/917_B12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29209/917_B12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/29209/920_B12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29209/920_B12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/29209/958_G12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29209/958_G12_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P35813-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
