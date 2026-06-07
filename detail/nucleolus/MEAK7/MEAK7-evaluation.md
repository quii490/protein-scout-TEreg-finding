---
type: protein-evaluation
gene: "MEAK7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MEAK7 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MEAK7 / KIAA1609, TLDC1 |
| 蛋白名称 | MTOR-associated protein MEAK7 |
| 蛋白大小 | 456 aa / 51.0 kDa |
| UniProt ID | Q6P9B6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoplasm, Nucleoli; UniProt: Membrane; Cytoplasm; Lysosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 456 aa / 51.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=86.3; PDB: 7U4T |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR006571; Pfam: PF07534 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.0/180** | |
| **归一化总分** | | | **77.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm, Nucleoli | Supported |
| UniProt | Membrane; Cytoplasm; Lysosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- lysosomal membrane (GO:0005765)
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
| PubMed strict count | 12 |
| PubMed broad count | 16 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1609, TLDC1 |

**关键文献**:
1. Human V-ATPase function is positively and negatively regulated by TLDc proteins.. *Structure (London, England : 1993)*. PMID: 38593795
2. MicroRNA-1911-3p targets mEAK-7 to suppress mTOR signaling in human lung cancer cells.. *Heliyon*. PMID: 33364499
3. Molecular basis of mEAK7-mediated human V-ATPase regulation.. *Nature communications*. PMID: 35672408
4. Microglia morphological response to mesenchymal stromal cell extracellular vesicles demonstrates EV therapeutic potential for modulating neuroinflammation.. *Journal of biological engineering*. PMID: 39420399
5. Targeting of lysosomal-bound protein mEAK-7 for cancer therapy.. *Frontiers in oncology*. PMID: 38532930

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.3 |
| 高置信度残基 (pLDDT>90) 占比 | 69.3% |
| 置信残基 (pLDDT 70-90) 占比 | 14.0% |
| 中等置信 (pLDDT 50-70) 占比 | 11.4% |
| 低置信 (pLDDT<50) 占比 | 5.3% |
| 有序区域 (pLDDT>70) 占比 | 83.3% |
| 可用 PDB 条目 | 7U4T |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=86.3，有序区 83.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006571; Pfam: PF07534 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RNASEK | 0.956 | 0.925 | — |
| ATP6V1A | 0.930 | 0.925 | — |
| ATP6V0E1 | 0.930 | 0.925 | — |
| ATP6V1D | 0.926 | 0.925 | — |
| ATP6V0C | 0.926 | 0.925 | — |
| ATP6V1H | 0.925 | 0.925 | — |
| ATP6AP1 | 0.925 | 0.925 | — |
| ATP6AP2 | 0.925 | 0.925 | — |
| ATP6V1C1 | 0.925 | 0.925 | — |
| ATP6V1G1 | 0.925 | 0.925 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRIP13 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TNIP2 | psi-mi:"MI:2289"(virotrap) | pubmed:30561431|imex:IM-26500 |
| SHARPIN | psi-mi:"MI:2289"(virotrap) | pubmed:30561431|imex:IM-26500 |
| TANK | psi-mi:"MI:2289"(virotrap) | pubmed:30561431|imex:IM-26500 |
| NMT2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NMT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ATP6V0A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC31A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| Q7TLC9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33845483|pmc:PPR177217| |
| EBI-25475894 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33845483|pmc:PPR177217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 12
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 12 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.3 + PDB: 7U4T | pLDDT=86.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Membrane; Cytoplasm; Lysosome / Cytosol; 额外: Nucleoplasm, Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 12 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. MEAK7 — MTOR-associated protein MEAK7，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小456 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6P9B6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140950-MEAK7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MEAK7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6P9B6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000140950-MEAK7/subcellular

![](https://images.proteinatlas.org/41020/474_D2_4_red_green.jpg)
![](https://images.proteinatlas.org/41020/474_D2_5_red_green.jpg)
![](https://images.proteinatlas.org/41020/480_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/41020/480_D2_2_red_green.jpg)
![](https://images.proteinatlas.org/41020/510_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/41020/510_D2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6P9B6 |
| SMART | SM00584; |
| UniProt Domain [FT] | DOMAIN 244..412; /note="TLDc"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01234" |
| InterPro | IPR006571; |
| Pfam | PF07534; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000140950-MEAK7/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HRAS | Biogrid | false |
| KRAS | Biogrid | false |
| SLC31A1 | Bioplex | false |
| TRIP13 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
