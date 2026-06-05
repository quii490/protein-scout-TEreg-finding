---
type: protein-evaluation
gene: "SAMHD1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SAMHD1 — REJECTED (研究热度过高 (PubMed strict=573，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SAMHD1 / MOP5 |
| 蛋白名称 | Deoxynucleoside triphosphate triphosphohydrolase SAMHD1 |
| 蛋白大小 | 626 aa / 72.2 kDa |
| UniProt ID | Q9Y3Z3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Plasma membrane; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 626 aa / 72.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=573 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=88.2; PDB: 2E8O, 3U1N, 4BZB, 4BZC, 4CC9, 4MZ7, 4Q7H |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR050135, IPR003607, IPR006674, IPR001660, IPR013 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.5/180** | |
| **归一化总分** | | | **51.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Plasma membrane | Supported |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)
- site of double-strand break (GO:0035861)
- tetraspanin-enriched microdomain (GO:0097197)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 573 |
| PubMed broad count | 910 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MOP5 |

**关键文献**:
1. Nucleotide metabolic rewiring enables NLRP3 inflammasome hyperactivation in obesity.. *Science (New York, N.Y.)*. PMID: 41538457
2. Genetic links between ovarian ageing, cancer risk and de novo mutation rates.. *Nature*. PMID: 39261734
3. Thymidine nucleotide metabolism controls human telomere length.. *Nature genetics*. PMID: 36959362
4. Characterization of human disease phenotypes associated with mutations in TREX1, RNASEH2A, RNASEH2B, RNASEH2C, SAMHD1, ADAR, and IFIH1.. *American journal of medical genetics. Part A*. PMID: 25604658
5. SAMHD1 Functions and Human Diseases.. *Viruses*. PMID: 32244340

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.2 |
| 高置信度残基 (pLDDT>90) 占比 | 74.4% |
| 置信残基 (pLDDT 70-90) 占比 | 14.2% |
| 中等置信 (pLDDT 50-70) 占比 | 1.8% |
| 低置信 (pLDDT<50) 占比 | 9.6% |
| 有序区域 (pLDDT>70) 占比 | 88.6% |
| 可用 PDB 条目 | 2E8O, 3U1N, 4BZB, 4BZC, 4CC9, 4MZ7, 4Q7H, 4QFX, 4QFY, 4QFZ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2E8O, 3U1N, 4BZB, 4BZC, 4CC9, 4MZ7, 4Q7H, 4QFX, 4QFY, 4QFZ）+ AlphaFold极高置信度预测（pLDDT=88.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050135, IPR003607, IPR006674, IPR001660, IPR013761; Pfam: PF01966, PF07647 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 无PPI数据
- STRING partners: 0，IntAct interactions: 0
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.2 + PDB: 2E8O, 3U1N, 4BZB, 4BZC, 4CC9,  | pLDDT=88.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / Nucleoplasm; 额外: Plasma membrane | 一致 |
| PPI | STRING + IntAct | 0 + 0 interactions | 数据有限 |

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
1. SAMHD1 — Deoxynucleoside triphosphate triphosphohydrolase SAMHD1，研究基础较多，新颖性有限。
2. 蛋白大小626 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 573 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 573 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y3Z3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000101347-SAMHD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SAMHD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y3Z3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000101347-SAMHD1/subcellular

![](https://images.proteinatlas.org/47072/2177_B7_38_red_green.jpg)
![](https://images.proteinatlas.org/47072/2177_B7_64_red_green.jpg)
![](https://images.proteinatlas.org/47072/742_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/47072/742_B9_2_red_green.jpg)
![](https://images.proteinatlas.org/47072/807_G2_2_red_green.jpg)
![](https://images.proteinatlas.org/47072/807_G2_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y3Z3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
