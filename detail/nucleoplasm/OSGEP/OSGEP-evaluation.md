---
type: protein-evaluation
gene: "OSGEP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## OSGEP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | OSGEP / GCPL1 |
| 蛋白名称 | tRNA N6-adenosine threonylcarbamoyltransferase |
| 蛋白大小 | 335 aa / 36.4 kDa |
| UniProt ID | Q9NPF4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 335 aa / 36.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=35 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=96.6; PDB: 6GWJ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR043129, IPR000905, IPR017861, IPR034680, IPR017 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.0/180** | |
| **归一化总分** | | | **71.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- EKC/KEOPS complex (GO:0000408)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 35 |
| PubMed broad count | 48 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GCPL1 |

**关键文献**:
1. Mutations in KEOPS-complex genes cause nephrotic syndrome with primary microcephaly.. *Nature genetics*. PMID: 28805828
2. OSGEP regulates islet β-cell function by modulating proinsulin translation and maintaining ER stress homeostasis in mice.. *Nature communications*. PMID: 39622811
3. Disruption of tRNA threonylation triggers RIG-I mediated anti-tumour immune response.. *Nature communications*. PMID: 41735308
4. Novel homozygous OSGEP gene pathogenic variants in two unrelated patients with Galloway-Mowat syndrome: case report and review of the literature.. *BMC nephrology*. PMID: 30975089
5. O-Sialoglycoprotein Endopeptidase Deficiency Impairs Proteostasis and Induces Autophagy in Human Embryonic Stem Cells.. *International journal of molecular sciences*. PMID: 39063131

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.6 |
| 高置信度残基 (pLDDT>90) 占比 | 96.4% |
| 置信残基 (pLDDT 70-90) 占比 | 3.6% |
| 中等置信 (pLDDT 50-70) 占比 | 0.0% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 100.0% |
| 可用 PDB 条目 | 6GWJ |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=96.6，有序区 100.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043129, IPR000905, IPR017861, IPR034680, IPR017860; Pfam: PF00814 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GON7 | 0.999 | 0.973 | — |
| LAGE3 | 0.999 | 0.992 | — |
| TP53RK | 0.999 | 0.993 | — |
| TPRKB | 0.999 | 0.992 | — |
| YRDC | 0.976 | 0.000 | — |
| SLC4A1AP | 0.947 | 0.000 | — |
| EMCN | 0.926 | 0.292 | — |
| ACP1 | 0.802 | 0.000 | — |
| TBC1D23 | 0.791 | 0.790 | — |
| NUP43 | 0.758 | 0.727 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DNAJA1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| LAGE3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| RAB5C | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TP53RK | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| P/V | psi-mi:"MI:0096"(pull down) | pubmed:21911578|imex:IM-17703 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| BAG3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MBIP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HYKK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| POP7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=96.6 + PDB: 6GWJ | pLDDT=96.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. OSGEP — tRNA N6-adenosine threonylcarbamoyltransferase，非常新颖，仅有少数基础研究。
2. 蛋白大小335 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 35 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NPF4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000092094-OSGEP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=OSGEP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NPF4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
