---
type: protein-evaluation
gene: "TKFC"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TKFC 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TKFC / DAK |
| 蛋白名称 | Triokinase/FMN cyclase |
| 蛋白大小 | 575 aa / 58.9 kDa |
| UniProt ID | Q3LXA3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 575 aa / 58.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=95.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR012734, IPR004006, IPR004007, IPR036117, IPR050 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 25 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DAK |

**关键文献**:
1. LINC317.5 as a novel biomarker for hypertriglyceridemia in normal glucose metabolism.. *Cell death discovery*. PMID: 38670967
2. Biallelic TYR and TKFC variants in Egyptian patients with OCA1 and new expanded TKFC features.. *BMC genomics*. PMID: 39251934
3. HNF4α is required for Tkfc promoter activation by ChREBP.. *Bioscience, biotechnology, and biochemistry*. PMID: 38782732
4. Alternative Splicing of the Last TKFC Intron Yields Transcripts Differentially Expressed in Human Tissues That Code In Vitro for a Protein Devoid of Triokinase and FMN Cyclase Activity.. *Biomolecules*. PMID: 39456221
5. Recent Progress on Fructose Metabolism-Chrebp, Fructolysis, and Polyol Pathway.. *Nutrients*. PMID: 37049617

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.3 |
| 高置信度残基 (pLDDT>90) 占比 | 89.9% |
| 置信残基 (pLDDT 70-90) 占比 | 8.2% |
| 中等置信 (pLDDT 50-70) 占比 | 1.7% |
| 低置信 (pLDDT<50) 占比 | 0.2% |
| 有序区域 (pLDDT>70) 占比 | 98.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=95.3，有序区 98.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012734, IPR004006, IPR004007, IPR036117, IPR050861; Pfam: PF02733, PF02734 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TPI1 | 0.992 | 0.000 | — |
| GPD2 | 0.979 | 0.000 | — |
| GLYCTK | 0.970 | 0.000 | — |
| IFIH1 | 0.964 | 0.292 | — |
| ALDOB | 0.955 | 0.000 | — |
| ALDOA | 0.920 | 0.000 | — |
| SORD | 0.919 | 0.231 | — |
| ALDOC | 0.915 | 0.000 | — |
| GPD1 | 0.865 | 0.000 | — |
| GPD1L | 0.848 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257121 | psi-mi:"MI:0096"(pull down) | pubmed:19367725|imex:IM-20587 |
| EBI-1257123 | psi-mi:"MI:0096"(pull down) | pubmed:19367725|imex:IM-20587 |
| RP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SNRNP27 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DEFA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IQCF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RDH12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SDCBP | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| NTNG1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SERBP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.3 + PDB: 无 | pLDDT=95.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TKFC — Triokinase/FMN cyclase，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小575 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q3LXA3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000149476-TKFC/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TKFC
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q3LXA3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000149476-TKFC/subcellular

![](https://images.proteinatlas.org/39486/1142_B6_3_red_green.jpg)
![](https://images.proteinatlas.org/39486/1142_B6_4_red_green.jpg)
![](https://images.proteinatlas.org/39486/1208_H1_1_red_green.jpg)
![](https://images.proteinatlas.org/39486/1208_H1_4_red_green.jpg)
![](https://images.proteinatlas.org/39486/2266_A5_10_red_green.jpg)
![](https://images.proteinatlas.org/39486/2266_A5_39_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q3LXA3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
