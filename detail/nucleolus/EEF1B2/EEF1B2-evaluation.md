---
type: protein-evaluation
gene: "EEF1B2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EEF1B2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EEF1B2 / EEF1B, EF1B |
| 蛋白名称 | Elongation factor 1-beta |
| 蛋白大小 | 225 aa / 24.8 kDa |
| UniProt ID | P24534 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli fibrillar center, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 225 aa / 24.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=26 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=77.3; PDB: 1B64, 5DQS |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036219, IPR018940, IPR049720, IPR014038, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.5/180** | |
| **归一化总分** | | | **65.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- eukaryotic translation elongation factor 1 complex (GO:0005853)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 26 |
| PubMed broad count | 35 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EEF1B, EF1B |

**关键文献**:
1. EEF1B2 regulates the proliferation and apoptosis of human spermatogonial stem cell lines through TAF4B.. *Heliyon*. PMID: 39281470
2. Novel biallelic loss of EEF1B2 function links to autosomal recessive intellectual disability.. *Human mutation*. PMID: 35015920
3. Proteogenomics Integrating Novel Junction Peptide Identification Strategy Discovers Three Novel Protein Isoforms of Human NHSL1 and EEF1B2.. *Journal of proteome research*. PMID: 34420305
4. Sex Difference of Ribosome in Stroke-Induced Peripheral Immunosuppression by Integrated Bioinformatics Analysis.. *BioMed research international*. PMID: 33354565
5. The role of translation elongation factor eEF1 subunits in neurodevelopmental disorders.. *Human mutation*. PMID: 30370994

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.3 |
| 高置信度残基 (pLDDT>90) 占比 | 16.0% |
| 置信残基 (pLDDT 70-90) 占比 | 61.8% |
| 中等置信 (pLDDT 50-70) 占比 | 11.1% |
| 低置信 (pLDDT<50) 占比 | 11.1% |
| 有序区域 (pLDDT>70) 占比 | 77.8% |
| 可用 PDB 条目 | 1B64, 5DQS |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1B64, 5DQS）+ AlphaFold高质量预测（pLDDT=77.3），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036219, IPR018940, IPR049720, IPR014038, IPR036282; Pfam: PF10587, PF00736 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EEF1G | 0.999 | 0.999 | — |
| EEF1A1 | 0.999 | 0.952 | — |
| EEF1D | 0.999 | 0.845 | — |
| EEF1A2 | 0.996 | 0.919 | — |
| TPT1 | 0.994 | 0.536 | — |
| RACK1 | 0.993 | 0.142 | — |
| RPS3 | 0.993 | 0.172 | — |
| RPL21 | 0.989 | 0.093 | — |
| RPS8 | 0.988 | 0.110 | — |
| RPS3A | 0.988 | 0.107 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.3 + PDB: 1B64, 5DQS | pLDDT=77.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli fibrillar center, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. EEF1B2 — Elongation factor 1-beta，非常新颖，仅有少数基础研究。
2. 蛋白大小225 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 26 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P24534
- Protein Atlas: https://www.proteinatlas.org/ENSG00000114942-EEF1B2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EEF1B2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P24534
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli fibrillar center (approved)。来源: https://www.proteinatlas.org/ENSG00000114942-EEF1B2/subcellular

![](https://images.proteinatlas.org/35029/739_A1_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/35029/739_A1_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/35029/752_F5_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/35029/752_F5_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/35029/753_A1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/35029/753_A1_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P24534-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
