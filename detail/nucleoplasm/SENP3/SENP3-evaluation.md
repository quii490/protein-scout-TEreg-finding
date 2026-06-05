---
type: protein-evaluation
gene: "SENP3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SENP3 — REJECTED (研究热度过高 (PubMed strict=124，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SENP3 / SSP3, SUSP3 |
| 蛋白名称 | Sentrin-specific protease 3 |
| 蛋白大小 | 574 aa / 65.0 kDa |
| UniProt ID | Q9H4L4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; 额外: Nucleoplasm; UniProt: Nucleus, nucleolus; Nucleus, nucleoplasm; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 574 aa / 65.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=124 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.6; PDB: 9ME8 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR038765, IPR003653, IPR045577; Pfam: PF02902, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Nucleoplasm | Supported |
| UniProt | Nucleus, nucleolus; Nucleus, nucleoplasm; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- MLL1 complex (GO:0071339)
- nuclear body (GO:0016604)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 124 |
| PubMed broad count | 206 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SSP3, SUSP3 |

**关键文献**:
1. Full-coverage regulations of autophagy by ROS: from induction to maturation.. *Autophagy*. PMID: 34662529
2. SENP3 Drives Abdominal Aortic Aneurysm Development by Regulating Ferroptosis via De-SUMOylation of CTH.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40019399
3. Astragaloside IV combined with ligustrazine ameliorates abnormal mitochondrial dynamics via Drp1 SUMO/deSUMOylation in cerebral ischemia-reperfusion injury.. *CNS neuroscience & therapeutics*. PMID: 38615367
4. Redox regulation of TRIM28 facilitates neuronal ferroptosis by promoting SUMOylation and inhibiting OPTN-selective autophagic degradation of ACSL4.. *Cell death and differentiation*. PMID: 39875520
5. SENP3: Cancers and diseases.. *Biochimica et biophysica acta. Reviews on cancer*. PMID: 39765284

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.6 |
| 高置信度残基 (pLDDT>90) 占比 | 41.3% |
| 置信残基 (pLDDT 70-90) 占比 | 5.2% |
| 中等置信 (pLDDT 50-70) 占比 | 4.4% |
| 低置信 (pLDDT<50) 占比 | 49.1% |
| 有序区域 (pLDDT>70) 占比 | 46.5% |
| 可用 PDB 条目 | 9ME8 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.6），有序残基占 46.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR038765, IPR003653, IPR045577; Pfam: PF02902, PF19722 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TEX10 | 0.998 | 0.818 | — |
| PELP1 | 0.997 | 0.836 | — |
| LAS1L | 0.996 | 0.777 | — |
| SUMO1 | 0.986 | 0.309 | — |
| SUMO2 | 0.978 | 0.620 | — |
| WDR18 | 0.975 | 0.855 | — |
| KMT2A | 0.960 | 0.297 | — |
| WDR5 | 0.956 | 0.407 | — |
| RBBP5 | 0.954 | 0.292 | — |
| NOL9 | 0.952 | 0.504 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CDK6 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22094256|imex:IM-16628 |
| CDK4 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22094256|imex:IM-16628 |
| ESR2 | psi-mi:"MI:0029"(cosedimentation through density g | imex:IM-13781|pubmed:21182203 |
| RRP1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-26310|pubmed:20926688 |
| Mycbp2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| WDR18 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| VIM | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H1-5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.6 + PDB: 9ME8 | pLDDT=64.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleolus; Nucleus, nucleoplasm; Cytoplas / Nucleoli; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SENP3 — Sentrin-specific protease 3，研究基础较多，新颖性有限。
2. 蛋白大小574 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 124 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=64.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 124 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H4L4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000161956-SENP3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SENP3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H4L4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/SENP3/IF_images/SENP3_IF_1039_A12_2_red_green.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (supported)。来源: https://www.proteinatlas.org/ENSG00000161956-SENP3/subcellular

![](https://images.proteinatlas.org/60290/1037_A12_2_red_green.jpg)
![](https://images.proteinatlas.org/60290/1037_A12_3_red_green.jpg)
![](https://images.proteinatlas.org/60290/1039_A12_2_red_green.jpg)
![](https://images.proteinatlas.org/60290/1039_A12_4_red_green.jpg)
![](https://images.proteinatlas.org/60290/1226_H4_2_red_green.jpg)
![](https://images.proteinatlas.org/60290/1226_H4_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H4L4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
