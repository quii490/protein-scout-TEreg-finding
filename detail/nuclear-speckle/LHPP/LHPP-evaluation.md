---
type: protein-evaluation
gene: "LHPP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LHPP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LHPP |
| 蛋白名称 | Phospholysine phosphohistidine inorganic pyrophosphate phosphatase |
| 蛋白大小 | 270 aa / 29.2 kDa |
| UniProt ID | Q9H008 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 270 aa / 29.2 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=78 篇 (≤80→4) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=97.2; PDB: 2X4D |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036412, IPR006357, IPR023214, IPR006355; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.0/180** | |
| **归一化总分** | | | **60.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear speck (GO:0016607)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 78 |
| PubMed broad count | 123 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Targeting LHPP in neoadjuvant chemotherapy resistance of gastric cancer: insights from single-cell and multi-omics data on tumor immune microenvironment and stemness characteristics.. *Cell death & disease*. PMID: 40240758
2. Histidine Phosphorylation: Protein Kinases and Phosphatases.. *International journal of molecular sciences*. PMID: 39063217
3. LHPP suppresses proliferation, migration, and invasion and promotes apoptosis in pancreatic cancer.. *Bioscience reports*. PMID: 32186702
4. Phospholysine phosphohistidine inorganic pyrophosphate phosphatase suppresses insulin-like growth factor 1 receptor expression to inhibit cell adhesion and proliferation in gastric cancer.. *MedComm*. PMID: 38292328
5. Does the LHPP gene share a common biological function in pancancer progression?. *BMC medical genomics*. PMID: 36376886

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 97.2 |
| 高置信度残基 (pLDDT>90) 占比 | 95.9% |
| 置信残基 (pLDDT 70-90) 占比 | 3.3% |
| 中等置信 (pLDDT 50-70) 占比 | 0.7% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.2% |
| 可用 PDB 条目 | 2X4D |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=97.2，有序区 99.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036412, IPR006357, IPR023214, IPR006355; Pfam: PF13344, PF13242 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PPA1 | 0.944 | 0.000 | — |
| PPA2 | 0.934 | 0.000 | — |
| ATP12A | 0.918 | 0.000 | — |
| ATP4A | 0.913 | 0.000 | — |
| ATP4B | 0.912 | 0.000 | — |
| ATP5PB | 0.807 | 0.000 | — |
| ATP5MC3 | 0.775 | 0.000 | — |
| ATP6V0A4 | 0.774 | 0.000 | — |
| ATP5MF | 0.768 | 0.000 | — |
| ATP6V0A2 | 0.765 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TNFRSF14 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ZSCAN23 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MYG1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MYH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MYH7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MYH8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CREG1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CLIC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HDHD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RPIA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=97.2 + PDB: 2X4D | pLDDT=97.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nuclear speckles, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LHPP — Phospholysine phosphohistidine inorganic pyrophosphate phosphatase，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小270 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 78 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H008
- Protein Atlas: https://www.proteinatlas.org/ENSG00000107902-LHPP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LHPP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H008
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (supported)。来源: https://www.proteinatlas.org/ENSG00000107902-LHPP/subcellular

![](https://images.proteinatlas.org/9163/44_H1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/9163/44_H1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/9163/45_H1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/9163/45_H1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/9163/46_H1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/9163/46_H1_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H008-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
