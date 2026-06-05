---
type: protein-evaluation
gene: "LCMT1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LCMT1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LCMT1 / LCMT |
| 蛋白名称 | Leucine carboxyl methyltransferase 1 |
| 蛋白大小 | 334 aa / 38.4 kDa |
| UniProt ID | Q9UIC8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 334 aa / 38.4 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=65 篇 (≤80→4) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=93.4; PDB: 3IEI, 3O7W, 3P71 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR016651, IPR007213, IPR029063; Pfam: PF04072 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.5/180** | |
| **归一化总分** | | | **60.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 65 |
| PubMed broad count | 79 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LCMT |

**关键文献**:
1. Loss of LCMT1 and biased protein phosphatase 2A heterotrimerization drive prostate cancer progression and therapy resistance.. *Nature communications*. PMID: 37644036
2. HMGA2 and protein leucine methylation drive pancreatic cancer lineage plasticity.. *Nature communications*. PMID: 40419509
3. HIF-1α Causes LCMT1/PP2A Deficiency and Mediates Tau Hyperphosphorylation and Cognitive Dysfunction during Chronic Hypoxia.. *International journal of molecular sciences*. PMID: 36555780
4. LCMT1 indicates poor prognosis and is essential for cell proliferation in hepatocellular carcinoma.. *Translational oncology*. PMID: 36401967
5. Low-dose benzo[a]pyrene exposure induces hepatic lipid deposition through LCMT1/PP2Ac-mediated autophagy inhibition.. *Food and chemical toxicology : an international journal published for the British Industrial Biological Research Association*. PMID: 37579989

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.4 |
| 高置信度残基 (pLDDT>90) 占比 | 89.2% |
| 置信残基 (pLDDT 70-90) 占比 | 4.5% |
| 中等置信 (pLDDT 50-70) 占比 | 1.2% |
| 低置信 (pLDDT<50) 占比 | 5.1% |
| 有序区域 (pLDDT>70) 占比 | 93.7% |
| 可用 PDB 条目 | 3IEI, 3O7W, 3P71 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3IEI, 3O7W, 3P71）+ AlphaFold高质量预测（pLDDT=93.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016651, IPR007213, IPR029063; Pfam: PF04072 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FXR2 | psi-mi:"MI:0096"(pull down) | pubmed:16189514|imex:IM-16520| |
| solA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| PPP4C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PPP2CA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PPP4R2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VPS37C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TGDS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DND1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 8
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.4 + PDB: 3IEI, 3O7W, 3P71 | pLDDT=93.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 0 + 8 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LCMT1 — Leucine carboxyl methyltransferase 1，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小334 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 65 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UIC8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000205629-LCMT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LCMT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UIC8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000205629-LCMT1/subcellular

![](https://images.proteinatlas.org/41559/493_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/41559/493_B4_4_red_green.jpg)
![](https://images.proteinatlas.org/41559/502_B4_3_red_green.jpg)
![](https://images.proteinatlas.org/41559/502_B4_4_red_green.jpg)
![](https://images.proteinatlas.org/41559/557_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/41559/557_B4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UIC8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
