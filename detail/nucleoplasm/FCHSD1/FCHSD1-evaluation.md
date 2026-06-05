---
type: protein-evaluation
gene: "FCHSD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FCHSD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FCHSD1 |
| 蛋白名称 | F-BAR and double SH3 domains protein 1 |
| 蛋白大小 | 690 aa / 76.9 kDa |
| UniProt ID | Q86WN1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Perikaryon; Cell projection; Cytoplasmic vesicle |
| 蛋白大小 | 10/10 | ×1 | 10 | 690 aa / 76.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=76.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027267, IPR031160, IPR001060, IPR035460, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Cytoplasm; Perikaryon; Cell projection; Cytoplasmic vesicle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell projection (GO:0042995)
- cuticular plate (GO:0032437)
- cytosol (GO:0005829)
- neuromuscular junction (GO:0031594)
- perikaryon (GO:0043204)
- protein-containing complex (GO:0032991)
- recycling endosome (GO:0055037)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 18 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Genetic predisposition to porto-sinusoidal vascular disorder: A functional genomic-based, multigenerational family study.. *Hepatology (Baltimore, Md.)*. PMID: 35989577
2. Identification and characterization of human FCHSD1 and FCHSD2 genes in silico.. *International journal of molecular medicine*. PMID: 15067381
3. Comprehensive pan-cancer analysis and experimental validation reveal FCHSD1 as a potential biomarker for diagnosis, immune infiltration, and prognosis.. *Frontiers in oncology*. PMID: 40535123
4. Key genes and immune infiltration patterns and the clinical implications in psoriasis patients.. *Skin research and technology : official journal of International Society for Bioengineering and the Skin (ISBS) [and] International Society for Digital Imaging of Skin (ISDIS) [and] International Society for Skin Imaging (ISSI)*. PMID: 39120060
5. FCHSD1 and FCHSD2 are expressed in hair cell stereocilia and cuticular plate and regulate actin polymerization in vitro.. *PloS one*. PMID: 23437151

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.7 |
| 高置信度残基 (pLDDT>90) 占比 | 36.4% |
| 置信残基 (pLDDT 70-90) 占比 | 34.9% |
| 中等置信 (pLDDT 50-70) 占比 | 10.0% |
| 低置信 (pLDDT<50) 占比 | 18.7% |
| 有序区域 (pLDDT>70) 占比 | 71.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=76.7，有序区 71.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027267, IPR031160, IPR001060, IPR035460, IPR036028; Pfam: PF00611, PF14604 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SNX9 | 0.813 | 0.340 | — |
| FNBP1 | 0.672 | 0.000 | — |
| TRIP10 | 0.642 | 0.000 | — |
| WASL | 0.630 | 0.355 | — |
| FCHO1 | 0.622 | 0.062 | — |
| ITSN2 | 0.617 | 0.504 | — |
| WAS | 0.611 | 0.355 | — |
| NCKIPSD | 0.610 | 0.535 | — |
| SNX16 | 0.599 | 0.094 | — |
| ARHGAP4 | 0.576 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=76.7 + PDB: 无 | pLDDT=76.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Perikaryon; Cell projection; Cytoplasmi / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FCHSD1 — F-BAR and double SH3 domains protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小690 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86WN1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000197948-FCHSD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FCHSD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86WN1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000197948-FCHSD1/subcellular

![](https://images.proteinatlas.org/43795/498_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/43795/498_D11_2_red_green.jpg)
![](https://images.proteinatlas.org/43795/501_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/43795/501_D11_3_red_green.jpg)
![](https://images.proteinatlas.org/43795/512_D11_2_red_green.jpg)
![](https://images.proteinatlas.org/43795/512_D11_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86WN1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
