---
type: protein-evaluation
gene: "NSL1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NSL1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NSL1 / C1orf48 |
| 蛋白名称 | Kinetochore-associated protein NSL1 homolog |
| 蛋白大小 | 281 aa / 32.2 kDa |
| UniProt ID | Q96IY1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; UniProt: Nucleus; Chromosome, centromere, kinetochore |
| 蛋白大小 | 10/10 | ×1 | 10 | 281 aa / 32.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=31 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=75.9; PDB: 4NF9, 5LSI, 5LSJ, 5LSK, 8PPR, 8Q5H |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR013950; Pfam: PF08641 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Supported |
| UniProt | Nucleus; Chromosome, centromere, kinetochore | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- kinetochore (GO:0000776)
- MIS12/MIND type complex (GO:0000444)
- nuclear speck (GO:0016607)
- nucleus (GO:0005634)
- outer kinetochore (GO:0000940)
- spindle pole (GO:0000922)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 31 |
| PubMed broad count | 92 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C1orf48 |

**关键文献**:
1. Proxitome profiling reveals a conserved SGT1-NSL1 signaling module that activates NLR-mediated immunity.. *Molecular plant*. PMID: 39066482
2. A role for β-1,6- and β-1,3-glucans in kinetochore function in Saccharomyces cerevisiae.. *Genetics*. PMID: 37950911
3. A Multibreed Genome-Wide Association Study for Cattle Leukocyte Telomere Length.. *Genes*. PMID: 37628647
4. The NSL complex is required for piRNA production from telomeric clusters.. *Life science alliance*. PMID: 37399316
5. Dysfunction of Arabidopsis MACPF domain protein activates programmed cell death via tryptophan metabolism in MAMP-triggered immunity.. *The Plant journal : for cell and molecular biology*. PMID: 27711985

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.9 |
| 高置信度残基 (pLDDT>90) 占比 | 46.3% |
| 置信残基 (pLDDT 70-90) 占比 | 16.4% |
| 中等置信 (pLDDT 50-70) 占比 | 14.6% |
| 低置信 (pLDDT<50) 占比 | 22.8% |
| 有序区域 (pLDDT>70) 占比 | 62.7% |
| 可用 PDB 条目 | 4NF9, 5LSI, 5LSJ, 5LSK, 8PPR, 8Q5H |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4NF9, 5LSI, 5LSJ, 5LSK, 8PPR, 8Q5H）+ AlphaFold极高置信度预测（pLDDT=75.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013950; Pfam: PF08641 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KNL1 | 0.999 | 0.987 | — |
| MIS12 | 0.999 | 0.991 | — |
| DSN1 | 0.999 | 0.990 | — |
| PMF1 | 0.999 | 0.983 | — |
| ZWINT | 0.997 | 0.912 | — |
| SPC24 | 0.977 | 0.873 | — |
| NUF2 | 0.976 | 0.915 | — |
| PMF1-BGLAP | 0.966 | 0.000 | — |
| NDC80 | 0.965 | 0.885 | — |
| CBX5 | 0.959 | 0.793 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CEP70 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| USHBP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NINL | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PSME3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| KRT15 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TSG101 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| TRAF2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CALCOCO2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| KANSL1 | psi-mi:"MI:0096"(pull down) | pubmed:16189514|imex:IM-16520| |
| CCDC85B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.9 + PDB: 4NF9, 5LSI, 5LSJ, 5LSK, 8PPR,  | pLDDT=75.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome, centromere, kinetochore / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. NSL1 — Kinetochore-associated protein NSL1 homolog，非常新颖，仅有少数基础研究。
2. 蛋白大小281 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 31 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96IY1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000117697-NSL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NSL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96IY1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (supported)。来源: https://www.proteinatlas.org/ENSG00000117697-NSL1/subcellular

![](https://images.proteinatlas.org/53721/1334_D5_7_red_green.jpg)
![](https://images.proteinatlas.org/53721/1334_D5_8_red_green.jpg)
![](https://images.proteinatlas.org/53721/1773_C10_4_red_green.jpg)
![](https://images.proteinatlas.org/53721/1773_C10_6_red_green.jpg)
![](https://images.proteinatlas.org/53721/880_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/53721/880_F2_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96IY1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96IY1 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR013950; |
| Pfam | PF08641; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000117697-NSL1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CBX1 | Biogrid, Opencell | true |
| CBX5 | Intact, Biogrid | true |
| DSN1 | Intact, Biogrid, Bioplex | true |
| MIS12 | Intact, Biogrid, Opencell, Bioplex | true |
| NDC80 | Biogrid, Bioplex | true |
| NUF2 | Biogrid, Opencell, Bioplex | true |
| SPC24 | Biogrid, Bioplex | true |
| ZWINT | Intact, Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
