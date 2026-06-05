---
type: protein-evaluation
gene: "CACYBP"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CACYBP — REJECTED (研究热度过高 (PubMed strict=147，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CACYBP / S100A6BP, SIP |
| 蛋白名称 | Calcyclin-binding protein |
| 蛋白大小 | 228 aa / 26.2 kDa |
| UniProt ID | Q9HB71 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoplasm; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 228 aa / 26.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=147 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=81.6; PDB: 1X5M, 2A25, 2A26 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR037201, IPR052289, IPR037893, IPR007052, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.0/180** | |
| **归一化总分** | | | **51.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm | Enhanced |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- beta-catenin destruction complex (GO:0030877)
- cell body (GO:0044297)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- nuclear envelope lumen (GO:0005641)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- SCF ubiquitin ligase complex (GO:0019005)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 147 |
| PubMed broad count | 176 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: S100A6BP, SIP |

**关键文献**:
1. Blockage of CacyBP inhibits macrophage recruitment and improves anti-PD-1 therapy in hepatocellular carcinoma.. *Journal of experimental & clinical cancer research : CR*. PMID: 37968706
2. CacyBP/SIP--Structure and variety of functions.. *Biochimica et biophysica acta*. PMID: 26493724
3. Astrocytes modulate neuronal development by S100A6 signaling.. *Nature communications*. PMID: 41083480
4. CacyBP/SIP - RPL6 interaction: potential influence on ribosome function.. *Amino acids*. PMID: 40691326
5. S100A6 binding protein and Siah-1 interacting protein (CacyBP/SIP): spotlight on properties and cellular function.. *Amino acids*. PMID: 20182755

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.6 |
| 高置信度残基 (pLDDT>90) 占比 | 54.8% |
| 置信残基 (pLDDT 70-90) 占比 | 15.8% |
| 中等置信 (pLDDT 50-70) 占比 | 20.2% |
| 低置信 (pLDDT<50) 占比 | 9.2% |
| 有序区域 (pLDDT>70) 占比 | 70.6% |
| 可用 PDB 条目 | 1X5M, 2A25, 2A26 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1X5M, 2A25, 2A26）+ AlphaFold高质量预测（pLDDT=81.6），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037201, IPR052289, IPR037893, IPR007052, IPR008978; Pfam: PF04969, PF05002, PF09032 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SIAH1 | 0.999 | 0.984 | — |
| SKP1 | 0.999 | 0.840 | — |
| S100A6 | 0.998 | 0.880 | — |
| CTNNB1 | 0.971 | 0.796 | — |
| GSK3B | 0.914 | 0.000 | — |
| AXIN1 | 0.905 | 0.000 | — |
| GSK3A | 0.902 | 0.000 | — |
| APC | 0.900 | 0.000 | — |
| HSP90AA1 | 0.863 | 0.452 | — |
| RNF41 | 0.788 | 0.734 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HLA-B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| GH1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| NME2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TFE3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| FTSJ1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EIF1B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MPG | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EIF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EBI-21351010 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TRAF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.6 + PDB: 1X5M, 2A25, 2A26 | pLDDT=81.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. CACYBP — Calcyclin-binding protein，研究基础较多，新颖性有限。
2. 蛋白大小228 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 147 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 147 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HB71
- Protein Atlas: https://www.proteinatlas.org/ENSG00000116161-CACYBP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CACYBP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HB71
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (enhanced)。来源: https://www.proteinatlas.org/ENSG00000116161-CACYBP/subcellular

![](https://images.proteinatlas.org/25753/212_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/25753/212_H8_2_red_green.jpg)
![](https://images.proteinatlas.org/25753/213_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/25753/213_H8_2_red_green.jpg)
![](https://images.proteinatlas.org/25753/214_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/25753/214_H8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9HB71-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
