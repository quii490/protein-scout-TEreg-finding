---
type: protein-evaluation
gene: "AATF"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## AATF 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AATF / CHE1, DED |
| 蛋白名称 | Protein AATF |
| 蛋白大小 | 560 aa / 63.1 kDa |
| UniProt ID | Q9NY61 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; 额外: Nucleoplasm; UniProt: Nucleus, nucleolus |
| 蛋白大小 | 10/10 | ×1 | 10 | 560 aa / 63.1 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=88 篇 (≤100→2) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.8; PDB: 5W6A, 7MQ8, 7MQ9 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR025160, IPR039223, IPR012617; Pfam: PF13339, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **91.5/180** | |
| **归一化总分** | | | **50.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Nucleoplasm | Supported |
| UniProt | Nucleus, nucleolus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- small-subunit processome (GO:0032040)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 88 |
| PubMed broad count | 167 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CHE1, DED |

**关键文献**:
1. Emerging roles of AATF: Checkpoint signaling and beyond.. *Journal of cellular physiology*. PMID: 33145763
2. AATF/Che-1-An RNA Binding Protein at the Nexus of DNA Damage Response and Ribosome Biogenesis.. *Frontiers in oncology*. PMID: 32587828
3. AATF is Overexpressed in Human Head and Neck Squamous Cell Carcinoma and Regulates STAT3/Survivin Signaling.. *OncoTargets and therapy*. PMID: 34785906
4. Che-1/AATF: A Critical Cofactor for Both Wild-Type- and Mutant-p53 Proteins.. *Frontiers in oncology*. PMID: 26913241
5. AATF is Overexpressed in Human Bladder Cancer and Regulates Chemo-Sensitivity Through Survivin.. *OncoTargets and therapy*. PMID: 35002255

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.8 |
| 高置信度残基 (pLDDT>90) 占比 | 22.7% |
| 置信残基 (pLDDT 70-90) 占比 | 21.1% |
| 中等置信 (pLDDT 50-70) 占比 | 25.2% |
| 低置信 (pLDDT<50) 占比 | 31.1% |
| 有序区域 (pLDDT>70) 占比 | 43.8% |
| 可用 PDB 条目 | 5W6A, 7MQ8, 7MQ9 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.8），有序残基占 43.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR025160, IPR039223, IPR012617; Pfam: PF13339, PF08164 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NOL10 | 0.999 | 0.997 | — |
| NAT10 | 0.999 | 0.993 | — |
| NGDN | 0.999 | 0.997 | — |
| UTP11 | 0.998 | 0.991 | — |
| WDR36 | 0.998 | 0.993 | — |
| TBL3 | 0.998 | 0.993 | — |
| BMS1 | 0.998 | 0.991 | — |
| NOL6 | 0.998 | 0.993 | — |
| WDR43 | 0.998 | 0.991 | — |
| WDR3 | 0.998 | 0.991 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DAZAP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| LDOC1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ATM | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-11842|pubmed:17157788 |
| ATR | psi-mi:"MI:0424"(protein kinase assay) | imex:IM-11842|pubmed:17157788 |
| CHEK2 | psi-mi:"MI:0424"(protein kinase assay) | imex:IM-11842|pubmed:17157788 |
| CHEK1 | psi-mi:"MI:0424"(protein kinase assay) | imex:IM-11842|pubmed:17157788 |
| RELA | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-11842|pubmed:17157788 |
| NEDD4L | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| ZNF468 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| SMAD3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.8 + PDB: 5W6A, 7MQ8, 7MQ9 | pLDDT=64.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleolus / Nucleoli; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. AATF — Protein AATF，研究基础较多，新颖性有限。
2. 蛋白大小560 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 88 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=64.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NY61
- Protein Atlas: https://www.proteinatlas.org/ENSG00000275700-AATF/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AATF
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NY61
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (supported)。来源: https://www.proteinatlas.org/ENSG00000275700-AATF/subcellular

![](https://images.proteinatlas.org/75963/1864_D12_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/75963/1864_D12_32_blue_red_green.jpg)
![](https://images.proteinatlas.org/75963/1899_H5_10_cr5ba211585a437_blue_red_green.jpg)
![](https://images.proteinatlas.org/75963/1899_H5_22_cr5ba211585a6ed_blue_red_green.jpg)
![](https://images.proteinatlas.org/75963/1964_C11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/75963/1964_C11_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NY61-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
