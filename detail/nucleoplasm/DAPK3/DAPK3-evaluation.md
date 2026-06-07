---
type: protein-evaluation
gene: "DAPK3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DAPK3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DAPK3 / ZIPK |
| 蛋白名称 | Death-associated protein kinase 3 |
| 蛋白大小 | 454 aa / 52.5 kDa |
| UniProt ID | O43293 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Vesicles, Primary cilium; UniProt: Nucleus; Nucleus, PML body; Cytoplasm, cytoskeleton, microtu |
| 蛋白大小 | 10/10 | ×1 | 10 | 454 aa / 52.5 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=88 篇 (≤100→2) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=87.0; PDB: 1YRP, 2J90, 3BHY, 3BQR, 5A6N, 5A6O, 5VJA |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR042870, IPR011009, IPR000719, IPR017441, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **105.5/180** | |
| **归一化总分** | | | **58.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Vesicles, Primary cilium | Supported |
| UniProt | Nucleus; Nucleus, PML body; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Chro... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- chromosome, centromeric region (GO:0000775)
- cilium (GO:0005929)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- midbody (GO:0030496)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 88 |
| PubMed broad count | 120 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ZIPK |

**关键文献**:
1. The tumor suppressor kinase DAPK3 drives tumor-intrinsic immunity through the STING-IFN-β pathway.. *Nature immunology*. PMID: 33767426
2. Death-associated protein kinase 3 modulates migration and invasion of triple-negative breast cancer cells.. *PNAS nexus*. PMID: 39319326
3. DAPK3 is Essential for DBP-Induced Autophagy of Mouse Leydig Cells.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40047320
4. Death-associated protein kinase 3 regulates the myogenic reactivity of cerebral arteries.. *Experimental physiology*. PMID: 37084168
5. DAPK3 inhibits gastric cancer progression via activation of ULK1-dependent autophagy.. *Cell death and differentiation*. PMID: 33037394

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.0 |
| 高置信度残基 (pLDDT>90) 占比 | 60.8% |
| 置信残基 (pLDDT 70-90) 占比 | 28.0% |
| 中等置信 (pLDDT 50-70) 占比 | 5.1% |
| 低置信 (pLDDT<50) 占比 | 6.2% |
| 有序区域 (pLDDT>70) 占比 | 88.8% |
| 可用 PDB 条目 | 1YRP, 2J90, 3BHY, 3BQR, 5A6N, 5A6O, 5VJA |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1YRP, 2J90, 3BHY, 3BQR, 5A6N, 5A6O, 5VJA）+ AlphaFold极高置信度预测（pLDDT=87.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR042870, IPR011009, IPR000719, IPR017441, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LUZP1 | 0.994 | 0.994 | — |
| BECN1 | 0.972 | 0.000 | — |
| PAWR | 0.938 | 0.526 | — |
| DAPK1 | 0.936 | 0.000 | — |
| MAPK3 | 0.929 | 0.168 | — |
| MAPK1 | 0.922 | 0.168 | — |
| BECN2 | 0.911 | 0.000 | — |
| DAPK2 | 0.903 | 0.000 | — |
| CALML3 | 0.896 | 0.400 | — |
| CALML5 | 0.896 | 0.400 | — |

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
| 三维结构 | AlphaFold pLDDT=87.0 + PDB: 1YRP, 2J90, 3BHY, 3BQR, 5A6N,  | pLDDT=87.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, PML body; Cytoplasm, cytoskeleto / Nucleoplasm, Cytosol; 额外: Vesicles, Primary cilium | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DAPK3 — Death-associated protein kinase 3，研究基础较多，新颖性有限。
2. 蛋白大小454 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 88 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43293
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167657-DAPK3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DAPK3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43293
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000167657-DAPK3/subcellular

![](https://images.proteinatlas.org/28569/2234_A5_15_blue_red_green.jpg)
![](https://images.proteinatlas.org/28569/2234_A5_99_blue_red_green.jpg)
![](https://images.proteinatlas.org/28569/2241_E6_36_blue_red_green.jpg)
![](https://images.proteinatlas.org/28569/2241_E6_52_blue_red_green.jpg)
![](https://images.proteinatlas.org/28569/2244_E4_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/28569/2244_E4_43_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O43293-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O43293 |
| SMART | SM00220; |
| UniProt Domain [FT] | DOMAIN 13..275; /note="Protein kinase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00159" |
| InterPro | IPR042870;IPR011009;IPR000719;IPR017441;IPR008271; |
| Pfam | PF00069; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000167657-DAPK3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| LUZP1 | Intact, Biogrid, Opencell | true |
| CALD1 | Opencell | false |
| CAPZB | Opencell | false |
| CDKN1A | Biogrid | false |
| GPS2 | Bioplex | false |
| MDM2 | Biogrid | false |
| PAWR | Biogrid | false |
| PPP1R12A | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
