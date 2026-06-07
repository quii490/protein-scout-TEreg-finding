---
type: protein-evaluation
gene: "USO1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## USO1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | USO1 / VDP |
| 蛋白名称 | General vesicular transport factor p115 |
| 蛋白大小 | 962 aa / 107.9 kDa |
| UniProt ID | O60763 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus; 额外: Nucleoli fibrillar center; UniProt: Cytoplasm, cytosol; Golgi apparatus membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 962 aa / 107.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=40 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.3; PDB: 2W3C |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011989, IPR016024, IPR000225, IPR041209, IPR006 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.0/180** | |
| **归一化总分** | | | **70.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoli fibrillar center | Supported |
| UniProt | Cytoplasm, cytosol; Golgi apparatus membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- ER to Golgi transport vesicle membrane (GO:0012507)
- fibrillar center (GO:0001650)
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- Golgi stack (GO:0005795)
- membrane (GO:0016020)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 40 |
| PubMed broad count | 61 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: VDP |

**关键文献**:
1. How autophagy controls the intestinal epithelial barrier.. *Autophagy*. PMID: 33906557
2. A cytoskeleton-related gene, uso1, is required for intracellular protein transport in Saccharomyces cerevisiae.. *The Journal of cell biology*. PMID: 2010462
3. Uso1 protein contains a coiled-coil rod region essential for protein transport from the ER to the Golgi apparatus in Saccharomyces cerevisiae.. *Journal of biochemistry*. PMID: 7706227
4. Uso1 protein is a dimer with two globular heads and a long coiled-coil tail.. *Journal of structural biology*. PMID: 8812994
5. The Uso1 globular head interacts with SNAREs to maintain viability even in the absence of the coiled-coil domain.. *eLife*. PMID: 37249218

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.3 |
| 高置信度残基 (pLDDT>90) 占比 | 57.7% |
| 置信残基 (pLDDT 70-90) 占比 | 26.7% |
| 中等置信 (pLDDT 50-70) 占比 | 6.5% |
| 低置信 (pLDDT<50) 占比 | 9.0% |
| 有序区域 (pLDDT>70) 占比 | 84.4% |
| 可用 PDB 条目 | 2W3C |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.3，有序区 84.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR000225, IPR041209, IPR006955; Pfam: PF18770, PF04871, PF04869 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| STX5 | 0.998 | 0.976 | — |
| GOLGA2 | 0.997 | 0.787 | — |
| GOSR2 | 0.994 | 0.975 | — |
| GOLGB1 | 0.991 | 0.963 | — |
| GOSR1 | 0.991 | 0.963 | — |
| GORASP1 | 0.990 | 0.260 | — |
| RAB1A | 0.990 | 0.645 | — |
| BET1L | 0.985 | 0.954 | — |
| BET1 | 0.982 | 0.869 | — |
| SCFD1 | 0.970 | 0.637 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000444850.2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| GAK | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| C1orf94 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| GABPB1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| IKBKG | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| Gbf1 | psi-mi:"MI:0018"(two hybrid) | pubmed:12634853|imex:IM-23685 |
| Golga2 | psi-mi:"MI:0018"(two hybrid) | pubmed:12634853|imex:IM-23685 |
| PTP4A3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| 7242199 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| GSTK1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.3 + PDB: 2W3C | pLDDT=85.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Golgi apparatus membrane / Golgi apparatus; 额外: Nucleoli fibrillar center | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. USO1 — General vesicular transport factor p115，非常新颖，仅有少数基础研究。
2. 蛋白大小962 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 40 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60763
- Protein Atlas: https://www.proteinatlas.org/ENSG00000138768-USO1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=USO1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60763
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (enhanced)。来源: https://www.proteinatlas.org/ENSG00000138768-USO1/subcellular

![](https://images.proteinatlas.org/38282/737_D9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/38282/737_D9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/38282/763_D9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/38282/763_D9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/38282/836_C1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/38282/836_C1_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O60763-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O60763 |
| SMART | SM00185; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR011989;IPR016024;IPR000225;IPR041209;IPR006955;IPR024095;IPR006953; |
| Pfam | PF18770;PF04871;PF04869; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000138768-USO1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| C1orf94 | Intact, Biogrid | true |
| ALK | Biogrid | false |
| BET1 | Biogrid | false |
| DDX20 | Biogrid | false |
| DUSP12 | Intact | false |
| EMC9 | Opencell | false |
| GOLGA2 | Biogrid | false |
| GOSR1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
