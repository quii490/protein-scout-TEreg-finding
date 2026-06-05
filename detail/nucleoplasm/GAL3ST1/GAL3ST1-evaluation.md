---
type: protein-evaluation
gene: "GAL3ST1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GAL3ST1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GAL3ST1 / CST |
| 蛋白名称 | Galactosylceramide sulfotransferase |
| 蛋白大小 | 423 aa / 48.8 kDa |
| UniProt ID | Q99999 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Vesicles; 额外: Nucleoplasm; UniProt: Golgi apparatus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 423 aa / 48.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=34 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR009729, IPR027417; Pfam: PF06990 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.5/180** | |
| **归一化总分** | | | **64.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm | Uncertain |
| UniProt | Golgi apparatus membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Golgi membrane (GO:0000139)
- membrane (GO:0016020)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 34 |
| PubMed broad count | 51 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CST |

**关键文献**:
1. Long-chain sulfatide enrichment is an actionable metabolic vulnerability in intraductal papillary mucinous neoplasm (IPMN)-associated pancreatic cancers.. *Gut*. PMID: 40268349
2. Multiomic analyses direct hypotheses for Creutzfeldt-Jakob disease risk genes.. *Brain : a journal of neurology*. PMID: 39865733
3. Genetic risk factors for Creutzfeldt-Jakob disease.. *Neurobiology of disease*. PMID: 32565065
4. A bidirectional link between sulfatide and Alzheimer's disease.. *Cell chemical biology*. PMID: 37972592
5. Copy number variation of GAL3ST1 gene is associated with growth traits of Chinese cattle.. *Animal biotechnology*. PMID: 35001788

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.2 |
| 高置信度残基 (pLDDT>90) 占比 | 72.3% |
| 置信残基 (pLDDT 70-90) 占比 | 14.7% |
| 中等置信 (pLDDT 50-70) 占比 | 5.9% |
| 低置信 (pLDDT<50) 占比 | 7.1% |
| 有序区域 (pLDDT>70) 占比 | 87.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.2，有序区 87.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009729, IPR027417; Pfam: PF06990 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UGT8 | 0.964 | 0.000 | — |
| GALC | 0.937 | 0.000 | — |
| NEU2 | 0.917 | 0.000 | — |
| NEU4 | 0.916 | 0.000 | — |
| GLA | 0.914 | 0.000 | — |
| NEU1 | 0.913 | 0.000 | — |
| NEU3 | 0.900 | 0.000 | — |
| LRIG3 | 0.815 | 0.781 | — |
| LRIG1 | 0.641 | 0.616 | — |
| ARSA | 0.581 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CHST8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NDUFA3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CANX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PSG4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LRIG3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PIGW | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LRIG1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PSG3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| Q7TLC9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33845483|pmc:PPR177217| |
| EBI-25475894 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33845483|pmc:PPR177217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 12
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 12 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.2 + PDB: 无 | pLDDT=88.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane / Vesicles; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 12 interactions | 数据充分 |

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
1. GAL3ST1 — Galactosylceramide sulfotransferase，非常新颖，仅有少数基础研究。
2. 蛋白大小423 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 34 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99999
- Protein Atlas: https://www.proteinatlas.org/ENSG00000128242-GAL3ST1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GAL3ST1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99999
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (uncertain)。来源: https://www.proteinatlas.org/ENSG00000128242-GAL3ST1/subcellular

![](https://images.proteinatlas.org/1220/50_C11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/1220/50_C11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/1220/52_C11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/1220/52_C11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/77138/1871_F3_17_cr5b51c39ab986e_blue_red_green.jpg)
![](https://images.proteinatlas.org/77138/1871_F3_23_cr5b51c39ab9d30_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
