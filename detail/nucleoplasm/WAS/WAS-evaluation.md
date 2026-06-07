---
type: protein-evaluation
gene: "WAS"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## WAS 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | WAS / IMD2 |
| 蛋白名称 | Actin nucleation-promoting factor WAS |
| 蛋白大小 | 502 aa / 52.9 kDa |
| UniProt ID | P42768 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane; 额外: Cytosol; UniProt: Cytoplasm, cytoskeleton; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 502 aa / 52.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.4; PDB: 1CEE, 1EJ5, 1T84, 2A3Z, 2K42, 2OT0 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000095, IPR036936, IPR011993, IPR011026, IPR033 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.0/180** | |
| **归一化总分** | | | **72.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Cytosol | Approved |
| UniProt | Cytoplasm, cytoskeleton; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- actin filament (GO:0005884)
- cell-cell junction (GO:0005911)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- nucleus (GO:0005634)
- phagocytic vesicle (GO:0045335)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 908 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: IMD2 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.4 |
| 高置信度残基 (pLDDT>90) 占比 | 23.5% |
| 置信残基 (pLDDT 70-90) 占比 | 26.5% |
| 中等置信 (pLDDT 50-70) 占比 | 25.7% |
| 低置信 (pLDDT<50) 占比 | 24.3% |
| 有序区域 (pLDDT>70) 占比 | 50.0% |
| 可用 PDB 条目 | 1CEE, 1EJ5, 1T84, 2A3Z, 2K42, 2OT0 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.4），有序残基占 50.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000095, IPR036936, IPR011993, IPR011026, IPR033927; Pfam: PF00786, PF00568, PF02205 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ACTR2 | 0.999 | 0.861 | — |
| WIPF1 | 0.999 | 0.950 | — |
| NCK1 | 0.999 | 0.772 | — |
| HCLS1 | 0.999 | 0.314 | — |
| CDC42 | 0.999 | 0.992 | — |
| TRIP10 | 0.998 | 0.710 | — |
| ARPC3 | 0.998 | 0.796 | — |
| ARPC2 | 0.997 | 0.573 | — |
| ACTR3 | 0.996 | 0.645 | — |
| CTTN | 0.996 | 0.314 | — |

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
| 三维结构 | AlphaFold pLDDT=69.4 + PDB: 1CEE, 1EJ5, 1T84, 2A3Z, 2K42,  | pLDDT=69.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Nucleus / Plasma membrane; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. WAS — Actin nucleation-promoting factor WAS，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小502 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=69.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P42768
- Protein Atlas: https://www.proteinatlas.org/ENSG00000015285-WAS/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=WAS
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P42768
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000015285-WAS/subcellular

![](https://images.proteinatlas.org/2022/1779_G4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/2022/1779_G4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/2022/1813_F8_17_cr59f33e96bd992_blue_red_green.jpg)
![](https://images.proteinatlas.org/2022/1813_F8_24_cr59f33e96be102_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P42768-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A0A0C5B5G6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR054130; |
| Pfam | PF21945; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000015285-WAS/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CDC42 | Intact, Biogrid | true |
| FYN | Intact, Biogrid | true |
| NCK1 | Intact, Biogrid | true |
| NCK2 | Intact, Biogrid | true |
| PSTPIP1 | Intact, Biogrid | true |
| SNX9 | Intact, Biogrid | true |
| WIPF1 | Intact, Biogrid | true |
| ABI3 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
