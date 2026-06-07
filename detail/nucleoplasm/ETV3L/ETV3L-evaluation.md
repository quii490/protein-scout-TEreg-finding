---
type: protein-evaluation
gene: "ETV3L"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ETV3L 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ETV3L |
| 蛋白名称 | ETS translocation variant 3-like protein |
| 蛋白大小 | 361 aa / 39.9 kDa |
| UniProt ID | Q6ZN32 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm, Nucleoli; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 361 aa / 39.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000418, IPR046328, IPR036388, IPR036390; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 9 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.0/180** | |
| **归一化总分** | | | **76.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli; 额外: Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Mapping Variation in Cellular and Transcriptional Response to 1,25-Dihydroxyvitamin D3 in Peripheral Blood Mononuclear Cells.. *PloS one*. PMID: 27454520
2. Five ETS family members, ELF-1, ETV-4, ETV-3L, ETS-1, and ETS-2 upregulate human leukocyte-associated immunoglobulin-like receptor-1 gene basic promoter activity.. *Aging*. PMID: 29915163
3. Whole exome sequencing of sporadic patients with Currarino Syndrome: A report of three trios.. *Gene*. PMID: 28456592

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.2 |
| 高置信度残基 (pLDDT>90) 占比 | 19.9% |
| 置信残基 (pLDDT 70-90) 占比 | 3.6% |
| 中等置信 (pLDDT 50-70) 占比 | 12.7% |
| 低置信 (pLDDT<50) 占比 | 63.7% |
| 有序区域 (pLDDT>70) 占比 | 23.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=55.2），有序残基占 23.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000418, IPR046328, IPR036388, IPR036390; Pfam: PF00178 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LRRC71 | 0.595 | 0.000 | — |
| PABPC1L2B | 0.453 | 0.000 | — |
| WDR86 | 0.450 | 0.051 | — |
| C17orf107 | 0.447 | 0.000 | — |
| ARHGEF11 | 0.421 | 0.000 | — |
| LRRIQ4 | 0.420 | 0.045 | — |
| UBXN10 | 0.411 | 0.000 | — |
| PEAR1 | 0.404 | 0.000 | — |
| SSX7 | 0.400 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NOTO | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 9，IntAct interactions: 1
- 调控相关比例: 0 / 9 = 0%

**评价**: STRING 9 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.2 + PDB: 无 | pLDDT=55.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nucleoli; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 9 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. ETV3L — ETS translocation variant 3-like protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小361 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=55.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZN32
- Protein Atlas: https://www.proteinatlas.org/ENSG00000253831-ETV3L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ETV3L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZN32
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000253831-ETV3L/subcellular

![](https://images.proteinatlas.org/72144/1935_E7_1_red_green.jpg)
![](https://images.proteinatlas.org/72144/1935_E7_2_red_green.jpg)
![](https://images.proteinatlas.org/72144/2064_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/72144/2064_F10_3_red_green.jpg)
![](https://images.proteinatlas.org/72144/2213_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/72144/2213_G8_5_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6ZN32-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6ZN32 |
| SMART | SM00413; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR000418;IPR046328;IPR036388;IPR036390; |
| Pfam | PF00178; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000253831-ETV3L/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NOTO | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
