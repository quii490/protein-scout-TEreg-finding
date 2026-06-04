---
type: protein-evaluation
gene: "CIAO1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CIAO1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CIAO1 / CIA1, WDR39 |
| 蛋白名称 | Probable cytosolic iron-sulfur protein assembly protein CIAO1 |
| 蛋白大小 | 339 aa / 37.8 kDa |
| UniProt ID | O76071 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | x1 | 10 | 339 aa / 37.8 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=29 篇 (≤40→8) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=96.7; PDB: 3FM0 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR028608, IPR015943, IPR019775, IPR036322, IPR001 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.0/180** | |
| **归一化总分** | | | **65.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosolic [4Fe-4S] assembly targeting complex (GO:0097361)
- MMXD complex (GO:0071817)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 29 |
| PubMed broad count | 43 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CIA1, WDR39 |

**关键文献**:
1. CIAO1 and MMS19 deficiency: A lethal neurodegenerative phenotype caused by cytosolic Fe-S cluster protein assembly disorders.. *Genetics in medicine : official journal of the American College of Medical Genetics*. PMID: 38411040
2. CIAO1 loss of function causes a neuromuscular disorder with compromise of nucleocytoplasmic Fe-S enzymes.. *The Journal of clinical investigation*. PMID: 38950322
3. CIAO1 as a crucial signature gene of cuproptosis in gastric cancer.. *Oncology letters*. PMID: 40697348
4. A Novel Heterozygous Missense Variant in the CIAO1 Gene in a Family with Alzheimer's Disease: The Val67Ile Variant Promotes the Interaction of CIAO1 and Amyloid-β Protein Precursor.. *Journal of Alzheimer's disease : JAD*. PMID: 34569959
5. Structural insights into Fe-S protein biogenesis by the CIA targeting complex.. *Nature structural & molecular biology*. PMID: 32632277

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.7 |
| 高置信度残基 (pLDDT>90) 占比 | 95.3% |
| 置信残基 (pLDDT 70-90) 占比 | 3.8% |
| 中等置信 (pLDDT 50-70) 占比 | 0.6% |
| 低置信 (pLDDT<50) 占比 | 0.3% |
| 有序区域 (pLDDT>70) 占比 | 99.1% |
| 可用 PDB 条目 | 3FM0 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=96.7，有序区 99.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028608, IPR015943, IPR019775, IPR036322, IPR001680; Pfam: PF00400 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CIAO2B | 0.999 | 0.994 | — |
| CIAO2A | 0.999 | 0.972 | — |
| MMS19 | 0.999 | 0.958 | — |
| CIAO3 | 0.998 | 0.680 | — |
| SLC25A5 | 0.993 | 0.000 | — |
| ERCC2 | 0.986 | 0.661 | — |
| NUBP1 | 0.969 | 0.100 | — |
| SLC25A6 | 0.935 | 0.000 | — |
| NUBP2 | 0.885 | 0.150 | — |
| POLD1 | 0.839 | 0.524 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CIAO2B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CIAO2A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CCDC7 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| GOLM1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| galla-2 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| AKAP8L | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| NDUFA9 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ENSP00000418287.1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| RPAP1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MRPL24 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=96.7 + PDB: 3FM0 | pLDDT=96.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CIAO1 -- Probable cytosolic iron-sulfur protein assembly protein CIAO1，非常新颖，仅有少数基础研究。
2. 蛋白大小339 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 29 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O76071
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144021-CIAO1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CIAO1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O76071
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
