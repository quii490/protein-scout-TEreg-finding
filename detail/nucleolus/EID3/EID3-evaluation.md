---
type: protein-evaluation
gene: "EID3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EID3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EID3 |
| 蛋白名称 | EP300-interacting inhibitor of differentiation 3 |
| 蛋白大小 | 333 aa / 38.2 kDa |
| UniProt ID | Q8N140 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli; UniProt: Nucleus; Cytoplasm; Chromosome, telomere |
| 蛋白大小 | 10/10 | ×1 | 10 | 333 aa / 38.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027786, IPR014854, IPR029225; Pfam: PF15412, PF |
| PPI 网络 | 10/10 | ×3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **154.5/180** | |
| **归一化总分** | | | **85.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli | Supported |
| UniProt | Nucleus; Cytoplasm; Chromosome, telomere | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromosome, telomeric region (GO:0000781)
- cytoplasm (GO:0005737)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- Smc5-Smc6 complex (GO:0030915)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 29 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Mesenchymal stem cell-derived extracellular vesicles subvert Th17 cells by destabilizing RORγt through posttranslational modification.. *Experimental & molecular medicine*. PMID: 36964252
2. Radiochemotherapy-induced DNA repair promotes the biogenesis of gastric cancer stem cells.. *Stem cell research & therapy*. PMID: 36153608
3. EID3 inhibits the osteogenic differentiation of periodontal ligament stem cells and mediates the signal transduction of TAZ-EID3-AKT/MTOR/ERK.. *Biochimica et biophysica acta. Molecular cell research*. PMID: 38216090
4. EP300-interacting inhibitor of differentiation 3 is required for spermatogenesis in mice.. *Andrology*. PMID: 39551708
5. EID3 Promotes Glioma Cell Proliferation and Survival by Inactivating AMPKα1.. *Journal of Korean Neurosurgical Society*. PMID: 36344477

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.0 |
| 高置信度残基 (pLDDT>90) 占比 | 21.0% |
| 置信残基 (pLDDT 70-90) 占比 | 41.1% |
| 中等置信 (pLDDT 50-70) 占比 | 19.8% |
| 低置信 (pLDDT<50) 占比 | 18.0% |
| 有序区域 (pLDDT>70) 占比 | 62.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=73.0，有序区 62.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027786, IPR014854, IPR029225; Pfam: PF15412, PF08743 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SMC5 | 0.999 | 0.972 | — |
| SMC6 | 0.999 | 0.976 | — |
| NSMCE2 | 0.998 | 0.968 | — |
| NSMCE1 | 0.998 | 0.979 | — |
| NSMCE3 | 0.996 | 0.889 | — |
| SUMO4 | 0.923 | 0.092 | — |
| EID2 | 0.921 | 0.292 | — |
| NSMCE4A | 0.907 | 0.000 | — |
| EID1 | 0.855 | 0.000 | — |
| SMC3 | 0.737 | 0.406 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| APPBP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| EID2B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| POGZ | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ARSA | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ACSL4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TLK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SMC5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NSMCE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NSMCE2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NSMCE3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 8 / 15 = 53%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 53%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.0 + PDB: 无 | pLDDT=73.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Chromosome, telomere / Nucleoplasm, Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. EID3 — EP300-interacting inhibitor of differentiation 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小333 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N140
- Protein Atlas: https://www.proteinatlas.org/ENSG00000255150-EID3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EID3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N140
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000255150-EID3/subcellular

![](https://images.proteinatlas.org/59367/1112_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/59367/1112_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/59367/1116_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/59367/1116_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/59367/1527_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/59367/1527_C4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N140-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
