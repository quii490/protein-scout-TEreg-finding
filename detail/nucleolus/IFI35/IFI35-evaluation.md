---
type: protein-evaluation
gene: "IFI35"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## IFI35 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | IFI35 / IFP35 |
| 蛋白名称 | Interferon-induced 35 kDa protein |
| 蛋白大小 | 286 aa / 31.5 kDa |
| UniProt ID | P80217 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Nucleoli; UniProt: Cytoplasm; Nucleus; Secreted |
| 蛋白大小 | 10/10 | ×1 | 10 | 286 aa / 31.5 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=76 篇 (≤80→4) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=83.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR009909, IPR009938, IPR012677; Pfam: PF07334, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **105.5/180** | |
| **归一化总分** | | | **58.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Nucleoli | Supported |
| UniProt | Cytoplasm; Nucleus; Secreted | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular space (GO:0005615)
- membrane (GO:0016020)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 76 |
| PubMed broad count | 103 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: IFP35 |

**关键文献**:
1. Empagliflozin protects against heart failure with preserved ejection fraction partly by inhibiting the senescence-associated STAT1-STING axis.. *Cardiovascular diabetology*. PMID: 39044275
2. Tumor-secreted IFI35 promotes proliferation and cytotoxic activity of CD8(+) T cells through PI3K/AKT/mTOR signaling pathway in colorectal cancer.. *Journal of biomedical science*. PMID: 37380972
3. Blockade of Interferon-Induced Protein 35 Alleviates Cisplatin-Induced Ferroptosis in Acute Kidney Injury Through Activation of the NRF2.. *Journal of biochemical and molecular toxicology*. PMID: 40654249
4. Interferon-inducible protein IFI35 negatively regulates RIG-I antiviral signaling and supports vesicular stomatitis virus replication.. *Journal of virology*. PMID: 24371060
5. Characterization of chicken IFI35 and its antiviral activity against Newcastle disease virus.. *The Journal of veterinary medical science*. PMID: 35135934

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.2 |
| 高置信度残基 (pLDDT>90) 占比 | 46.9% |
| 置信残基 (pLDDT 70-90) 占比 | 37.8% |
| 中等置信 (pLDDT 50-70) 占比 | 7.0% |
| 低置信 (pLDDT<50) 占比 | 8.4% |
| 有序区域 (pLDDT>70) 占比 | 84.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=83.2，有序区 84.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009909, IPR009938, IPR012677; Pfam: PF07334, PF07292 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FAU | 0.995 | 0.967 | — |
| NMI | 0.982 | 0.812 | — |
| RPS18 | 0.981 | 0.840 | — |
| RPL8 | 0.981 | 0.839 | — |
| RPL23 | 0.980 | 0.839 | — |
| RPS19 | 0.980 | 0.839 | — |
| RPL36 | 0.980 | 0.834 | — |
| RPS24 | 0.980 | 0.840 | — |
| RPL14 | 0.980 | 0.836 | — |
| RPL35A | 0.980 | 0.840 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAPK1 | psi-mi:"MI:0018"(two hybrid) | pubmed:18624398|imex:IM-19021 |
| PLEKHO1 | psi-mi:"MI:0018"(two hybrid) | pubmed:18624398|imex:IM-19021 |
| CLEC4G | psi-mi:"MI:0018"(two hybrid) | pubmed:18624398|imex:IM-19021 |
| PDGFRB | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| FHL2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| EML2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TFAP2A | psi-mi:"MI:0018"(two hybrid) | imex:IM-22985|pubmed:24835590 |
| STAT5A | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| - | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| PTPN11 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.2 + PDB: 无 | pLDDT=83.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Secreted / Nucleoplasm, Cytosol; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. IFI35 — Interferon-induced 35 kDa protein，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小286 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 76 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P80217
- Protein Atlas: https://www.proteinatlas.org/ENSG00000068079-IFI35/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=IFI35
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P80217
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000068079-IFI35/subcellular

![](https://images.proteinatlas.org/3283/1964_F1_2_red_green.jpg)
![](https://images.proteinatlas.org/3283/1964_F1_3_red_green.jpg)
![](https://images.proteinatlas.org/3283/2058_C9_1_red_green.jpg)
![](https://images.proteinatlas.org/3283/2058_C9_2_red_green.jpg)
![](https://images.proteinatlas.org/3283/2089_B1_3_red_green.jpg)
![](https://images.proteinatlas.org/3283/2089_B1_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P80217-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
