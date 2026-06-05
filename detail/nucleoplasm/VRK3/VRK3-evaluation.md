---
type: protein-evaluation
gene: "VRK3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## VRK3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | VRK3 |
| 蛋白名称 | Serine/threonine-protein kinase VRK3 |
| 蛋白大小 | 474 aa / 52.9 kDa |
| UniProt ID | Q8IV63 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Vesicles; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 474 aa / 52.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=26 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=79.8; PDB: 2JII |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050235, IPR011009, IPR000719, IPR026870; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.0/180** | |
| **归一化总分** | | | **70.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles | Approved |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 26 |
| PubMed broad count | 30 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. RNF144a induces ERK-dependent cell death under oxidative stress via downregulation of vaccinia-related kinase 3.. *Journal of cell science*. PMID: 33067254
2. Single-cell transcriptome-wide Mendelian randomization and colocalization reveal cell-specific mechanisms in systemic lupus erythematosus.. *Rheumatology (Oxford, England)*. PMID: 41233983
3. VRK3-mediated inactivation of ERK signaling in adult and embryonic rodent tissues.. *Biochimica et biophysica acta*. PMID: 18035061
4. Novel Alzheimer Disease Risk Loci and Pathways in African American Individuals Using the African Genome Resources Panel: A Meta-analysis.. *JAMA neurology*. PMID: 33074286
5. Presumed pseudokinase VRK3 functions as a BAF kinase.. *Biochimica et biophysica acta*. PMID: 25899223

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.8 |
| 高置信度残基 (pLDDT>90) 占比 | 63.5% |
| 置信残基 (pLDDT 70-90) 占比 | 9.7% |
| 中等置信 (pLDDT 50-70) 占比 | 3.2% |
| 低置信 (pLDDT<50) 占比 | 23.6% |
| 有序区域 (pLDDT>70) 占比 | 73.2% |
| 可用 PDB 条目 | 2JII |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=79.8，有序区 73.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050235, IPR011009, IPR000719, IPR026870; Pfam: PF00069, PF13240 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DUSP3 | 0.979 | 0.095 | — |
| BANF1 | 0.646 | 0.359 | — |
| BANF2 | 0.587 | 0.132 | — |
| LTV1 | 0.586 | 0.514 | — |
| NCL | 0.557 | 0.292 | — |
| PARP1 | 0.546 | 0.292 | — |
| H4C6 | 0.522 | 0.510 | — |
| HMGA2 | 0.515 | 0.203 | — |
| MAPK3 | 0.507 | 0.091 | — |
| STRADA | 0.503 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DSG1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TWF2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TSG101 | psi-mi:"MI:0018"(two hybrid) | imex:IM-11696|pubmed:19549727 |
| RAN | psi-mi:"MI:0096"(pull down) | imex:IM-9273|pubmed:18617507 |
| VRK1 | psi-mi:"MI:0096"(pull down) | imex:IM-9273|pubmed:18617507 |
| ZNF524 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NR2E1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IRF2 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| SP4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.8 + PDB: 2JII | pLDDT=79.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm, Vesicles | 一致 |
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
1. VRK3 — Serine/threonine-protein kinase VRK3，非常新颖，仅有少数基础研究。
2. 蛋白大小474 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 26 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IV63
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105053-VRK3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=VRK3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IV63
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000105053-VRK3/subcellular

![](https://images.proteinatlas.org/56489/1035_B11_1_red_green.jpg)
![](https://images.proteinatlas.org/56489/1035_B11_4_red_green.jpg)
![](https://images.proteinatlas.org/56489/982_A8_1_red_green.jpg)
![](https://images.proteinatlas.org/56489/982_A8_2_red_green.jpg)
![](https://images.proteinatlas.org/56489/985_A8_1_red_green.jpg)
![](https://images.proteinatlas.org/56489/985_A8_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IV63-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
